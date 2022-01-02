light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

thorx = initial_tx
thory = initial_ty

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    move = ''
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    
    # vertical
    if thory < light_y:
        thory +=1
        move +='S'
    if thory > light_y:
        thory -=1
        move +='N'
    
    # horizontal
    if thorx < light_x:
        thorx += 1
        move += 'E'
    if thorx > light_x:
        thorx -= 1
        move += 'W'

    print(move)