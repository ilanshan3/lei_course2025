import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams


x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)


Z1 = np.exp(-(X**2 + Y**2))
Z2 = np.exp(-(X**2 + 5 * Y**2))
Z3 = 0.1 * ((X - 1)**2 + (Y + 1)**2) / 2

fig = plt.figure(figsize=(15, 4))


ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='viridis')
ax1.set_title("Standard Gaussian")

ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='viridis')
ax2.set_title("Elliptical Gaussian")


ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(X, Y, Z3, cmap='viridis')
ax3.set_title("MSE Loss Surface: $\\frac{1}{2}(x - y)^2$")

plt.tight_layout()
rcParams['font.family'] = 'SimHei'
plt.tight_layout(rect=[0, 0, 1, 0.9])
plt.suptitle("高斯函数和MSE损失函数")
plt.show()
