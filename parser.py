from abc import ABC, abstractclassmethod


class Parser(ABC):

    @abstractclassmethod
    def request(self, text: str) -> str:
        pass