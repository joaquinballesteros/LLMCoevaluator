import os
from LLMEvaluation.utils.llm_base import LLMBase
from LLMEvaluation.utils.base_assesment import BaseAssesment
from LLMEvaluation.APIs.openai_llm import OpenAILLM
from LLMEvaluation.APIs.antrophic_llm import AnthropicLLM

# Assesment to test :)
from LLMEvaluation.courses.dataStructures.assesments.polyAssesment.poly_c import PolyC
from LLMEvaluation.courses.dataStructures.assesments.splayTreeAssesment.splay_tree_java import (
    SplayTreeJava,
)
from LLMEvaluation.courses.objectOrientedProgramming.assesments.AlergySystem.alergy_system import (
    AlergySystem,
)


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
                result_file = os.path.splitext(student)[0] + "Result.html"
                with open(result_file, "w") as f:
                    f.write(result)
                    print(f"Result saved in: {result_file}")

    def getEvaluation(self, student):
        buildOutput, prompt = self.assessment.read_test(
            student
        )  # Build the project and get the prompt
        response = self.llm.evaluate_submission(
            prompt
        )  # Evaluate the student's code using a LLM
        return (
            f"{buildOutput}<br>\n" + response
        )  # Combine the build output and the LLM response


# Example usage
# Student submissions are in a folder named "assesmentExampleJava"
# Each submission is in a folder named after the student
# The folder structure is as follows, is the name of the student (the same as in the CSV file), and a structure of folders and files:
# assesmentExampleJava/
#   student1/
#     submission1.java
#     submission2.java
#     folder1/
#       submission3.java
#   student2/
#     submission1.java
#     submission2.java
#     folder1/
#       submission3.java


# Prueba a evaluar en Java con Maven, un solo fichero java
# studentAssesmentsFolder="./LLMEvaluation/courses/dataStructures/assesments/splayTreeAssesment/students/"
# assessment = EvaluateStudents(studentAssesmentsFolder, OpenAILLM("o3-mini"), SplayTreeJava())


# Prueba en C, un solo fichero por estudiante.
# studentAssesmentsFolder="./LLMEvaluation/courses/dataStructures/assesments/polyAssesment/students/"
# assessment = EvaluateStudents(studentAssesmentsFolder, AnthropicLLM("claude-3-5-haiku-20241022"), PolyC())


# Prueba a evaluar en Java con Maven, una estructura completa, se espera que los estudiantes tengan el src/ y luego el resto de carpetas
studentAssesmentsFolder = "./LLMEvaluation/courses/objectOrientedProgramming/assesments/AlergySystem/students/"
assessment = EvaluateStudents(
    studentAssesmentsFolder, OpenAILLM("o3-mini"), AlergySystem()
)


assessment.processSubmissions()
