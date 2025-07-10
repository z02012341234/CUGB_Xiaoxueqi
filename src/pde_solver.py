from abc import ABC, abstractmethod
import numpy as np
from typing import Tuple
from src.pde_problem import PDEProblem
from src.grid import Grid

class PDESolver(ABC):
    @abstractmethod
    def solve(self, problem: PDEProblem, grid: Grid) -> np.ndarray:
        pass

class FiniteDifferenceSolver(PDESolver):
    def solve(self, problem: PDEProblem, grid: Grid) -> np.ndarray:
        alpha, dx, dt = problem.alpha, grid.dx, grid.dt
        nx, nt = grid.nx, grid.nt
        r = alpha * dt / dx**2
        if r > 0.5:
            raise ValueError(f"稳定性条件 r={r:.3f} 超出范围(r<=0.5)")
        u = np.zeros((nt, nx))
        u[0, :] = problem.initial_condition(grid.x)

        for n in range(0, nt - 1):
            u[n+1, 1:-1] = u[n, 1:-1] + r * (u[n, 2:] - 2*u[n, 1:-1] + u[n, :-2])
            u[n+1, :] = problem.boundary_conditions(u[n+1, :])

        return u
