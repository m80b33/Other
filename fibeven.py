def f(n):
    f1 = f2 = 1
    for i in range(n):
        f1 , f2 = f2, f1 + f2
        if f2 % 2 != 0:
            while True:
                f1 , f2 = f2, f1 + f2
                if f2 % 2 == 0:
                    print(f2)
                    break
        else:
            print(f2)
