from abc import ABC, abstractmethod
import numpy as np

class PDEProblem(ABC):
    def __init__(self, alpha):
        self.alpha = alpha
    @abstractmethod
    def initial_condition(self, x: np.ndarray) -> np.ndarray:
        pass
    @abstractmethod
    def boundary_conditions(self, u: np.ndarray) -> np.ndarray:
        pass
    
class HeatEquation(PDEProblem):

    def __init__(self, alpha):
        super().__init__(alpha)

    def initial_condition(self, x):
        return np.exp(-100 * (x - 0.5)**2)

    def boundary_conditions(self, u):
        u[0] = 0
        u[-1] = 0
        return u
