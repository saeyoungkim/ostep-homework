import os

def main():
    value = 100

    pid = os.fork()

    # child process
    if pid == 0:
        value = 200
        print('[child process] value : {}'.format(value))
    elif pid > 0:
        value = 300
        print('[parent process] value : {}'.format(value))

    return 0

main()