from dotenv import load_dotenv  # Para cargar las variables de entorno
import os  # Para cargar las variables de entorno
from LLMEvaluation.APIs.llm_base import LLMBase  # Importar la clase base correcta
from openai import OpenAI

class DeepSeekLLM(LLMBase):
    deep_seek = None  # Atributo para almacenar la instancia de OpenAI

    def __init__(self, model="claude-3-5-haiku-20241022"):
        super().__init__(model)

        # Cargamos la variable de entorno desde el archivo .env
        load_dotenv()
        deepseek_api_key = os.getenv("DEEPSEEKER_API_KEY")

        if deepseek_api_key:
            print(f"DeepSeek API Key exists and begins {deepseek_api_key[:7]}")
        else:
            input_folder = os.path.dirname(
                os.path.abspath(__file__)
            )  # It takes the direction of the current file and append de students folder
            raise ValueError(
                "DeepSeek API Key not set. .env file not found on " + input_folder
            )

        self.model = model  # Asignamos el modelo LLM
        self.deep_seek = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")


    def evaluate_submission(self, prompt):
        if prompt is None or prompt == "":
            raise ValueError("Prompt cannot be None or empty")
        # Construimos el mensaje para el modelo
        response = self.deep_seek.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": prompt},
            ],
            stream=False
        )
        return response.choices[0].message.content
