#DATBASES

##Encoding
Data(unicode) is moved across systems,  characters must be encoded properly. Most common encoding sceme is utf-8
Ascii
characters are represent between numbers 0 -256
print(ord("H"))
Each character is stored in 8 bits , meaning 1 byte of memeory.
ASCII /Latin / Arabic
utf-8 (1(ascii)-4 Bytes)
Python2
2 Kinds of String (Normal String and unicode string)
Python3

Python3: Byte String is different from string, Unicode is same as string in python3
Python2: Byte String is same as string, unicode is different than string

Python3
=======
Computer  Internet
Unicode    UTF-8
SEND: 'string'.encoding('utf-8') -> byte string
RECEIVE: b''.decode('utf-8')
