from tkinter import *

root = Tk()
root.title("clases")
root.geometry("900x600")

class CreateElements:
    def __init__(self):
        print("This is Create Elements Classes")
        
        
    def create_new_element(self):
        label=Label(root,text="A New Label has been created using class", fg="red")
        label.pack()
        btn=Button(root,text="Button",command=self.message)
        btn.pack(padx=20 , pady=10)
        
   
    def message(self):
        messagebox.showinfo("Show info" , "You clicked the button created using class")
        

obj_of_createelements=CreateElements()

btn=Button(root,text="Click to create label and button elements" , command=obj_of_createelements.create_new_element)
btn.pack(padx=20 , pady=10)

root.mainloop()
