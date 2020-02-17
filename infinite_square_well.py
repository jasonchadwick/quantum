from numpy import sqrt,sin,pi,linspace,e
from matplotlib import pyplot as plt
from matplotlib import animation
import cmath

fig = plt.figure()
ax = plt.axes(xlim=(0,1), ylim=(0,3))
line, = ax.plot([],[],lw=2)

def init():
  line.set_data([],[])
  return line,

def psi(n, x):
  return sin(n * pi * x)

def phi(n, t):
  return cmath.exp(-1j * n**2 * t)

def eigenfunc(n, x, t):
  return sqrt(2) * psi(n, x) * phi(n, t)

def superpos(weights, maxn, x, t):
  s=0
  weights = normalize(weights)
  for n in range(maxn):
    s += weights[n] * eigenfunc(n + 1, x, t)
  return s

def normalize(weights):
  s = sqrt(sum([w**2 for w in weights]))
  return [w/s for w in weights]

def animate(i, w, c):
  x = linspace(0,1,1000)
  y = abs(superpos(w,c,x,i/100))**2
  line.set_data(x, y)
  return line,

def make_animation(weights, maxnum):
  anim = animation.FuncAnimation(fig, animate, 1000, init, fargs=(weights,maxnum), interval=40, blit=True)
  plt.show()

make_animation([1,1],2)