def flag(n):
    if n in (1, 2):
        return 2
    return flag(n - 1) + flag(n - 2)


a = int(input("N="))
print(flag(a))


