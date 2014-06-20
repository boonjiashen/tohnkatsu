"Demo the use of the _Getch class"

import Getch
getch = Getch._Getch()
while 1:
    print "Enter keystroke (or ESC to escape):"
    char = getch()
    esc = '\x1b'
    if char == esc:
        break
    print char
