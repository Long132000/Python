import numpy as np

# Исходные коэффициенты
A = np.array([
    [-23.98, 1.50, -8.78, 7.74],
    [-8.70, -28.73, 3.86, 8.08],
    [1.62, 3.88, -18.17, -8.68],
    [-6.97, 1.96, 1.55, -29.54]
])

# Правая часть
B = np.array([-0.04, 7.86, -0.44, -2.02])

# Решение системы
solution = np.linalg.solve(A, B)

# Вычисление невязок
residuals = B - A.dot(solution)

# Вывод результатов
print("Решение:", np.round(solution, 3))
print("Невязки:", np.round(residuals, 3))
