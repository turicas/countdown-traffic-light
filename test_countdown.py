#!/usr/bin/env python

from countdown import countdown, two_digits
import unittest


class TestCountdown(unittest.TestCase):
    def test_all_in_minute_zero(self):
        self.assertEquals(countdown('0:00'), 'G')
        for second in range(1, 60):
            self.assertEquals(countdown('0:' + two_digits(second)), 'G')

    def test_all_in_minute_one(self):
        self.assertEquals(countdown('1:00'), 'R')
        for second in range(1, 60):
            self.assertEquals(countdown('1:' + two_digits(second)), 'G')

    def test_all_in_minute_two(self):
        self.assertEquals(countdown('2:00'), 'R')
        self.assertEquals(countdown('2:01'), 'G')
        self.assertEquals(countdown('2:02'), 'R')
        for second in range(3, 60):
            self.assertEquals(countdown('2:' + two_digits(second)), 'G')

    def test_all_in_minute_three(self):
        self.assertEquals(countdown('3:00'), 'R')
        self.assertEquals(countdown('3:01'), 'G')
        self.assertEquals(countdown('3:02'), 'R')
        self.assertEquals(countdown('3:03'), 'G')
        self.assertEquals(countdown('3:04'), 'R')
        for second in range(5, 60):
            self.assertEquals(countdown('3:' + two_digits(second)), 'G')

    def test_all_in_minute_four(self):
        self.assertEquals(countdown('4:00'), 'R')
        self.assertEquals(countdown('4:01'), 'G')
        self.assertEquals(countdown('4:02'), 'R')
        self.assertEquals(countdown('4:03'), 'G')
        self.assertEquals(countdown('4:04'), 'R')
        self.assertEquals(countdown('4:05'), 'G')
        self.assertEquals(countdown('4:06'), 'R')
        for second in range(7, 30):
            self.assertEquals(countdown('4:' + two_digits(second)), 'G')
        self.assertEquals(countdown('4:30'), 'R')
        for second in range(31, 40):
            self.assertEquals(countdown('4:' + two_digits(second)), 'G')
        self.assertEquals(countdown('4:40'), 'R')
        for second in range(41, 50):
            self.assertEquals(countdown('4:' + two_digits(second)), 'G')
        self.assertEquals(countdown('4:50'), 'R')
        for second in range(50, 60):
            if second % 2 == 0:
                state = 'R'
            else:
                state = 'G'
            self.assertEquals(countdown('4:' + two_digits(second)), state)

    def test_minute_five_and_so_on(self):
        for minute in range(5, 10):
            for second in range(60):
                self.assertEquals(countdown('%02d:%02d' % (minute, second)),
                                  'R')
