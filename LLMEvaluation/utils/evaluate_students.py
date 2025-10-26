import os
from LLMEvaluation.APIs.llm_base import LLMBase
from LLMEvaluation.utils.base_assesment import BaseAssesment





class EvaluateStudents:
    llm = None
    assessment = None
    base_folder = None

    def __init__(self, base_folder, llm: LLMBase, assessment: BaseAssesment):
        self.llm = llm
        self.assessment = assessment
        self.base_folder = base_folder

    def processSubmissions(self):
        for filename in os.listdir(self.base_folder):
            print("---------------------------")
            print(filename)
            if "." in filename:
                print("Hidden file, skipping to the next one")
                continue

            student = os.path.join(self.base_folder, filename + "/")
            result = self.getEvaluation(student)

            if result is None:
                print(
                    "Could not evaluate the student's code. Please review the code and try again."
                )
            else:
                result_file = os.path.splitext(student)[0] + self.assessment.output_file_name
                with open(result_file, "w") as f:
                    f.write(result)
                    print(f"Result saved in: {result_file}")

    def getEvaluation(self, student):
        buildOutput, prompt = self.assessment.read_test(
            student
        )  #Build the project and get the prompt

        if prompt is None:
            print("No prompt generated, skipping this submission.")
            return f"{buildOutput}<br>\n"
        
        response = self.llm.evaluate_submission(
            prompt
        )  # Evaluate the student's code using a LLM
        return (
            f"{buildOutput}<br>\n" + response
        )  # Combine the build output and the LLM response


# # Example usage
# # Student submissions are in a folder named "assesmentExampleJava"
# # Each submission is in a folder named after the student
# # The folder structure is as follows, is the name of the student (the same as in the CSV file), and a structure of folders and files:
# # assesmentExampleJava/
# #   student1/
# #     submission1.java
# #     submission2.java
# #     folder1/
# #       submission3.java
# #   student2/
# #     submission1.java
# #     submission2.java
# #     folder1/
# #       submission3.java


# # Prueba en C, un solo fichero por estudiante.
# # studentAssesmentsFolder="./LLMEvaluation/courses/dataStructures/assesments/polyAssesment/students/"
# # assessment = EvaluateStudents(studentAssesmentsFolder, AnthropicLLM("claude-3-5-haiku-20241022"), PolyC())


# # Prueba a evaluar en Java con Maven, una estructura completa, se espera que los estudiantes tengan el src/ y luego el resto de carpetas
# #studentAssesmentsFolder = "./LLMEvaluation/courses/objectOrientedProgramming/assesments/AlergySystem/students/"
# #assessment = EvaluateStudents(
# #    studentAssesmentsFolder, OpenAILLM("o3-mini"), AlergySystem()
# #)


# # Prueba a evaluar en Java, una estructura completa, se espera que los estudiantes tengan el src/ y luego el resto de carpetas
# #studentAssesmentsFolder = "./LLMEvaluation/courses/objectOrientedProgramming/assesments/Telehealth/students/"
# #assessment = EvaluateStudents(
# #    studentAssesmentsFolder, OpenAILLM("gpt-4o-mini"), TelehealthSystem()
# #)
# # assessment.processSubmissions()

# # Prueba a evaluar en Java, una estructura completa, se espera que los estudiantes tengan el src/ y luego el resto de carpetas
# studentAssesmentsFolder = "./LLMEvaluation/courses/objectOrientedProgramming/assesments/Caidas/students/"
# allfiles_names=["Caida", "Usuario", "Even", "Movi", "Siste", "Noti","Fractura"]

# prompUsuario = EvaluateStudents(
#     studentAssesmentsFolder, OpenAILLM("o4-mini"), Caida_UsuarioVigiliado("ResultUsuarioVigilado.html", file_names=["Caida", "Usuario", "Even", "Movi", "Siste", "Noti","Fractura"])
# )
# prompUsuario.processSubmissions()

# promptSistemaDeteccion = EvaluateStudents(
#     studentAssesmentsFolder, OpenAILLM("o4-mini"), Caida_SistemaDeteccion("ResultSistemaDeteccion.html", file_names=allfiles_names)
# )
# promptSistemaDeteccion.processSubmissions()

# promptCaidaConfirmada = EvaluateStudents(
#     studentAssesmentsFolder, OpenAILLM("o4-mini"), Caida_CaidaConfirmada("ResultCaidaConfirmada.html", file_names=["Caida", "Even", "Siste", "Noti","Fractura"])
# )
# promptCaidaConfirmada.processSubmissions()  

# promptAmagoCaida = EvaluateStudents(
#     studentAssesmentsFolder, OpenAILLM("o4-mini"), Caida_AmagoCaida("ResultAmagoCaida.html", file_names=["Caida", "Even", "Siste", "Noti"])
# )
# promptAmagoCaida.processSubmissions()   

# promptMovimientoBrusco = EvaluateStudents(
#     studentAssesmentsFolder, OpenAILLM("o4-mini"), Caidas_MovimientoBrusco("ResultMovimientoBrusco.html", file_names=["Ex","Movi", "Even"])
# )
# promptMovimientoBrusco.processSubmissions()

# promptNotificable = EvaluateStudents(
#     studentAssesmentsFolder, OpenAILLM("o4-mini"), Caidas_Notificable("ResultNotificable.html", file_names=["notificable"])
# )
# promptNotificable.processSubmissions()  

# promptFracturaAsociada = EvaluateStudents(
#     studentAssesmentsFolder, OpenAILLM("o4-mini"), Caidas_FracturaAsociada("ResultFracturaAsociada.html", file_names=["asoc"])
# )
# promptFracturaAsociada.processSubmissions()

# prompCaidaException = EvaluateStudents(
#     studentAssesmentsFolder, OpenAILLM("o4-mini"), Caidas_Excepcion("ResultCaidaException.html", file_names=["ex"])
# )
# prompCaidaException.processSubmissions()


# promptEvento = EvaluateStudents(
#     studentAssesmentsFolder, OpenAILLM("o4-mini"), Caidas_Evento("ResultEvento.html", file_names=["evento"])
# )
# promptEvento.processSubmissions()   






