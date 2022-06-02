import tkinter as tk
from tkinter import DISABLED, messagebox,filedialog
import customtkinter as ct
from docx import Document
import pandas as pd


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
        
        self.startUI()
        
    def startUI(self):
        #----------- Main Frames -----------
        self.main_Lframe = ct.CTkFrame(self,width=380,height=580)
        self.main_Lframe.grid(row=0,column=0,rowspan=2,padx=10,pady=10)
        self.main_Lframe.grid_propagate(0)

        self.main_Lframe.rowconfigure(0,minsize=20)
        self.main_Lframe.rowconfigure(2,weight=1)
        self.main_Lframe.rowconfigure(4,weight=1)
        self.main_Lframe.columnconfigure(0,weight=1)
        self.main_Lframe.columnconfigure(2,weight=1)

        self.main_labelLframe = ct.CTkFrame(self.main_Lframe,width=300,height=100)
        self.main_labelLframe.grid_propagate(0)
        self.main_labelLframe.rowconfigure(1,minsize=10)
        self.main_labelLframe.rowconfigure(3,minsize=10)
        self.main_labelLframe.columnconfigure(0,weight=1)
        self.main_labelLframe.columnconfigure(2,weight=1)

        self.main_labelLframe.grid(row=1,column=1,sticky="nsew")


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
        # self.main_labelRframe2 = ct.CTkFrame(self.main_Rframe2,width=380,height=285)
        # self.main_labelRframe2.grid(row=0,column=0,sticky="nsew")

        #----------- Labels ----------------
        
        self.Llabel1 = ct.CTkLabel(self.main_labelLframe,text="Merhaba")
        self.Llabel1.grid(row=0,column=1,sticky="nsew")
        self.Llabel2 = ct.CTkLabel(self.main_labelLframe,text="İsminizi bahşeder misiniz?")
        self.Llabel2.grid(row=2,column=1)
        self.Llabel3 = ct.CTkLabel(self.main_labelLframe,text="hahahahaaahahah")
        self.Llabel3.grid(row=4,column=1)

        # self.R2documentlabel = ct.CTkLabel(self.main_Rframe2,text="")
        # self.R2documentlabel.grid()

        
        

        #----------- Buttons ---------------

        self.R1button1 = ct.CTkButton(self.main_Rframe1,text="Click Me!",command=self.namechange)
        self.R1button1.grid(row=1,column=1)

        self.Lbutton = ct.CTkButton(self.main_Lframe,text="Select document", command=self.select_document)
        self.Lbutton.grid(row=3,column=1)

        
        #----------- Entries -----------------
        
        self.entvar1 = tk.StringVar(self,value="")
        self.R2entry1 = ct.CTkEntry(self.main_Rframe1,textvariable=self.entvar1,width=150)
        self.R2entry1.grid(row=3,column=1)
        

    def namechange(self):
        if len(self.R2entry1.get()) > 20:
            messagebox.showerror("Long Name","The name you've written is too long to display. It's length must be 20 characters or less.")
        elif self.R2entry1.get() == "":
            self.Llabel2.config(text="İsminiz yok mu?")
        else:
            self.Llabel2.config(text=f"Benim adım {self.R2entry1.get()}")         # ÇOK ÖNEMLİ BİR ARAÇ

    def select_document(self):
        file = filedialog.askopenfilename(title="Select Your Document",initialdir="/home/bs2022/e2581163/Desktop")
        try:
            if file.split(".")[-1] == "docx":
                self.editor = tk.Text(self.main_Rframe2,bg="#3d3d3d",fg="white")
                self.editor.grid()
                doc = Document(file)
                text1 = doc.paragraphs[2].text
                self.editor.insert(tk.END,text1)
            elif file.split(".")[-1] == "xls":
                table = pd.read_excel(file)
                print(table)
        except AttributeError:
            pass




    


if __name__ == "__main__":
    app = Window()
    app.mainloop()
