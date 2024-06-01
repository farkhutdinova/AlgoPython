n = 16

for i in range(1, n):
    if i % 3 == 0 and i % 5 == 0:
        print("fizz,buzz")
    else:
        if i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
                print("buzz")
        else:
            print(i)
