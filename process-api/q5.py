import os

def main():
    pid = os.fork()

    # child process
    if pid == 0:
        pid2 = os.fork()

        ## child-child process
        if pid2 == 0:
            for i in range(5,10) :
                print("[child-child process] {} !!".format(i))
        elif pid2 > 0:
            os.wait()
            for i in range(5) :
                print("[child process] {} !!".format(i))
        
            
    elif pid > 0:
        os.wait()
        print("[parent process] done!")

main()