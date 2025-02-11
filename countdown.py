import time

def countdown(t):
    try:
        t=int(t)
        if t<=0:
            print("Enter positive interger for countdown")
            return
        while t>0:
            mins,secs=divmod(t,60)
            timer='{:02d}:{:02d}'.format(mins,secs)
            print(timer,end="\r")
            time.sleep(1)
            t-=1
            print('FIRE IN THE HOLE!!')
    except ValueError:
        print("INVALID INPUT")   


t=input("Enter the time in seconds: ")

countdown(t)

