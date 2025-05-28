# App.py

import random
import matplotlib.pyplot as plt
from SortMethods import SortMethods
from Benchmarking import Benchmarking
from typing import List, Dict, Callable, Tuple

class App:
    def __init__(self, tam: List[int], maxi_tam: int):
        self.tam = tam
        self.maxi_tam= maxi_tam
        self.arreglo_base = []
        self.algoritmos: Dict[str, Callable] = {
            "bubble": SortMethods.sort_bubble,
            "bubbleMejorado": SortMethods.sort_bubble_optimized,
            "seleccion": SortMethods.sort_selection,
            "insercion": SortMethods.sort_insertion,
            "shell": SortMethods.sort_shell
        }
        self.resultados: List[Tuple[int, str, float]] = []

    def build_arreglo(self, tamano: int) -> List[int]:
        
        return [random.randint(1, 10000) for _ in range(tamano)]

    def main(self):
        
        for tamano in self.tamano:
            arr = self.build_arreglo(tamano)
            for nombre_algoritmo, algoritmo in self.algoritmos.items():
                tiempo = Benchmarking.medir_tiempo(algoritmo, arr.copy())
                self.resultados.append((tamano, nombre_algoritmo, tiempo))
        
        self.show_results()

    def show_results(self):
        algoritmos = ["bubble", "bubbleMejorado", "seleccion", "insercion", "shell"]
        for algoritmo in algoritmos:
            tiempos = [tiempo for tamano, nombre, tiempo in self.resultados if nombre == algoritmo]
            tamanos = [tamano for tamano, nombre, tiempo in self.resultados if nombre == algoritmo]
            plt.plot(tamanos, tiempos, label=algoritmo)

        plt.xlabel("Tamaño del Arreglo")
        plt.ylabel("Tiempo de Ejecución (segundos)")
        plt.title("Comparativa de Tiempos de Métodos de Ordenamiento")
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    tamanos = [5000, 10000, 30000, 50000, 100000]
    app = App(tamano=tamanos, max_tamano=100000)
    app.main()
