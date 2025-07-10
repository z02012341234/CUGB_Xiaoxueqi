# solver_factory.py
from src.pde_solver import FiniteDifferenceSolver, PDESolver
from src.pde_problem import HeatEquation, PDEProblem
from src.grid import Grid

class SolverFactory:
    @staticmethod
    def create_problem(name: str, **kwargs) -> PDEProblem:
        if name.lower() == "heat":
            return HeatEquation(alpha=kwargs.get("alpha", 1.0))
        else:
            raise ValueError(f"未知 PDE 问题：{name}")

    @staticmethod
    def create_solver(method: str) -> PDESolver:
        if method.lower() == "fd_explicit":
            return FiniteDifferenceSolver()
        else:
            raise ValueError(f"未知求解方法：{method}")
