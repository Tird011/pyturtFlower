blue = -2
red = 2
sulk = 10

while True:
    hallow = blue + red
    if hallow == 0:
        purple = 5
        if purple >= 0:
            print("honored")
        else:
            print("still a negative")
            break
    else:
        print("gg")
        #adjustment
        if hallow > 0:
            blue -= 1 
        else:
            red += 1 
if hallow - 10 >= sulk:#-15 is the magic number
     if sulk >= hallow:
        print("win")
     else:
        print("lose")
else:
    print("kitkat💀")