import os
import sys

def main():
    pid = os.fork()

    if pid == 0:
        sys.stdout.flush()
        os.execv('/bin/ls', ['/bin/ls', '-al', '.'])
    elif pid > 0:
        os.wait()
        print("[parent process] child process completed!!")

main()