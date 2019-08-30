from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

text = Text(frame)
text.pack()

B = Button(bottomframe, text ="Print", command = text.insert(INSERT, "Message"))
B.pack()
"""
def calc(input):
        a = '5+5'
        elements = list()
        for i in a : elements.append(i)
        try:
            if elements[1] == '+':
                result = int(elements[0]) + int(elements[2])
                print(result)
            if elements[1] == '-':
                result = int(elements[0]) - int(elements[2])
                print(result)
            if elements[1] == '*':
                result = int(elements[0]) * int(elements[2])
                print(result)
            if elements[1] == '/' and int(elements[2]) == 0:
                print("Alert! Zero division!")
            elif elements[1] == '/' and int(elements[2]) != 0:
                result = int(elements[0]) // int(elements[2])
                print(result)
        except:
            print('Something is wrong, try again!')

button_list = [
'C', '/', 'x', 'DEL',
'7', '8', '9', '+',
'4', '5', '6', '-',
'1', '2', '3', '='
]
button_list[0] # = clear input
button_list[1] # = /
button_list[2] # = *
button_list[3] # = # clear one character
button_list[4] = 7
button_list[5] = 8
button_list[6] = 9
button_list[7] # = +
button_list[8] = 4
button_list[9] = 5
button_list[10] = 6
button_list[11] # = -
button_list[12] = 1
button_list[13] = 2
button_list[14] = 3
button_list[15] # = enter
"""

root.mainloop()
