from tkinter import *

class RootGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Visualización de datos")
        self.root.geometry("1000x1000")
        self.root.config(bg="black")

class ComGui():
    def __init__(self,root):
        self.root = root
        
        self.frame = LabelFrame(root, text = "Com Manger", 
                                padx = 5, pady=5, bg = "gray")
        
        self.label_com = Label(
            self.frame, text="Puertos: ", bg = "gray", width=15, anchor="w")
        self.label_bd = Label(
            self.frame, text="Baudios: ", bg = "gray", width=15, anchor="w")
        
        self.publish()

    def publish(self):
        self.frame.grid(row=0,column=0,rowspan=3,
                        columnspan=3,padx =5,pady=5)
        self.label_com.grid(column=1,row=2)
        self.label_bd.grid(column=1,row=3)

if __name__ == "__main__":
    RootGUI()
    ComGui()