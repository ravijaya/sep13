from os import listdir


def power(x, n):
    return x ** n, x ** 2, x ** 3


def ls(dir_path='.'):
    for item in listdir(dir_path):
        print(item)


if __name__ == '__main__':
    print(power(2, 3))
    ls()
