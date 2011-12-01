#!/usr/bin/env python
# coding: utf-8

import serial


def two_digits(n):
    if n < 10:
        return '0' + str(n)
    else:
        return str(n)

COLOR_NAMES = ('red', 'green', 'blue', 'magenta', 'cyan', 'gray')
COLORS = dict(zip(COLOR_NAMES, range(31, 38)))
BACKGROUND_COLORS = dict(zip(COLOR_NAMES, range(41, 48)))

def color(text, color=None, background=None):
    if color:
        text = '\033[%dm%s\033[0m' % (COLORS[color], text)
    if background:
        text = '\033[%dm%s\033[0m' % (BACKGROUND_COLORS[background], text)
    return text

def countdown(state):
    seconds = int(state.split(':')[1])
    minutes = int(state.split(':')[0])
    exceptions = ((4, 30), (4, 40), (4, 50), (4, 52), (4, 54), (4, 56),
                  (4, 58))
    if (minutes, seconds) in exceptions or \
         minutes >= 5 or \
         (minutes > 0 and seconds == 0) or \
         (seconds < minutes * 2 and seconds % 2 == 0):
        return 'R'
    else:
        return 'G'

if __name__ == '__main__':
    import glob
    import sys
    import time

    MAPPING = {'R': '1', 'G': '2'}
    BAUD_RATE = 9600
    TIMEOUT = 0.1

    serial_ports = glob.glob('/dev/ttyUSB0') + glob.glob('/dev/ttyACM0')
    if not len(serial_ports):
        print 'ERROR: no Arduino found'
        exit(1)

    serial_port = serial_ports[0]
    arduino = serial.Serial(serial_port, BAUD_RATE, timeout=TIMEOUT)
    time.sleep(2)
    start_time = time.time()
    while True:
        try:
            seconds_passed = int(time.time() - start_time)
            minute = seconds_passed / 60
            second = seconds_passed % 60
            timer = '%s:%s' % (two_digits(minute), two_digits(second))
            state = countdown(timer)
            arduino.write(MAPPING[state])
            if state == 'R':
                sys.stdout.write('\r' + color(timer, 'red'))
            else:
                sys.stdout.write('\r' + color(timer, 'green'))
            sys.stdout.flush()
            time.sleep(1)
        except KeyboardInterrupt:
            break
