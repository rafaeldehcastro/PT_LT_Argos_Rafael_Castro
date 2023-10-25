from typing import List, Union
from abc import ABC, abstractmethod

# Paso 1: Definir la interfaz para los agentes

class Agent(ABC):
    @abstractmethod
    def getMedia(self, numbers: List[Union[int, float]]) -> float:
        pass

# Paso 2: Implementar los tres agentes (A, B y C) que heredan de la interfaz

class AgentA(Agent):
    def getMedia(self, numbers: List[Union[int, float]]) -> float:
        return sum(numbers) / len(numbers)


class AgentB(Agent):
    def getMedia(self, numbers: List[Union[int, float]]) -> float:
        if 0 in numbers:  # Evitar la división por cero
            raise ValueError("The list contains a zero, which is invalid for harmonic mean computation.")
        return len(numbers) / sum(1/x for x in numbers)


class AgentC(Agent):
    def getMedia(self, numbers: List[Union[int, float]]) -> float:
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        if n % 2 == 1:  # Impar
            return sorted_numbers[n // 2]
        else:  # Par
            mid1, mid2 = sorted_numbers[(n-1) // 2], sorted_numbers[n // 2]
            return (mid1 + mid2) / 2

# Paso 3: Fábrica para habilitar la selección dinámica de agentes

class AgentFactory:
    @staticmethod
    def create_agent(agent_type: str) -> Agent:
        if agent_type == "A":
            return AgentA()
        elif agent_type == "B":
            return AgentB()
        elif agent_type == "C":
            return AgentC()
        else:
            raise ValueError(f"Agent type '{agent_type}' is not recognized.")
