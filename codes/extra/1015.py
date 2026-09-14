import numpy as np

def distance(x1,y1,x2,y2):
    dist = np.sqrt((x2-x1)**2 + (y2-y1)**2)

    return dist

c1 = input().split()
x1 = float(c1[0])
y1 = float(c1[1])

c2 = input().split()
x2 = float(c2[0])
y2 = float(c2[1])

print(f"{distance(x1,y1,x2,y2):.4f}")