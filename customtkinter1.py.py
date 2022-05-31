import tkinter as tk
from tkinter import ttk
import customtkinter as ct

ct.set_appearance_mode("Dark")
ct.set_default_color_theme("blue")


class Window(ct.CTk):

    WIDTH = 800
    HEIGHT = 600
    
    def __init__(self):
        super().__init__()

        self.title("Voice Assistant")
        self.geometry(f"{Window.WIDTH}x{Window.HEIGHT}")
        # widget_width_multiplier = self.winfo_width()/self.winfo_height()
        
        self.Ltext1 = "Merhaba"
        self.name = "Ozan"
        self.Ltext2 = f"Benim adim {self.name}"

        self.startUI()
        
    def startUI(self):
        #----------- Main Frames -----------
        self.main_Lframe = ct.CTkFrame(self,width=380,height=580)
        self.main_Lframe.grid(row=0,column=0,rowspan=2,padx=10,pady=10)
        self.main_Lframe.grid_propagate(0)

        # self.main_editLframe = ct.CTkFrame(self.main_Lframe,width=380,height=580)
        # self.main_editLframe.grid(row=0,column=0,sticky="nsew")
        self.main_Lframe.rowconfigure(0,weight=1)
        self.main_Lframe.rowconfigure(4,weight=1)

        self.main_Lframe.columnconfigure(0,weight=1)
        self.main_Lframe.columnconfigure(2,weight=1)

        self.main_Rframe1 = ct.CTkFrame(self,width=380,height=285)
        self.main_Rframe1.grid(row=0,column=1)
        self.main_Rframe1.grid_propagate(0)
        

        self.main_Rframe1.rowconfigure(0,weight=1)
        self.main_Rframe1.rowconfigure(2,minsize=10)
        self.main_Rframe1.rowconfigure(4,weight=1)
        self.main_Rframe1.columnconfigure(0,weight=1)
        self.main_Rframe1.columnconfigure(2,weight=1)

        
        self.main_Rframe2 = ct.CTkFrame(self,width=380,height=285)
        self.main_Rframe2.grid(row=1,column=1)
        self.main_Rframe2.grid_propagate(0)
        self.main_editRframe2 = ct.CTkFrame(self.main_Rframe2,width=380,height=285)
        self.main_editRframe2.grid(row=0,column=0,sticky="nsew")

        #----------- Labels ----------------
        
        self.Llabel1 = ct.CTkLabel(self.main_Lframe,text=self.Ltext1)
        self.Llabel1.grid(row=1,column=1,sticky="nsew")
        self.Llabel2 = ct.CTkLabel(self.main_Lframe,text=self.Ltext2)
        self.Llabel2.grid(row=2,column=1)
        self.Llabel3 = ct.CTkLabel(self.main_Lframe,text="hahahahaaahahah")
        self.Llabel3.grid(row=3,column=1)

        
        

        #----------- Buttons ---------------

        self.R1button1 = ct.CTkButton(self.main_Rframe1,text="Click Me!",command=self.namechange)
        self.R1button1.grid(row=1,column=1)

        self.R1button2 = ct.CTkButton(self.main_Rframe1,text="Don't Click Me!",command=self.getname)
        self.R1button2.grid(row=3,column=1)

        
        #----------- Entries -----------------
        
        self.entvar1 = tk.StringVar(self,value="")
        self.R2entry1 = ct.CTkEntry(self.main_editRframe2,textvariable=self.entvar1,width=150)
        self.R2entry1.grid()

        #----------- Textbox ----------------

        self.R2textbox = tk.Text(self.main_Rframe2,bg="#3d3d3d",fg="white",font="Helvetica")
        self.R2textbox.grid(row=1,column=0)


    def namechange(self):
        self.name = self.R2entry1.get()
        self.Llabel2.destroy()
        self.Llabel2 = ct.CTkLabel(self.main_Lframe,text=f"Benim adim {self.name}")
        self.Llabel2.grid(row=2,column=1)
        # pass
    def getname(self):
        pass


if __name__ == "__main__":
    app = Window()
    app.mainloop()
