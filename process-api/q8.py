import os

LENGTH = 4096

def main():
    child1 = os.fork()

    # child1 process
    if child1 == 0:
        (read_fd, write_fd) = os.pipe()

        child2 = os.fork()

        # child2 process
        if child2 == 0:
            os.close(write_fd)
            # this will be blocked til message comes from child1 process
            byte = os.read(read_fd, LENGTH)
            print("[child2 process] {}".format(str(byte)))
            os.close(read_fd)
        # child1 process
        elif child2 > 0:
            os.close(read_fd)
            os.write(write_fd, "this is message for child2 process from child1 process")
            os.close(write_fd)
            os.wait()

    # parent process
    elif child1 > 0:
        os.wait()
        print("[parent process] all done!!")


main()