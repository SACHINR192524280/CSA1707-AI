import numpy as np

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

W1 = np.random.rand(2,2)
W2 = np.random.rand(2,1)

def sigmoid(x):
    return 1/(1+np.exp(-x))

for _ in range(10000):
    h = sigmoid(X @ W1)
    o = sigmoid(h @ W2)

    e = y - o
    W2 += h.T @ (e * o * (1-o)) * 0.5
    W1 += X.T @ ((e * o * (1-o)) @ W2.T * h * (1-h)) * 0.5

print("Output:")
print(np.round(o))