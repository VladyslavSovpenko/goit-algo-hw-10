import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0
b = 2

n_points = 10000

x_rand = np.random.uniform(a, b, n_points)
y_rand = np.random.uniform(0, max(f(x_rand)), n_points)

under_curve = y_rand < f(x_rand)

monte_carlo_result = (b - a) * max(f(x_rand)) * np.sum(under_curve) / n_points
print(f"Інтеграл методом Монте-Карло: {monte_carlo_result}")

quad_result, error = spi.quad(f, a, b)
print(f"Інтеграл за допомогою quad: {quad_result} з помилкою {error}")

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
