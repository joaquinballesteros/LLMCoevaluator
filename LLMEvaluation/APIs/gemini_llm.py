import os  # Para cargar las variables de entorno

from dotenv import load_dotenv  # Para cargar las variables de entorno

from LLMEvaluation.APIs.llm_base import LLMBase  # Importar la clase base correcta

from google import genai

class GeminiLLM(LLMBase):
    genimi = None  # Atributo para almacenar la instancia de OpenAI

    def __init__(self, model="gemini-2.0-flash"):
        super().__init__(model)

        # Cargamos la variable de entorno desde el archivo .env
        load_dotenv()
        gemini_api_key = os.getenv("GEMINI_API_KEY")

        if gemini_api_key:
            print(f"Gemini API Key exists and begins {gemini_api_key[:8]}")
        else:
            input_folder = os.path.dirname(
                os.path.abspath(__file__)
            )  # It takes the direction of the current file and append de students folder
            raise ValueError(
                "Gemini API Key not set. .env file not found on " + input_folder
            )

        self.model = model  # Asignamos el modelo LLM
        self.genimi = genai.Client(api_key=gemini_api_key)

    def evaluate_submission(self, prompt):
        if prompt is None or prompt == "":
            raise ValueError("Prompt cannot be None or empty")

        response = self.genimi .models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text
