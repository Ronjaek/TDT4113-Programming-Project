import arduino_connect  # This is the key import so that you can access the serial port.

# Codes for the 5 signals sent to this level from the Arduino

_dot = 0
_dash = 1
_symbol_pause = 2  # pause between dot and dash
_letter_pause = 3  # pause between letters
_word_pause = 4  # pause between words
_reset = 5  # define when the sentence is over


# Morse Code Class
class mocoder():
    _morse_codes = {'01': 'a', '1000': 'b', '1010': 'c', '100': 'd', '0': 'e', '0010': 'f', '110': 'g', '0000': 'h',
                    '00': 'i', '0111': 'j',
                    '101': 'k', '0100': 'l', '11': 'm', '10': 'n', '111': 'o', '0110': 'p', '1101': 'q', '010': 'r',
                    '000': 's', '1': 't',
                    '001': 'u', '0001': 'v', '011': 'w', '1001': 'x', '1011': 'y', '1100': 'z', '01111': '1',
                    '00111': '2', '00011': '3',
                    '00001': '4', '00000': '5', '10000': '6', '11000': '7', '11100': '8', '11110': '9', '11111': '0'}

    # This is where you set up the connection to the serial port.
    def __init__(self, sport=True):
        if sport:
            self.serial_port = arduino_connect.basic_connect()
        self.reset()

    def reset(self):
        self.current_message = ''
        self.current_word = ''
        self.current_symbol = ''

    # This should receive an integer in range 1-4 from the Arduino via a serial port
    def read_one_signal(self, port=None):
        connection = port if port else self.serial_port
        while True:
            # Reads the input from the arduino serial connection
            data = connection.readline()
            if data:
                return data

    # The signal returned by the serial port is one (sometimes 2) bytes, that represent characters of a string.  So,
    # a 2 looks like this: b'2', which is one byte whose integer value is the ascii code 50 (ord('2') = 50).  The use
    # of function 'int' on the string converts it automatically.   But, due to latencies, the signal sometimes
    # consists of 2 ascii codes, hence the little for loop to cycle through each byte of the signal.

    def decoding_loop(self):

        # O = dot, 1 = dash in the _morse_codes dictionary below
        _morse_codes = {'01': 'a', '1000': 'b', '1010': 'c', '100': 'd', '0': 'e', '0010': 'f', '110': 'g', '0000': 'h',
                        '00': 'i', '0111': 'j',
                        '101': 'k', '0100': 'l', '11': 'm', '10': 'n', '111': 'o', '0110': 'p', '1101': 'q', '010': 'r',
                        '000': 's', '1': 't',
                        '001': 'u', '0001': 'v', '011': 'w', '1001': 'x', '1011': 'y', '1100': 'z', '01111': '1',
                        '00111': '2', '00011': '3',
                        '00001': '4', '00000': '5', '10000': '6', '11000': '7', '11100': '8', '11110': '9',
                        '11111': '0'}

        counter = 0
        letterSigns = ''
        word = ''
        t = 0

        while True:
            s = self.read_one_signal(self.serial_port)
            #print(s)
            for byte in s:  # This is the way to read value form serial gate so tha twe can make an int
                # self.process_signal(int(chr(byte)))

                t = int(chr(byte))

            if t != 5:  # if t=5 the code is finished
                print(t)
                if (t == 0 or t == 1):  # reciving 0 or 1 means it is either a dot or a dash
                    letterSigns += str(t)
                #elif t == 2: # pause between dash and dot, i am not adding anything here
                #    pass # technically unnecessary
                elif t == 3:  # pause between letters, adds the current letter to the word and adds space to word after
                    word += _morse_codes[letterSigns]  # adding the coresponding letter
                    letterSigns = ''
                elif t == 4:  # pause between words, adds the current letter to the word and adds space to word after
                    word += _morse_codes[letterSigns]
                    letterSigns = ''
                    word += ' '
                counter = 1  # changes the counter from 0, such that it can end after a button has been pressed

            elif (t == 5 and counter != 0):  # the lights are off and the code ends
                word += _morse_codes[letterSigns]
                print(word)
                break

    # Dummy method
    def process_signal(self, sig):
        return True


''' To test if this is working, do the following in a Python command window:

> from morse_skeleton import *
> m = mocoder()
> m.decoding_loop()

If your Arduino is currently running and hooked up to the serial port, then this
simple decoding loop will print the raw signals that the Arduino sends to
the serial port.  Each time you press (or release) your morse-code device, a signal should
appear in your Python window. In Python, these signals typically look like this:
 b'5' or b'1' or b'3', etc.

path:
1. cd Documents/2.klasse_data/PycharmProjects/Oving1_proglab2/
2. python3
3. Kommandoer: cd, pwd (hvor jeg er), ls
4. control + c -> stoppe program 
5. exit 
'''