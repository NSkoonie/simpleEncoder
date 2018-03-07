from tkinter import *

code = {"a" : "z",
        "b" : "y",
        "c" : "x",
        "d" : "w",
        "e" : "v",
        "f" : "u",
        "g" : "t",
        "h" : "s",
        "i" : "r",
        "j" : "q",
        "k" : "p",
        "l" : "o",
        "m" : "n",
        "n" : "m",
        "o" : "l",
        "p" : "k",
        "q" : "j",
        "r" : "i",
        "s" : "h",
        "t" : "g",
        "u" : "f",
        "v" : "e",
        "w" : "d",
        "x" : "c",
        "y" : "b",
        "z" : "a",
        "0" : "9",
        "1" : "8",
        "2" : "7",
        "3" : "6",
        "4" : "5",
        "5" : "4",
        "6" : "3",
        "7" : "2",
        "8" : "1",
        "9" : "0",}

w = Tk()
Label(w, text="NCODE").pack()
convertButton = Button(w, text="CONVERT")
textBox = Text(w)

def setText(text):
    textBox.delete(1.0, END)
    textBox.insert(END, text)

def convertText():
    textInput = textBox.get(1.0, END+"-1c").lower()
    convertedText = ""
    for char in textInput:
        try:
            convertedText = convertedText + code[char]
        except KeyError:
            convertedText = convertedText + char
    setText(convertedText)
    
convertButton["command"] = convertText
convertButton.pack()
textBox.pack()

w.mainloop()


