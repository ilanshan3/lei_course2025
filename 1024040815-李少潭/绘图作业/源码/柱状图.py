import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

np.random.seed(0)


data_image = np.random.normal(loc=0.5, scale=0.05, size=1000000)
data_text = np.random.normal(loc=0.25, scale=0.1, size=1000000)
data_cross = np.random.normal(loc=0.05, scale=0.035, size=1000000)

colors = ['#60a6e0', '#f4a259', '#83c167']

plt.hist(data_image, bins=50, alpha=0.6, label='image-to-image',
         color=colors[0], edgecolor='black')
plt.hist(data_text, bins=45, alpha=0.6, label='text-to-text',
         color=colors[1], edgecolor='black')
plt.hist(data_cross, bins=30, alpha=0.6, label='image-to-text',
         color=colors[2], edgecolor='black')

plt.xlabel("Cosine Similarity")
plt.ylabel("Count")
plt.legend()
plt.grid(True)
plt.tight_layout()
rcParams['font.family'] = 'SimHei'
plt.suptitle("不同模态之间的余弦相似度分布情况", fontsize=14)
plt.show()
