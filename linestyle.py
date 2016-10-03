import numpy as np
import matplotlib.pyplot as plt

dashes = [40, 2, 4, 4]  # 40 points on, 2 off, 4 on, 4 off
x = np.linspace(0, 10, 500)
y = np.sin(x)

# Set dash style via the Line method `set_dashes`
line, = plt.plot(x, y, '--', linewidth=2, color='0.25',
                 label="set_dashes({0})".format(dashes))
line.set_dashes(dashes)

# Set dash style directly via the `linestyle` keyword argument
# NB: The offset `dy` is "manually" adjusted to get a smooth evolution of the
# dashes offsets along the line stack.
for offset, dy in zip([-10, -5, 0, 5, 10], [-0.4, -0.2, 0.2, 0.4, 0.6]):
    ls = str((offset, dashes))
    import pdb;pdb.set_trace()
    l= plt.plot(x, y + dy, ls=ls, lw=2, label="ls={0}".format(ls))

#plt.legend(loc='lower right', fontsize='small')
#plt.axvline(0.95, color='0.8')  # to compare the offset values more easily
plt.show()
