from abc import ABC, abstractclassmethod


class Parser():

    @abstractclassmethod
    def request(self, text: str) -> None:
        pass