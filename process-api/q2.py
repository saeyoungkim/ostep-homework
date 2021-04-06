import os

def main():
    with open('test_q2','a') as f:
        pid = os.fork()

        if pid==0:
            f.write("[child process] write!!")
        elif pid>0:
            f.write("[parent process] write!!")
    
    return 0

main()