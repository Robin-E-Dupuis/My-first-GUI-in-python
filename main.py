from tkinter import *

window = Tk()

photo = PhotoImage(file='img.png')

window.geometry("420x420")
window.title("My First GUI")
window.config(background="cyan")
label = Label(window, text="Hello from Louisiana!",
              font=('Arial', 15, 'underline'),
              background="turquoise", fg='blue',
              padx=20, pady=20,
              image=photo,
              compound='bottom')
label.pack()
window.mainloop()
