import numpy as np

class Grid:
    def __init__(self, x_start, x_end, nx, t_start, t_end, nt):
        self.x_start = x_start
        self.x_end = x_end
        self.t_start = t_start
        self.t_end = t_end

        self.nx = nx
        self.nt = nt
        self.dx = (x_end - x_start) / (nx - 1)
        self.dt = (t_end - t_start) / (nt - 1)

        self.x = np.linspace(x_start, x_end, nx)
        self.t = np.linspace(t_start, t_end, nt)
