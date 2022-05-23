import tkinter as tk
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
        widget_width_multiplier = self.winfo_width()/self.winfo_height()
        
        self.Ltext1 = "Merhaba"
        self.Ltext2 = f"Benim adim  "

        self.startUI()
        
    def startUI(self):
        #----------- Main Frames -----------
        self.main_Lframe = ct.CTkFrame(self,width=380,height=580)
        self.main_Lframe.grid(row=0,column=0,rowspan=2,padx=10,pady=10)
        self.main_editLframe = ct.CTkFrame(self.main_Lframe,width=380,height=580)
        self.main_editLframe.grid(row=0,column=0)

        
        self.main_Rframe1 = ct.CTkFrame(self,width=380,height=285)
        self.main_Rframe1.grid(row=0,column=1)
        self.main_editRframe1 = ct.CTkFrame(self.main_Rframe1,width=380,height=285)
        self.main_editRframe1.grid(row=0,column=0,sticky="nsew")
        
        self.main_Rframe2 = ct.CTkFrame(self,width=380,height=285)
        self.main_Rframe2.grid(row=1,column=1)
        self.main_editRframe2 = ct.CTkFrame(self.main_Rframe2,width=380,height=285)
        self.main_editRframe2.grid(row=0,column=0,sticky="nsew")

        #----------- Labels ----------------
        
        self.Llabel1 = ct.CTkLabel(self.main_editLframe,text=self.Ltext1)
        self.Llabel1.grid(row=0,column=0)
        self.Llabel2 = ct.CTkLabel(self.main_editLframe,text=self.Ltext2)
        self.Llabel2.grid(row=1,column=0)

        
        

        #----------- Buttons ---------------

        self.R1button1 = ct.CTkButton(self.main_editRframe1,text="Click Me!",command=self.namechange)
        self.R1button1.grid()

        
        #----------- Entries -----------------
        
        self.entvar1 = tk.StringVar(self,value="")
        self.R2entry1 = ct.CTkEntry(self.main_editRframe2,textvariable=self.entvar1)
        self.R2entry1.grid()

    def namechange(self):
        return


if __name__ == "__main__":
    app = Window()
    app.mainloop()
