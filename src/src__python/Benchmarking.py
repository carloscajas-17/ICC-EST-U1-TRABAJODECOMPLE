

from typing import List, Callable
import time

class Benchmarking:
    @staticmethod
    def medir_tiempo(func: Callable, array: List[int]) -> float:
       
        inicio = time.time()
        func(array)
        fin = time.time()
        return fin - inicio
