import os  # Para cargar las variables de entorno

from dotenv import load_dotenv  # Para cargar las variables de entorno

from LLMEvaluation.utils.llm_base import LLMBase  # Importar la clase base correcta
from openai_llm import OpenAI  # Para cargar las variables necesarias para la API de OpenAI


class OpenAILLM(LLMBase):
    openai = None  # Atributo para almacenar la instancia de OpenAI

    def __init__(self, model="o3-mini"):
        super().__init__(model)

        # Cargamos la variable de entorno desde el archivo .env
        load_dotenv()
        openai_api_key = os.getenv("OPENAI_API_KEY")

        if openai_api_key:
            print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
        else:
            input_folder = os.path.dirname(
                os.path.abspath(__file__)
            )  # It takes the direction of the current file and append de students folder
            raise ValueError(
                "OpenAI API Key not set. .env file not found on " + input_folder
            )

        self.model = model  # Asignamos el modelo LLM
        self.openai = OpenAI()  # Inicializamos la instancia de OpenAI

    def evaluate_submission(self, prompt):
        if prompt is None or prompt == "":
            raise ValueError("Prompt cannot be None or empty")

        message = [{"role": "user", "content": prompt}]

        response = self.openai.chat.completions.create(
            messages=message, model=self.model
        )
        return response.choices[0].message.content
