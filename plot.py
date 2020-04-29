import matplotlib.pyplot as plt
import numpy as np
import serial

t = np.arange(0, 10, 0.1)
a = []
m = []


serdev = '/dev/ttyACM0'
s = serial.Serial(serdev)
for i in range(100):
    line = s.readline()
    value = float(line)
    a.append(value)
    line = s.readline()
    value = int(line)
    m.append(value)

plt.subplot(211)
plt.xlabel("t")
plt.ylabel("ax")
plt.plot(t, a, label = "a")


plt.subplot(212)
plt.xlabel("t")
plt.ylabel("displacement > 5cm")
plt.stem(t, m)

plt.show()

s.close()
