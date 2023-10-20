def fact(num=5):
    return 1 if num == 0 else num * fact(num - 1)


if __name__ == '__main__':
    print(fact())
