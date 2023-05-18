# import matplotlib

# print(matplotlib.__version__)

# #Draw a line in a diagram from position (0,0) to position (6,250):

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.show()

##################
# Plotting without line
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'x')
plt.show()