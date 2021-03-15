import numpy as np
import matplotlib.pyplot as plot

time = np.arange(0, 10, 0.1)
amplitude = np.cos(time)

plot.plot(time, amplitude)

plot.title("Cosine curve")

plot.xlabel("Time")

plot.ylabel("Amplitude")

plot.show()
