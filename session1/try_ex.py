import math

x = 528

def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))

y = calc(x)
print("y=", y)
