import anthropic  # Para cargar las variables necesarias para la API de Anthropic
from dotenv import load_dotenv  # Para cargar las variables de entorno
import os  # Para cargar las variables de entorno
from LLMEvaluation.utils.llm_base import LLMBase  # Importar la clase base correcta


class AnthropicLLM(LLMBase):
    claude = None  # Atributo para almacenar la instancia de OpenAI

    def __init__(self, model="claude-3-5-haiku-20241022"):
        super().__init__(model)

        # Cargamos la variable de entorno desde el archivo .env
        load_dotenv()
        anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

        if anthropic_api_key:
            print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
        else:
            input_folder = os.path.dirname(
                os.path.abspath(__file__)
            )  # It takes the direction of the current file and append de students folder
            raise ValueError(
                "Anthropic API Key not set. .env file not found on " + input_folder
            )

        self.model = model  # Asignamos el modelo LLM
        self.claude = anthropic.Client(api_key=anthropic_api_key)

    def evaluate_submission(self, prompt):
        if prompt is None or prompt == "":
            raise ValueError("Prompt cannot be None or empty")
        # Construimos el mensaje para el modelo
        response = self.claude.messages.create(
            model=self.model,
            max_tokens=5000,
            temperature=0.1,
            messages=[
                {"role": "user", "content": prompt},
            ],
        )

        return response.content[0].text
