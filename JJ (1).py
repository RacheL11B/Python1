import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frame):
    ball.set_ydata(ball.get_ydata() - 0.1)  
    return ball,

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

ball = ax.plot(5, 10, 'o')[0]

anim = animation.FuncAnimation(fig, update, frames=100, interval=50)

plt.show()