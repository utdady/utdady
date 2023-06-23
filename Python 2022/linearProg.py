import numpy as np
import cvxpy as cp

def problem2():
    x = cp.Variable(shape=(3, 1), name='x')

    A1 = np.array([[122, 237, 307], [95, 130, 180]])
    A2 = np.array([0, 0, 0])
    B = np.array([[3000], [2000]])

    constraints = [cp.matmul(A1, x) <= B, cp.matmul(A2, x) >= 0, x >= 0]

    r = np.array([800, 1300, 1800])
    objective = cp.Maximize(cp.matmul(r, x))

    problem = cp.Problem(objective, constraints)

    solution = problem.solve()
    print(solution)
    print(x.value)

if __name__ == '__main__':
    problem2()
