from tkinter import *
from PIL import ImageTk, Image

ilk_pencere = Tk()

yazi = Label(ilk_pencere, text="Welcome to Social Credit Test", font=("Arial",25), bg="red")
yazi.pack()

def oyun():
    ilk_pencere.destroy()
    soru1 = Tk()
    soru_1 = Label(soru1, text="Which country is the best?", font=("Arial",25), bg="red")
    soru1.geometry("400x200")

    def yanliscevap1():
        soru1.destroy()
        gg = Tk()
        eksi = ImageTk.PhotoImage(Image.open("eksisocial.jpg").resize([400,300]))
        eksii = Label(gg,image=eksi)
        eksii.pack()
        gg.mainloop()
    def ydevam1():
        pass
    def dogrucevap1():
        soru1.destroy()

        arti1 = Tk()
        arti = ImageTk.PhotoImage(Image.open("socill.gif").resize([400,300]))
        artii = Label(arti1,image=arti)
        artii.pack()
        def de():
            arti1.destroy()
            soru2 = Tk()
            soru_2 = Label(soru2, text="How many hours do you play\n video games in a week?", font=("Arial",25), bg="red")

            def yanliscevap2():
                soru2.destroy()
                gge = Tk()
                eksil = ImageTk.PhotoImage(Image.open("oyunbitti.jpg").resize([400,300]))
                eksiil = Label(gge,image=eksil)
                eksiil.pack()
                gge.mainloop()
            
            def dogrucevap2():
                soru2.destroy()
                arti2 = Tk()
                artid = ImageTk.PhotoImage(Image.open("socill.gif").resize([400,300]))
                artiid = Label(arti2,image=artid)
                artiid.pack()
                def fe():
                    arti2.destroy()
                    soru3 = Tk()
                    frame1 = LabelFrame(soru3,text="Is Taiwan a country?")
                    var=IntVar()
                    cevap3_1 = Radiobutton(frame1, text="Yes      ", variable=var, value=0)
                    cevap3_1.pack()
                    cevap3_2 = Radiobutton(frame1, text="Maybe", variable=var, value=1)
                    cevap3_2.pack()
                    cevap3_3 = Radiobutton(frame1, text="No      ", variable=var, value=2)
                    cevap3_3.pack()
                    frame1.grid(row=0,column=0,padx=10,pady=10)

                    frame2 = LabelFrame(soru3,text="What happened in\n 1989 Tiananmen Square????")
                    var2 = IntVar()
                    cevap3_11 = Radiobutton(frame2, text="Something", variable=var2, value=0)
                    cevap3_11.pack()
                    cevap3_22 = Radiobutton(frame2, text="Nothing", variable=var2, value=1)
                    cevap3_22.pack()
                    cevap3_33 = Radiobutton(frame2, text="I don't know", variable=var2, value=2)
                    cevap3_33.pack()
                    frame2.grid(row=0,column=2,padx=10,pady=10)

                    def submitbutt():
                        a = var.get()
                        b = var2.get()
                        if a ==2 and b==1:
                            soru3.destroy()
                            win = Tk()
                            win.title("Nice job!")
                            bitis = ImageTk.PhotoImage(Image.open("kazandi.jpg").resize([400,300]))
                            bitiss = Label(win,image=bitis)
                            bitiss.pack()
                            def ss():
                                win.destroy()
                                winn = Tk()
                                bitisd = ImageTk.PhotoImage(Image.open("johnxina.jpg").resize([400,300]))
                                bitissd = Label(winn,image=bitisd)
                                bitissd.pack()
                                Label(winn,text="JOHN XINA IS PROUD OF YOU",fg="red",bg="black",font=("Arial",20)).pack()
                                winn.mainloop()
                            Button(win,text="Continue",command=ss).pack()
                            win.mainloop()
                        else:
                            soru3.destroy()
                            lose = Tk()
                            bit = ImageTk.PhotoImage(Image.open("gg.jpg").resize([400,300]))
                            bitt = Label(lose,image=bit)
                            bitt.pack()
                            
                            lose.mainloop()

                    button31 = Button(soru3,text="Submit",command=submitbutt)
                    button31.grid(row=1,column=1)

                    soru3.mainloop()

                Button(arti2,text="Continue",command=fe).pack()
                arti2.mainloop()

            soru_2.grid(row=0,column=0,columnspan=2)
            cevap2_1 = Button(soru2,text="1",padx=41,pady=20,bg="pink",command=dogrucevap2)
            cevap2_1.grid(column=0,row=1)
            cevap2_2 = Button(soru2,text="69",padx=47,pady=20,bg="pink",command=yanliscevap2)
            cevap2_2.grid(column=1,row=1)
            cevap2_3 = Button(soru2,text="420",padx=35,pady=20,bg="pink",command=yanliscevap2)
            cevap2_3.grid(column=0,row=2)
            cevap2_4 = Button(soru2,text="1989",padx=41,pady=20,bg="pink",command=yanliscevap2)
            cevap2_4.grid(column=1,row=2)
            soru2.mainloop()
        Button(arti1,text="Continue",command=de).pack()
        arti1.mainloop()
    soru_1.grid(row=0,column=0,columnspan=2)
    cevap1_1 = Button(soru1,text="USA",padx=41,pady=20,bg="pink",command=yanliscevap1)
    cevap1_1.grid(column=0,row=1)
    cevap1_2 = Button(soru1,text="China",padx=47,pady=20,bg="pink",command=dogrucevap1)
    cevap1_2.grid(column=1,row=1)
    cevap1_3 = Button(soru1,text="North Korea",padx=20,pady=20,bg="pink",command=yanliscevap1)
    cevap1_3.grid(column=0,row=2)
    cevap1_4 = Button(soru1,text="England",padx=41,pady=20,bg="pink",command=yanliscevap1)
    cevap1_4.grid(column=1,row=2)

    soru1.mainloop()
bosluk1= Label(ilk_pencere , text=" ")
bosluk1.pack()

basla = Button(ilk_pencere, text="Start", pady=15, padx=20, bg="pink", command=oyun)
basla.pack()

ilk_pencere.mainloop()