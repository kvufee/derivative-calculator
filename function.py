import re
import sympy as sp
import numpy as np
from sympy.abc import x

from . import Parser


class InputParser(Parser):

    def __init__(self) -> None:
        pass

    def parsing(self, text: str) -> str:
        match