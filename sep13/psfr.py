def demo():
    fp = None

    try:
        fp = open('test.txt')
        1 / 0
        print(fp.read())
    except FileNotFoundError as err:
        print(err)
    finally:
        # mandate block
        if fp:
            fp.close()


while True:
    try:
        demo()
    except:
        print('error...')
