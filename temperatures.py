
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
m = 10000
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

    if abs(t) < abs(m):
            m = t
    elif abs(t) == abs(m):
            m = abs(t)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
if (m==10000):
    print(0)
else:
    print(m)
