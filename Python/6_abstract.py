fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])


def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result
