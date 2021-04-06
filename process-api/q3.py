import os
import signal

def handler(signum, frame):
    print("goodbye")

def main():
    parent = os.getpid()
    rc = os.fork()

    # child process
    if rc == 0:
        print("hello")
        os.kill(parent, signal.SIGCONT)
    elif rc > 0:
        # set signal handler
        signal.signal(signal.SIGCONT, handler)
        # wait till signal comes
        signal.pause()

main()