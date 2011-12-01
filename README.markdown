Python+Arduino-based Lightning Talks Countdown
==============================================

This software shows a 5-minute countup (need to fix it to countdown) timer in
the terminal and sends information to Arduino turn on/off the red or green
lights.

To make it work:

- Connect a red light to digital port 4 and green to digital 2 of your Arduino;
- Upload `countdown.ino` to your Arduino;
- Plug your Arduino in your computer using a USB cable;
- Run `python countdown.py`


Requirements
------------

You need to install [pyserial](http://pyserial.sourceforge.net/). To do so,
execute:

    pip install pyserial

or:

    aptitude install python-serial

(If do you use Ubuntu, execute `sudo apt-get install aptitude` and be happy)
