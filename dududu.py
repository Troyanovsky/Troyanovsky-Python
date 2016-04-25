# -*- coding: utf-8 -*-
name = str(raw_input("What is your first name?      "))
name = name.upper()
print name
if name == "NAN":
    l = "♥"
    blank_1 = 10
    blank_2 = 9
    paint_1 = 3
    print blank_1*" "+paint_1*l++blank_2*" "+paint_1*l+blank_1*" "

    blank_1 = 8
    blank_2 = 5
    paint_1 = 7
    while blank_2 >= 0:
        print blank_1*" "+paint_1*l+blank_2*" "+paint_1*l+blank_1*" "
        blank_1 = blank_1 - 1
        paint_1 = paint_1 + 2
        blank_2 = blank_2 - 2
    paint_1 = paint_1 * 2 - 1
    while paint_1 >= 0:
        print blank_1*" "+paint_1*l+blank_1*" "
        blank_1 += 2
        paint_1 -= 4
    print " "*13+chr(105).upper(),chr(108)+chr(111)+chr(118)+chr(101),chr(121)+chr(111)+chr(117)
else:
    print "???"