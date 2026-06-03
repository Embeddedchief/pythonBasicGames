def add_one(num):
    if num >= 11:
        return num + 1
    total = num +1
    print(total)
    return add_one(total)


print(add_one(0))