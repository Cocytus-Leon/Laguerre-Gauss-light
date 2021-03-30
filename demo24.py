# %%
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import special
print("Ready!")
# %%


def car2pol(A, B):
    r = np.sqrt(A*A+B*B)
    theta = np.arctan(B/A)
    return r, theta


def r_over_limit(R):
    A = []
    B = []

    for i in range(R.shape[0]):
        for j in range(R.shape[1]):
            if R[i, j] > a:
                A.append(i)
                B.append(j)
    return A, B


# %%
a = 5  # * radius of fiber core
x = np.linspace(-a, a, 100)
y = np.linspace(-a, a, 100)
[X, Y] = np.meshgrid(x, y)
r, theta = car2pol(X, Y)
A, B = r_over_limit(r)
# %%
m = 3  # *次数
l = 3  # *阶数
W = 1
s = np.sqrt(2)*r/W
E = s**l*sp.special.eval_genlaguerre(m, l, s*s)*np.exp(-s*s/2)
I = E**2
for k in range(len(A)):
    I[A[k]][B[k]] = 0
plt.imshow(I)
plt.title('LP$\mathregular{{_{}}}$$\mathregular{{_{}}}$'.format(l, m))
plt.show()
# %%
