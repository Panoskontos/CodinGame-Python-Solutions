
powers = []
n = int(input())
for i in range(n):
    pi = int(input())
    powers.append(pi)

m = 1000
powers.sort()

for i in range(1, len(powers)):
    if m > abs(powers[i] - powers[i-1]):
        m = abs(powers[i] - powers[i-1])

print(m)

# To debug: print("Debug messages...", file=sys.stderr, flush=True)

