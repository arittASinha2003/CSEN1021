import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(1, 20)
# print(x)

# x = np.linspace(1, 50, 24)
# y = x ** 3
# plt.plot(x, y)
# plt.show()

# x = np.array(["CSE", "ECE", "CIVIL", "MECH"])
# y = np.array([600, 300, 100, 100])

# plt.bar(x, y, width = 0.4, color = 'blue')
# plt.pie(y)
# plt.show()

fig, ax = plt.subplots()
ax.set(xlim = (-1, 1), ylim = (-1, 1))
a_circle = plt.Circle((0, 0), 0.5, color = 'cyan')
ax.add_artist(a_circle)
plt.show()