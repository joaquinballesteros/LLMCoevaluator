from abc import ABC, abstractmethod


class LLMBase(ABC):
    llm = None
    model = None

    def __init__(self, model=None):
        self.model = model

    @abstractmethod
    def evaluate_submission(self, prompt):
        pass
