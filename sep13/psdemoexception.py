def cat(*args):
    try:
        info = {}
        info['paramater123']

        for file_name in args:
            for line in open(file_name):
                print(line, end='')
    except FileNotFoundError as error:
        print(error)
    except ZeroDivisionError as ravi:
        print(ravi)
    except Exception as err:
        raise


try:
    cat('/etc/resolv.conf2')
except KeyError as err:
    print(err)
