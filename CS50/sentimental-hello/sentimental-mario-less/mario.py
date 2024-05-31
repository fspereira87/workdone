# TODO
from cs50 import get_int


h = get_int("Height: ")


while h < 1 or h > 8:
    h = int(input("Height: "))


for i in range(h):
    for _ in range (h-i-1):
        print(" ", end="")
    for _ in range (i+1):
        print ("#", end="")
    print()




