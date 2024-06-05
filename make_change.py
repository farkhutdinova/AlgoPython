def make_change(target_amount):
    denominators = [200, 100, 50, 20, 10, 5, 2, 1]
    n = 0
    result = []

    for d in denominators:
        while target_amount >= d:
            target_amount -= d
            n += 1
            result.append(d)
    return n, result

print(make_change(24)) # 3: 20p + 2p + 2p
print(make_change(163)) # 5: £1 + 50p + 10p + 2p + 1p