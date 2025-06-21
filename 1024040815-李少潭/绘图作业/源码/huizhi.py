import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

plt.style.use('seaborn-v0_8-whitegrid')
colors = ['dodgerblue', 'forestgreen', 'red', 'gold']


x_vals = {
    'γ': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
    'κ': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
    'λ_VR': [0.5, 0.8, 1.0, 2.0],
    'λ_SR': [0.01, 0.1, 0.5, 1.0, 2.0]
}


def gen_data(length):
    return [np.random.uniform(62, 65) for _ in range(length)], \
        [np.random.uniform(70, 73) for _ in range(length)], \
        [np.random.uniform(66, 69) for _ in range(length)], \
        [np.random.uniform(73, 76) for _ in range(length)]


titles = ['(a) Varying γ effect', '(b) Varying κ effect', '(c) Varying λ_VR effect', '(d) Varying λ_SR effect']
x_labels = ['γ', 'κ', 'λ_VR', 'λ_SR']

fig, axs = plt.subplots(1, 4, figsize=(20, 5), sharey=True)

for i, ax in enumerate(axs):
    key = list(x_vals.keys())[i]
    x = x_vals[key]
    u, s, h, acc = gen_data(len(x))

    ax.plot(x, u, marker='o', color=colors[0], label='U')
    ax.plot(x, s, marker='s', color=colors[1], label='S')
    ax.plot(x, h, marker='^', color=colors[2], label='H')
    ax.plot(x, acc, marker='D', color=colors[3], label='acc')

    ax.set_title(titles[i], fontsize=11)
    ax.set_xlabel(x_labels[i], fontsize=10)
    if i == 0:
        ax.set_ylabel('Accuracy (%)')
    ax.set_ylim(60, 78)
    ax.legend(fontsize=8)

rcParams['font.family'] = 'SimHei'
plt.suptitle("四个超参数对准确率的影响", fontsize=14)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
