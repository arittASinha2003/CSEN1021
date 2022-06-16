import matplotlib.pyplot as plt
import numpy as np

## Using Line
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
# print(xpoints)
# print(ypoints)
# plt.plot(xpoints, ypoints)
# plt.show()

## Using Dots
# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints, 'o')
# plt.show()

# Default X - Points
# ypoints = np.array([3, 8, 1, 10, 5, 7])
# plt.plot(ypoints)
# plt.show()

## Markers
## https://matplotlib.org/3.1.1/api/markers_api.html
## https://www.geeksforgeeks.org/matplotlib-markers-module-in-python/
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'D')  # Diamond
# plt.show()

## Format Strings
## Syntax: marker | line | color
## https://www.w3schools.com/python/matplotlib_markers.asp
## https://matplotlib.org/2.0.2/api/colors_api.html
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, 'o-.m') # Dot | Dashed Dotted | Magenta
# plt.show()

## Marker Size
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20)
# plt.show()

## Marker Color (Edge Color)
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# plt.show()

## Marker Face Color (Inside Color)
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
# plt.show()

## Linestyles
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, ls = ':')
# plt.show()

## Line Color
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, color = 'r')
# plt.show()

## Line Width
# ypoints = np.array([3, 8, 1, 10])
# plt.plot(ypoints, linewidth = '20.5')
# plt.show()

## Title, X - Label, Y - Label, Grid
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x, y)
# plt.title("Sports Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.grid()
# plt.show()

## Subplots
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.title('One')
plt.plot(x, y)

# Plot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.title('Two')
plt.plot(x, y)
plt.suptitle('Main')
plt.show()