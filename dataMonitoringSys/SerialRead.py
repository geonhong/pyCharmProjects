import serial

with serial.Serial('/dev/tty.usbmodemFD141', 9600, timeout=1) as s:
    while(True):
        l = s.readline()
        arr = l.decode("utf-8").split('\t')
        if arr[0] == 'p':
            print(arr)
            break