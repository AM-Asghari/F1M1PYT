import time

t = int(input("Hoeveel seconden moet de timer op staan? "))

while t :
    mins = t // 60
    secs = t % 60
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1
print("Je hebt net je tijd verspilt, congrats!")