from tkinter import *

window = Tk()
window.title("Password Strength Checker App")
window.geometry('400x400')
lbl = Label(window, text="Enter password Ishaan")
lbl.pack()
lbl1=Label(window)

txtbox = Entry(window)
txtbox.pack()
def checkstrength():
    password = txtbox.get()
    lengthchecker = len(password)
    print(lengthchecker)
    if lengthchecker <= 5:
        lbl1.config(fg="red")
        lbl1["text"]= "Weak"
    if lengthchecker >= 6 and lengthchecker <=8:
        lbl1.config(fg="yellow")
        lbl1["text"]="Medium"
    if lengthchecker > 8 and lengthchecker <= 12:
        lbl1.config(fg="lightgreen")
        lbl1["text"]="Strong"
    if lengthchecker > 12:
        lbl1.config(fg="darkgreen")
        lbl1["text"]="Very Strong"




button = Button(window, text="Check Strength", command=checkstrength)
button.pack()
lbl1.pack()


window.mainloop()




