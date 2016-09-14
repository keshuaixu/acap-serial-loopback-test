import serial
import time
import random

repeat = 1000
port = '/dev/ttyACM0'


# port = '/dev/ttyUSB0'


def loop_once(ser):
    # out = 'a'.encode()
    # out = bytearray([random.randrange(0, 128) for _ in range(0, 8)])
    out = bytearray([random.randrange(0, 255)])
    time_start = time.clock()
    ser.write(out)
    # ser.flush()
    lo_in = ser.read()
    elapsed = time.clock() - time_start
    match = False
    if lo_in == out:
        match = True
        print('.', end='')
    else:
        print('x', end='')
    return match, elapsed


with serial.Serial(port, baudrate=115200, timeout=1.) as ser:
    time.sleep(1.)
    print('start')
    match = []
    elapsed = []
    for i in range(0, repeat):
        m, e = loop_once(ser)
        match.append(m)
        elapsed.append(e)
        if i % 100 == 99:
            print(' {}/{} E{}'.format(i + 1, repeat, i + 1 - sum(match)))
    print('\nmatch : {}/{}'.format(sum(match), repeat))
    print('time us: avg {}, max {}, min {}'.format(sum(elapsed) * 1e6 / repeat, max(elapsed) * 1e6, min(elapsed) * 1e6))
