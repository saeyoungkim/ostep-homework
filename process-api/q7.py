import os

STDOUT_FILENO = 1

def main():
    pid = os.fork()

    # child process
    if pid == 0:
        fd = os.open("q7-test.txt", os.O_RDWR, 0)
        os.close(STDOUT_FILENO)
        os.write(fd, "[child process] hi hello".encode())
        os.fsync(fd)
    elif pid > 0:
        os.wait()
        print("[paraent process] bye")


main()