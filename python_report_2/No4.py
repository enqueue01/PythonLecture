def fact(num=5):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


if __name__ == '__main__':
    print(fact())
