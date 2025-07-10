import numpy as np
from src.grid import Grid
from src.solver_factory import SolverFactory

def main():
    alpha = 0.5
    t0, t1 = 0.0, 0.1
    x0, x1, nx = 0.0, 1.0, 51
    dx = (x1 - x0) / (nx - 1)
    dt_max = 0.5 * dx*dx / alpha
    dt = 0.8 * dt_max
    nt = int((t1 - t0) / dt) + 1

    print(f"自动配置：dx={dx:.5f}, dt={dt:.5f}, nt={nt}")

    problem = SolverFactory.create_problem("heat", alpha=alpha)
    grid   = Grid(x_start=x0, x_end=x1, nx=nx,
                  t_start=t0, t_end=t1, nt=nt)

    solver = SolverFactory.create_solver("fd_explicit")
    solution = solver.solve(problem, grid)

    print("初始时 max(u)=%.5f" % np.max(solution[0]))
    print("末时   max(u)=%.5f" % np.max(solution[-1]))
    np.save("heat_solution.npy", solution)
    print("解已保存到 heat_solution.npy")

if __name__ == "__main__":
    main()
