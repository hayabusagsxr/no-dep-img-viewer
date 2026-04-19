from tkinter import *
import tkinter.filedialog as fd

img_thing = None

def load_img():
    global img
    f = fd.askopenfilename()

    if f != "":
        try:
            img = PhotoImage(file=f)
            l.config(image=img)
            l.image = img
            print("loaded the file successfully")
        except:
            print("Error happened")

w = Tk()
w.geometry("700x500")
w.title("Image Viewer")

b = Button(w, text="Load Image", command=load_img)
b.pack(pady=20)

l = Label(w, text="Image goes here")
l.pack()

w.mainloop()