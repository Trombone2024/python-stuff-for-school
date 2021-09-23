from tkinter import*
obj=Tk()
obj.title('among sus')
obj.geometry('400x300')
wintext = Text(obj)
wintext.insert(INSERT, 'I made a gui with python and')
wintext.insert(END, ' this is pretty cool')
wintext.pack()
obj.mainloop()