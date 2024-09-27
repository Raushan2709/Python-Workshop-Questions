
def sum(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum = sum * 3
    return sum
print(sum(1, 2, 3))
print(sum(3, 3, 3))
