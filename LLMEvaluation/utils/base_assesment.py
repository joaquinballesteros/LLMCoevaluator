from abc import ABC, abstractmethod
import os


class BaseAssesment(ABC):
    def __init__(self):
        """
        Initializes the base assessment class.

        This constructor is intended to be called by subclasses that implement specific assessment.
        It sets up the necessary structure for creating custom assessment classes by inheritance.
        """

    @abstractmethod
    def general_rubric(self):
        pass

    @abstractmethod
    def specific_rubric(self):
        pass

    @abstractmethod
    def sample_output(self):
        pass

    @abstractmethod
    def build_project(self, input_folder):
        pass

    def read_test(self, input_folder):
        studentCode, buildOutput = self.build_project(input_folder)
        if not studentCode or not buildOutput:
            return None, None

        prompt = f"""{self.general_rubric()}
        {self.specific_rubric()}
        {self.sample_output()}
        Evalua el siguiente código del estudiante que {buildOutput}:
        {studentCode}"""

        return buildOutput, prompt
