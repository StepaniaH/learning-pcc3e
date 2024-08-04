import matplotlib.pyplot as plt
from die import Die

# 创建两个D6骰子
die_1 = Die()
die_2 = Die()

# 进行多次投掷,并将结果存储在列表中
results = [die_1.roll() + die_2.roll() for _ in range(1000)]

# 分析结果
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
frequencies = [results.count(value) for value in poss_results]

# 使用matplotlib可视化结果
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(poss_results, frequencies, align='center', color='skyblue', edgecolor='navy')

# 设置图表标题和标签
ax.set_title("Results of Rolling Two D6 Dice 1,000 Times", fontsize=18)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency", fontsize=14)

# 设置刻度
ax.set_xticks(poss_results)

# 设置y轴的范围,使图表更美观
ax.set_ylim(0, max(frequencies) * 1.1)

plt.tight_layout()
plt.show()

import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np

def random_walk_2d(steps):
    x, y = 0, 0
    x_walk = [x]
    y_walk = [y]
    
    for _ in range(steps):
        dx, dy = np.random.choice([-1, 1]), np.random.choice([-1, 1])
        x += dx
        y += dy
        x_walk.append(x)
        y_walk.append(y)
    
    return x_walk, y_walk

# 生成随机游走数据
steps = 1000
x_walk, y_walk = random_walk_2d(steps)

# 创建图表
fig = make_subplots(rows=1, cols=2, 
                    subplot_titles=("2D Random Walk", "Distance from Origin"),
                    specs=[[{"type": "scatter"}, {"type": "scatter"}]])

# 添加2D随机游走轨迹
fig.add_trace(
    go.Scatter(x=x_walk, y=y_walk, mode='lines+markers', name='Walk Path'),
    row=1, col=1
)

# 计算并添加距离原点的距离
distances = np.sqrt(np.array(x_walk)**2 + np.array(y_walk)**2)
fig.add_trace(
    go.Scatter(x=list(range(steps+1)), y=distances, mode='lines', name='Distance from Origin'),
    row=1, col=2
)

# 更新布局
fig.update_layout(height=500, width=1000, title_text="2D Random Walk Visualization")
fig.update_xaxes(title_text="X", row=1, col=1)
fig.update_yaxes(title_text="Y", row=1, col=1)
fig.update_xaxes(title_text="Step", row=1, col=2)
fig.update_yaxes(title_text="Distance", row=1, col=2)

fig.show()
