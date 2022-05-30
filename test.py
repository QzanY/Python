import tkinter as tk
import customtkinter as ct
from tkinter import Tk, ttk, Button
from tkinter import messagebox
import numpy as np
from PIL import Image
import tkinter.font as font
# import cv2
from tkinter import filedialog as fd
import os
from math import sqrt
import matplotlib.pyplot as plt
import pandas as pd
from scipy import optimize
import xlwt
# import xlsxwriter
# import docx
# from docx import Document
# from docx.shared import Inches
# Some General Information

ct.set_appearance_mode("Dark")
ct.set_default_color_theme("blue")

# ----------------------------------------------------
window_for_Image = 'Image'
list_of_method = []
#selected_area_for_video = None
holding_function = None
month_cb = None



# Main Window Creating
# ----------------------------------------------------
main_root = ct.CTk()
screen_width = main_root.winfo_screenwidth()
screen_height = main_root.winfo_screenheight()
screen_width_constant = screen_width/1366
screen_height_constant = screen_height/768

# main_root.configure(background='')
main_root.geometry(str(int(screen_width_constant*1000))+'x'+str(int(screen_height_constant*600)))
main_root.resizable(False, False)
# main_root.wm_iconbitmap('codest_1.ico')
main_root.title('READER')
# ----------------------------------------------------

# Largening the interface by users resolution
# ----------------------------------------------------
def multiplier_for_x(x):
    global screen_width_constant
    return int(x * screen_width_constant)

def multiplier_for_y(y):
    global screen_height_constant
    return int(y * screen_height_constant)
# ----------------------------------------------------


# Separator Arranging
# -------------------------------------------------------------------
separator_horizontal = ttk.Separator(main_root, orient='horizontal')
separator_horizontal.place(x=0, y=multiplier_for_y(50), relwidth=1)
separator_vertical = ttk.Separator(main_root, orient='vertical')
separator_vertical.place(x=multiplier_for_x(300), y=0, relheight=multiplier_for_y(1))
# -------------------------------------------------------------------


# History Tree
# ----------------------------------------------------------------------
text = tk.Text(main_root, bg='#1f1f1f', borderwidth=4, highlightthickness=5,fg="white")
text.place(x=multiplier_for_x(20), y=multiplier_for_y(310), height=multiplier_for_y(280), width=multiplier_for_x(260))
label_for_text = ct.CTkLabel(main_root, text='        History')
label_for_text.place(x=multiplier_for_x(25), y=multiplier_for_y(280), height=multiplier_for_y(25), width=multiplier_for_x(200))
# ----------------------------------------------------------------------


# Creating table
# ---------------------------------------
style = ttk.Style()

style.theme_use('clam')
style.map('Treeview',
          background=[('selected', 'blue')]
          )
tv_for_data = ttk.Treeview(main_root)
vsb = ttk.Scrollbar(main_root, orient="vertical", command=tv_for_data.yview)
vsb.place(x=multiplier_for_x(975), y=multiplier_for_y(330), height=multiplier_for_y(210))
tv_for_data.configure(yscrollcommand=vsb.set)
tv_for_data.column('#0', width=multiplier_for_x(120), minwidth=25)
tv_for_data.heading('#0', text='Index', anchor='w')
style.configure('Treeview',
                foreground='black',
                rowheight=multiplier_for_y(25),
                fieldbackground="#1f1f1f"
        
                )
tv_for_data.place(x=multiplier_for_x(310), y=multiplier_for_y(310), height=multiplier_for_y(280), width=multiplier_for_x(680))
# -------------------------------------------------


# Creating Image Area
# -------------------------------------------------
# photo_for_graph = Image.open(r'C:/Users/ozany/OneDrive/Masaüstü/Python/Reader/johnxina.jpg')
# photo_for_graph = photo_for_graph.resize((multiplier_for_x(320), multiplier_for_y(240)))
# photo_for_graph = ImageTk.PhotoImage(photo_for_graph)
# file_path_graph = tk.Label(main_root, bg='', image=photo_for_graph).place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(670), y=multiplier_for_y(65))
# *************************************************************
# photo_for_img = Image.open(r'C:/Users/ozany/OneDrive/Masaüstü/Python/Reader/johnxina.jpg')
# photo_for_img = photo_for_img.resize((multiplier_for_x(320), multiplier_for_y(240)))
# photo_for_img = ImageTk.PhotoImage(photo_for_img)
# file_path_img = tk.Label(main_root, bg='', image=photo_for_img).place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(310), y=multiplier_for_y(65))

# -------------------------------------------------


# Button and Method Creating
# -------------------------------------------------------------------
myFont = font.Font(size=multiplier_for_x(10))


# Importing Button
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def Import_file():
    global main_root
    global img_main
    global photo_for_img
    global cap
    global file_path_img
    global text
    global file_path_of_image
    global img
    global Label_for_width, Label_for_height
    try:
        file_path_of_image = fd.askopenfilename(initialdir=os.getcwd(), title="Select file")
        split_file_path = file_path_of_image.split('/')
        type_of = split_file_path[-1].split('.')[-1]
        if type_of == 'png' or type_of == 'jpg' or type_of == 'jpeg' or type_of == 'JPEG' or type_of == 'jfif' or type_of == 'JPG':
            img_main = cv2.imread(r""+file_path_of_image, 1)
            img = cv2.cvtColor(img_main, cv2.COLOR_BGR2RGB)
            Label_for_height = tk.Label(main_root, text='Height of Image (in pixels): ' + str(img.shape[0]), bg='',
                                        anchor='w')
            Label_for_width = tk.Label(main_root, text='Width of Image (in pixels): ' + str(img.shape[1]), bg='',
                                        anchor='w')
            Label_for_width.place(y=multiplier_for_y(60), x=multiplier_for_x(26), width=multiplier_for_x(150), height=multiplier_for_y(20))
            Label_for_height.place(y=multiplier_for_y(85), x=multiplier_for_x(26), width=multiplier_for_x(150), height=multiplier_for_y(20))
            photo_for_img = Image.fromarray(img)
            photo_for_img = photo_for_img.resize((multiplier_for_x(320), multiplier_for_y(240)))
            photo_for_img = ImageTk.PhotoImage(photo_for_img)
            file_path_img = tk.Label(main_root, bg='', image=photo_for_img).place(height=multiplier_for_y(240), width=multiplier_for_x(320),
                                                                                            x=multiplier_for_x(310),
                                                                                            y=multiplier_for_y(65))
            text.insert('1.0', '* Image selected\n')
        elif type_of == 'MOV' or type_of == 'MP4' or type_of == 'AVI' or type_of == 'WMV' or type_of == 'MKV' or type_of == 'mp4':
            cap = cv2.VideoCapture(file_path_of_image)
            tf, frame = cap.read()
            photo_for_img = Image.fromarray(frame)
            photo_for_img = photo_for_img.resize((multiplier_for_x(320), multiplier_for_y(240)))
            photo_for_img = ImageTk.PhotoImage(photo_for_img)
            file_path_img = tk.Label(main_root, bg='', image=photo_for_img).place(height=multiplier_for_y(240), width=multiplier_for_x(320),
                                                                                            x=multiplier_for_x(310),
                                                                                            y=multiplier_for_y(65))

        else:
            text.insert('1.0', '* Image or Video not selected\n')
    except:
        text.insert('1.0', '* Image was not selected\n')


button_for_import = ct.CTkButton(main_root, text='Import', command=Import_file)
button_for_import.place(height=multiplier_for_y(46), width=multiplier_for_x(70), x=multiplier_for_x(4), y=multiplier_for_y(2))


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


# Exporting Button
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def exporting_excel(database, path):
    global month_cb
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()
    if holding_function == 'CR_3D_ID' or holding_function =='RR_3D_ID':
        worksheet.set_column('B:I', 12)
        merge_format = workbook.add_format({'bold': 1,'border': 1,'align': 'center','valign': 'vcenter'})
        worksheet.merge_range('B1:C1', 'CIE1931(2D)', merge_format)
        worksheet.merge_range('D1:F1', 'CIE1931(3D)', merge_format)
        worksheet.merge_range('G1:I1', 'RGB', merge_format)
        worksheet.write("A2", "Index")
        worksheet.write("B2", "X Values")
        worksheet.write("C2", "Y Values")
        worksheet.write("D2", "X Values")
        worksheet.write("E2", "Y Values")
        worksheet.write("F2", "Z Values")
        worksheet.write("G2", "Red Scale")
        worksheet.write("H2", "Green Scale")
        worksheet.write("I2", "Blue Scale")
        for tupl in database:  # data yı aktarma ve yerine göre yazma
            for p in range(len(database)):
                for n in range(len(tupl)):
                    worksheet.write(p+2, n, database[p][n])
        chart = workbook.add_chart({'type': 'scatter'})  # grafik ayarları
        if month_cb is not None:
            ord = int(month_cb.get())  # order of trendline
            if ord > 6:
                ord = 6
            chart.add_series({  # datayı grafiğe dökme
            'categories': 'Sheet1!$B$3:$B$' + str(len(database) + 2),
            'values': '=Sheet1!$C$3:$C$' + str(len(database) + 2),
            'name': 'Codest',
            'trendline': {  # trendline
                'type': 'polynomial',
                'name': 'Bestline',
                'order': ord,
                'forward': 0.001,
                'backward': 0.001,
                'display_equation': True,
                'line': {'color': 'red', 'width': 2}}})
        else:
            chart.add_series({  # datayı grafiğe dökme
            'categories': 'Sheet1!$B$3:$B$' + str(len(database) + 2),
            'values': '=Sheet1!$C$3:$C$' + str(len(database) + 2),
            'name': 'Codest'})
        # axis isimler, ve grafik ismi
        chart.set_x_axis({'name': 'CIE1931X', 'name_font': {'size': 10, 'bold': True}, 'num_font': {'italic': True}, })
        chart.set_y_axis({'name': 'CIE1931Y', 'name_font': {'size': 10, 'bold': True}, 'num_font': {'italic': True}, })
        chart.set_title({"name": " Results of Analysis"})
        worksheet.insert_chart('I10', chart)
        month_cb = None
    elif holding_function =='CR_ID' or  holding_function == 'RR_ID' or  holding_function =='RTR_ID' or  holding_function =='AAI_ID':
        worksheet.write("A1", "X Values")
        worksheet.write("B1", "Y Values")
        for value in range(len(database)):  # data yı aktarma ve yerine göre yazma
            worksheet.write(value + 1, 0, database[value][0])
            worksheet.write(value + 1, 1, database[value][1])
        if month_cb is not None:
            chart = workbook.add_chart({'type': 'scatter'})
            ord = int(month_cb.get())  # order of trendline
            if ord > 6:
                ord = 6
            chart.add_series({  # datayı grafiğe dökme
            'categories': 'Sheet1!$A$2:$A$' + str(len(database) + 1),
            'values': '=Sheet1!$B$2:$B$' + str(len(database) + 1),
            'name': 'Codest',
            'trendline': {  # trendline
                'type': 'polynomial',
                'name': 'Bestline',
                'order': ord,
                'forward': 0.001,
                'backward': 0.001,
                'display_equation': True,
                'line': {'color': 'red', 'width': 2}}})
        else:
            chart = workbook.add_chart({'type': 'scatter', 'subtype': 'straight'})
            chart.add_series({  # datayı grafiğe dökme
            'categories': 'Sheet1!$A$2:$A$' + str(len(database) + 1),
            'values': '=Sheet1!$B$2:$B$' + str(len(database) + 1),
            'name': 'Codest'})
        # axis isimler, ve grafik ismi
        chart.set_x_axis({'name': 'Direction', 'name_font': {'size': 10, 'bold': True}, 'num_font': {'italic': True}, })
        chart.set_y_axis({'name': 'Average', 'name_font': {'size': 10, 'bold': True}, 'num_font': {'italic': True}, })
        chart.set_title({"name": " Results of Analysis"})
        worksheet.insert_chart('G9', chart)
        month_cb = None
    elif holding_function == 'PA_ID':
        worksheet.write("A1", "Index")
        worksheet.write("B1", "Center X")
        worksheet.write("C1", "Center Y")
        worksheet.write("D1", "Radius")
        worksheet.write("E1", "Area")
        worksheet.write("F1", "Average Density")
        for tupl in database:  # data yı aktarma ve yerine göre yazma
            for p in range(len(database)):
                for n in range(len(tupl)):
                    worksheet.write(p+1, n, database[p][n])
        chart = workbook.add_chart({'type': 'scatter'})
        if month_cb is not None:
            ord = int(month_cb.get())  # order of trendline
            if ord > 6:
                ord = 6
            chart.add_series({  # datayı grafiğe dökme
            'categories': 'Sheet1!$E$2:$E$' + str(len(database) + 1),
            'values': '=Sheet1!$F$2:$F$' + str(len(database) + 1),
            'name': 'Codest',
            'trendline': {  # trendline
                'type': 'polynomial',
                'name': 'Bestline',
                'order': ord,
                'forward': 0.001,
                'backward': 0.001,
                'display_equation': True,
                'line': {'color': 'red', 'width': 2}}})
        else:
            chart.add_series({  # datayı grafiğe dökme
            'categories': 'Sheet1!$E$2:$E$' + str(len(database) + 1),
            'values': '=Sheet1!$F$2:$F$' + str(len(database) + 1),
            'name': 'Codest'})
        # axis isimler, ve grafik ismi
        chart.set_x_axis({'name': 'Direction', 'name_font': {'size': 10, 'bold': True}, 'num_font': {'italic': True}, })
        chart.set_y_axis({'name': 'Average', 'name_font': {'size': 10, 'bold': True}, 'num_font': {'italic': True}, })
        chart.set_title({"name": " Results of Analysis"})
        worksheet.insert_chart('G9', chart)
        month_cb = None
    workbook.close()


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


def exporting_word(database,path):
    global file_path_of_image

    mydoc = Document()

    mydoc.add_heading("READER ANALYSIS RESULTS", 0)  ### grafiği foto olarak tabloya ekleme
    mydoc.add_paragraph("\n\n\n")
    mydoc.add_paragraph("Imported Photograph\t\t\t\t    Graph of Analysis")

    paragraph = mydoc.add_paragraph()
    run = paragraph.add_run()
    run.add_picture(r""+file_path_of_image, width=Inches(3.0), height=Inches(3.0))

    run_2 = paragraph.add_run()
    run_2.add_picture('deleted.png', width=Inches(3.0), height=Inches(3.0))

    mydoc.add_page_break()
    mydoc.add_heading("Results of Analysis", 0)
    n=1
    if holding_function == 'CR_ID' or holding_function =='RR_ID' or holding_function =='RTR_ID' or  holding_function =='AAI_ID':
        datatable = mydoc.add_table(rows=len(database) + 1, cols=len(database[0]))  # tablo özellikleri
        datatable.style = "TableGrid"
        hdr_cells = datatable.rows[0].cells
        hdr_cells[0].text = "Index"
        hdr_cells[1].text = "Average"
        for x, y in database:
            cell = datatable.rows[n].cells
            cell[0].text = str(x)
            cell[1].text = str(y)
            n = n + 1
    elif holding_function == 'CR_3D_ID' or holding_function =='RR_3D_ID':
        datatable = mydoc.add_table(rows=len(database) + 1, cols=len(database[0]))  # tablo özellikleri
        datatable.style = "TableGrid"
        hdr_cells = datatable.rows[0].cells
        hdr_cells[0].text = "Index"
        hdr_cells[1].text = "CIE1931(2D) X Values"
        hdr_cells[2].text = "CIE1931(2D)Y Values"
        hdr_cells[3].text = "CIE1931(3D)X Values"
        hdr_cells[4].text = "CIE1931(3D)Y Values"
        hdr_cells[5].text = "CIE1931(3D)Z Values"
        hdr_cells[6].text = "Red Scale"
        hdr_cells[7].text = "Green Scale"
        hdr_cells[8].text = "Blue Scale"
        for i, x, y, x1, y1, z1, r, g, b in database:
            if n <= len(database):
                cell = datatable.rows[n].cells
                cell[0].text = str(i)
                cell[1].text = str(x)
                cell[2].text = str(y)
                cell[3].text = str(x1)
                cell[4].text = str(y1)
                cell[5].text = str(z1)
                cell[6].text = str(r)
                cell[7].text = str(g)
                cell[8].text = str(b)
                n = n + 1
    elif holding_function == 'PA_ID':
        datatable = mydoc.add_table(rows=len(database) + 1, cols=len(database[0]))  # tablo özellikleri
        datatable.style = "TableGrid"
        hdr_cells = datatable.rows[0].cells
        hdr_cells[0].text = "Index"
        hdr_cells[1].text = "Center X"
        hdr_cells[2].text = "Center Y"
        hdr_cells[3].text = "Radius"
        hdr_cells[4].text = "Area"
        hdr_cells[5].text = "Average Density"
        for i, x, y, r, a, d in database:
            if n <= len(database):
                cell = datatable.rows[n].cells
                cell[0].text = str(i)
                cell[1].text = str(x)
                cell[2].text = str(y)
                cell[3].text = str(r)
                cell[4].text = str(a)
                cell[5].text = str(d)
                n = n + 1
    mydoc.save(path)


def Export_data():
    global i
    global main_root
    global file_path_for_exporting
    global dataset
    global value_for_export
    global entry_for_export
    global dataset_1
    global list_allex
    global constant_for_excel,constant_for_word
    try:
        file_path_for_exporting = fd.askdirectory()
        value_for_export = entry_for_export.get()
        if (list_allex is not None) and (file_path_for_exporting != ''):
            if constant_for_excel.get()==1:
                path = file_path_for_exporting +'/'+ value_for_export+".xlsx"
                exporting_excel(list_allex, path)
                text.insert('1.0', '* File saved\n')
            if constant_for_word.get()==1:
                path = file_path_for_exporting +'/'+ value_for_export+".docx"
                exporting_word(list_allex, path)
                text.insert('1.0', '* File saved\n')

    except:
        text.insert('1.0', '* Exporting Error\n')


def export_button():
    global main_root
    global value
    global export_mid_button
    global list_of_method
    global entry_for_export
    global value_for_export
    global constant_for_word,constant_for_excel
    # cleaning method on interface if it exists
    if len(list_of_method) == 0:
        pass
    else:
        for item in list_of_method:
            item.place_forget()
        list_of_method = []
    value_for_export = tk.string()
    entry_for_export = ttk.Entry(main_root)  # textvariable=value_for_export
    entry_for_export.place(height=multiplier_for_y(20), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(140))
    label_for_export = tk.Label(main_root, text='Name of File:', bg='', fg='black', font='Helvetica 10')
    label_for_export.place(x=multiplier_for_x(11), y=multiplier_for_y(115), height=multiplier_for_y(25), width=multiplier_for_x(100))
    list_of_method.append(entry_for_export)
    list_of_method.append(label_for_export)
    export_mid_button = tk.Button(main_root, text='Export', bg='gray70', fg='black', command=Export_data)
    export_mid_button.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(225))
    list_of_method.append(export_mid_button)
    constant_for_word = tk.IntVar()
    Check_box_for_word = tk.Checkbutton(main_root,text="Word",variable=constant_for_word,onvalue=1,offvalue=0,bg="",anchor=tk.W)
    Check_box_for_word.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(170))
    constant_for_excel = tk.IntVar()
    Check_box_for_excel = tk.Checkbutton(main_root,text="Excel",variable=constant_for_excel,onvalue=1,offvalue=0,bg="",anchor=tk.W)
    Check_box_for_excel.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(190))
    list_of_method.append(Check_box_for_excel)
    list_of_method.append(Check_box_for_word)
button_for_export = ct.CTkButton(main_root, text='Export', command=export_button)
button_for_export.place(height=multiplier_for_y(46), width=multiplier_for_x(70), x=multiplier_for_x(79), y=multiplier_for_y(2))


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


# Clean Button
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def Clean_data():
    global blank_for_clear
    global file_path_graph
    global file_path_img
    global list_of_method
    global img_main
    global dataset
    img_main = None
    for item in tv_for_data.get_children():
        tv_for_data.delete(item)
    blank_for_clear = Image.new("RGB", (320, 240), (0, 0, 0))
    blank_for_clear = ImageTk.PhotoImage(blank_for_clear)
    file_path_graph = tk.Label(main_root, bg='', image=blank_for_clear).place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(670),
                                                                                        y=multiplier_for_y(65))
    file_path_img = tk.Label(main_root, bg='', image=blank_for_clear).place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(310),
                                                                                      y=multiplier_for_y(65))
    dataset = None
    if len(list_of_method) == 0:
        pass
    else:
        for item in list_of_method:
            item.place_forget()
        list_of_method = []


button_for_clean = ct.CTkButton(main_root, text='Clean All', command=Clean_data)
button_for_clean.place(height=multiplier_for_y(46), width=multiplier_for_x(70), x=multiplier_for_x(152), y=multiplier_for_y(2))


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


# Resize Button
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def resize_image():
    global img_main
    global value_for_height, entry_for_height, entry_for_width, value_for_width
    global text
    global Label_for_width,Label_for_height
    try:
        img_main = cv2.resize(img_main, (int(entry_for_width.get()), int(entry_for_height.get())), cv2.INTER_AREA)
        text.insert('1.0', '* Image resized\n')
        Label_for_height.config(text="Height of Image: "+str(img_main.shape[0]))
        Label_for_width.config(text="Width of Image: "+str(img_main.shape[1]))
        Label_for_height.update()
        Label_for_width.update()
    except:
        text.insert('1.0', '* Image not found\n')


def Resize_data():
    global list_of_method
    global img_main
    global main_root
    global list_of_method
    global value_for_height, entry_for_height, entry_for_width, value_for_width
    if len(list_of_method) == 0:
        pass
    else:
        for item in list_of_method:
            item.place_forget()
        list_of_method = []
    label_for_height = ct.CTkLabel(main_root, text='Height', fg='black')
    label_for_height.place(height=multiplier_for_y(20), width=multiplier_for_x(150), x=multiplier_for_x(25), y=multiplier_for_y(110))
    value_for_height = tk.IntVar()
    entry_for_height = ct.CTkEntry(main_root, textvariable=value_for_height)
    entry_for_height.place(height=multiplier_for_y(25), width=multiplier_for_x(150), x=multiplier_for_x(25), y=multiplier_for_y(130))
    label_for_width = ct.CTkLabel(main_root, text='Width', bg='', fg='black')
    label_for_width.place(height=multiplier_for_y(20), width=multiplier_for_x(150), x=multiplier_for_x(25), y=multiplier_for_y(160))
    value_for_width = tk.IntVar()
    entry_for_width = ct.CTkEntry(main_root, textvariable=value_for_width)
    entry_for_width.place(height=multiplier_for_y(25), width=multiplier_for_x(150), x=multiplier_for_x(25), y=multiplier_for_y(180))
    resize_button = ct.CTkButton(main_root, text='Resize', bg='gray70', fg='black', command=resize_image)
    resize_button.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(225))
    list_of_method.append(entry_for_height)
    list_of_method.append(entry_for_width)
    list_of_method.append(resize_button)
    list_of_method.append(label_for_height)
    list_of_method.append(label_for_width)


button_for_resize = ct.CTkButton(main_root, text='Resize', command=Resize_data)
button_for_resize.place(height=multiplier_for_y(46), width=multiplier_for_x(70), x=multiplier_for_x(225), y=multiplier_for_y(2))


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


# Circle Reading Method
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# Circle Reading Operation Function
# **********************************


# Mouse Event of circle reading
def clickevent_for_CR(event, x, y, flag, param):
    global img_main
    global list_of_click
    global list_of_move
    global diameter
    global img_template
    global window_for_Image
    # getting image from main
    img_template = np.copy(img_main)
    # selection point
    if event == cv2.EVENT_LBUTTONDOWN and flag == cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_FLAG_LBUTTON and len(
            list_of_click) == 0:
        list_of_click.append((x, y))
    elif event == cv2.EVENT_LBUTTONDOWN and flag == cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_FLAG_LBUTTON and len(
            list_of_click) > 0:
        list_of_click.append((x, y))
    # visualizing selection area
    elif event == cv2.EVENT_MOUSEMOVE and flag == cv2.EVENT_FLAG_CTRLKEY and len(list_of_click) == 1:
        img_backup = np.copy(img_template)
        radius = int(sqrt((x - list_of_click[0][0]) ** 2 + (y - list_of_click[0][1]) ** 2))
        diameter = radius
        cv2.circle(img_template, list_of_click[0], radius, (0, 0, 0), 1)
        cv2.imshow(window_for_Image, img_template)
        img_template = img_backup
    # Cleaning selection
    elif event == cv2.EVENT_RBUTTONDOWN:
        list_of_click = []
        list_of_move = []
        img_template = np.copy(img_main)
        cv2.imshow(window_for_Image, img_template)


# Operation blocks of circle reading
def CR_function():
    global list_of_move
    global list_of_click
    global window_for_Image
    global cutted_img
    global diameter
    global img_main
    global photo_for_graph
    global dataset
    global file_path_graph
    global entry_for_circle
    global holding_function
    global average_list
    global dataset_1
    global list_allex

    holding_function = "CR_ID"
    # Deleting Data from table on interface
    for item in tv_for_data.get_children():
        tv_for_data.delete(item)
    # Operation blocks
    try:
        img_template_local = np.copy(img_main)
        cv2.arrowedLine(img_template_local, (20, 20), (20, 50), (0, 0, 0), 2)
        cv2.putText(img_template_local, '30 Pixels', (40, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 1)
        cv2.imshow(window_for_Image, img_template_local)
        list_of_click = []
        list_of_move = []
        diameter = 0
    except:
        text.insert('1.0','* image is not imported\n')
        return None
    while True:
        cv2.setMouseCallback(window_for_Image, clickevent_for_CR)
        if cv2.waitKey(20) == ord('q') or len(list_of_click) == 2 or (cv2.getWindowProperty(window_for_Image, 0) == -1):
            break
    cv2.destroyWindow(window_for_Image)
    y_range_start = int(list_of_click[0][1] - diameter)
    y_range_finish = int(list_of_click[0][1] + diameter)
    x_range_start = int(list_of_click[0][0] - diameter)
    x_range_finish = int(list_of_click[0][0] + diameter)
    try:
        cutted_img = img_main[y_range_start:y_range_finish, x_range_start:x_range_finish]
        cutted_img_gray = cv2.cvtColor(cutted_img, cv2.COLOR_BGR2GRAY)
        step = int(entry_for_circle.get())
        average_list = []
        for step_of_loop in range(1, diameter, step):
            Blank = np.zeros((cutted_img_gray.shape[0], cutted_img_gray.shape[1]), dtype='uint8')
            cv2.circle(Blank, (cutted_img_gray.shape[1] // 2, cutted_img_gray.shape[0] // 2), step_of_loop,
                    (255, 255, 255),
                    -1)
            if len(average_list) == 0:
                average = cv2.mean(cutted_img_gray, mask=Blank)
                average_list.append(average[0])
            else:
                non = step_of_loop - step
                cv2.circle(Blank, (cutted_img_gray.shape[1] // 2, cutted_img_gray.shape[0] // 2), non, (0, 0, 0),
                        -1)
                average = cv2.mean(cutted_img_gray, mask=Blank)
                average_list.append(average[0])
    except:
        text.insert('1.0','* Circle exceed from frame or Distribution constant is not integer\n')
        return None


    # visualizing data
    plt.plot(average_list)
    plt.xlabel('Direction')
    plt.ylabel('Average')
    plt.savefig('deleted.png')
    plt.show()
    plt.close()
    photo_for_graph = Image.open(r'deleted.png')
    photo_for_graph = photo_for_graph.resize((multiplier_for_x(320), multiplier_for_y(240)), Image.ANTIALIAS)
    photo_for_graph = ImageTk.PhotoImage(photo_for_graph)
    file_path_graph = tk.Label(main_root, bg='', image=photo_for_graph)
    file_path_graph.place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(670), y=multiplier_for_y(65))
    dataset = pd.DataFrame(average_list)
    for item_1 in range(len(average_list)):
        tv_for_data.insert(parent='', index='end', iid=item_1, text=str(item_1), values=(average_list[item_1]))
    text.insert('1.0', '* Dataset created\n')
    index_number = [int(i) for i in range(len(dataset))]
    index_number = pd.DataFrame(index_number)
    dataset_1 = pd.concat([index_number, dataset], axis=1)
    list_allex = []
    for i in range(int(len(dataset_1))):
        list_allex.append([dataset_1.iloc[i,0], dataset_1.iloc[i,1]])


# *************************************************************************


# Clear data function
# *************************************************************************
def clear():
    # Cleaning data and graph from interface
    global tv_for_data
    global text
    global blank_for_clear
    global main_root
    global file_path_graph
    global dataset
    for item in tv_for_data.get_children():
        tv_for_data.delete(item)
    blank_for_clear = Image.new("RGB", (320, 240), (0, 0, 0))
    blank_for_clear = ImageTk.PhotoImage(blank_for_clear)
    file_path_graph = tk.Label(main_root, bg='', image=blank_for_clear).place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(670),
                                                                                        y=multiplier_for_y(65))
    dataset = None
    text.insert('1.0', '* Dataset has been deleted\n')


# *************************************************************************


# Circle Reading to interface
# *************************************************************************
def CR_methods():
    global main_root
    global value
    global list_of_method
    global entry_for_circle
    # cleaning method on interface if it exists
    if len(list_of_method) == 0:
        pass
    else:
        for item in list_of_method:
            item.place_forget()
        list_of_method = []
    for item in tv_for_data.get_children():
        tv_for_data.delete(item)
    # creating necessary widget
    value_for_circle = tk.IntVar()
    entry_for_circle = ttk.Entry(main_root, textvariable=value_for_circle)
    entry_for_circle.place(height=multiplier_for_y(20), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(140))
    label_for_entry = tk.Label(main_root, text='Distribution:', bg='', fg='black', font='Helvetica 10')
    label_for_entry.place(x=multiplier_for_x(11), y=multiplier_for_y(115), height=multiplier_for_y(25), width=multiplier_for_x(100))
    tv_for_data['columns'] = ['Average']
    tv_for_data.column('#0', width=multiplier_for_x(120), minwidth=25)
    tv_for_data.column('Average', anchor='w', width=multiplier_for_x(120))
    tv_for_data.heading('#0', text='Index', anchor='w')
    tv_for_data.heading('Average', text='Average', anchor='w')
    tv_for_data.place(x=multiplier_for_x(310), y=multiplier_for_y(310), height=multiplier_for_y(280), width=multiplier_for_x(680))
    Button_for_CR = tk.Button(main_root, text='Analysis', bg='gray70', fg='black', command=CR_function)
    Button_for_CR.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(180), y=multiplier_for_y(225))
    clear_button = tk.Button(main_root, text='Clear Data', bg='gray70', fg='black', command=clear)
    clear_button.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(225))
    list_of_method.append(clear_button)
    list_of_method.append(Button_for_CR)
    list_of_method.append(entry_for_circle)
    list_of_method.append(label_for_entry)


# ******************************************************************************************************

button_for_CR = ct.CTkButton(main_root, text='Circle\n Reading', command=CR_methods)
button_for_CR.place(height=multiplier_for_y(46), width=multiplier_for_x(92), x=multiplier_for_x(307), y=multiplier_for_y(2))

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


# Circle Reading 3-D method
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# mouse click function
# *************************************************************
def clickevent_for_CR_3D(event, x, y, flag, param):
    global img_main
    global list_of_click
    global list_of_move
    global diameter
    global img_template
    global window_for_Image
    # getting image from main
    img_template = np.copy(img_main)
    # Mouse event
    if event == cv2.EVENT_LBUTTONDOWN and flag == cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_FLAG_LBUTTON and len(
            list_of_click) == 0:
        list_of_click.append((x, y))
    elif event == cv2.EVENT_LBUTTONDOWN and flag == cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_FLAG_LBUTTON and len(
            list_of_click) > 0:
        list_of_click.append((x, y))
    elif event == cv2.EVENT_MOUSEMOVE and flag == cv2.EVENT_FLAG_CTRLKEY and len(list_of_click) == 1:
        img_backup = np.copy(img_template)
        radius = int(sqrt((x - list_of_click[0][0]) ** 2 + (y - list_of_click[0][1]) ** 2))
        diameter = radius
        cv2.circle(img_template, list_of_click[0], radius, (0, 0, 0), 1)
        cv2.imshow(window_for_Image, img_template)
        img_template = img_backup
    elif event == cv2.EVENT_RBUTTONDOWN:
        list_of_click = []
        list_of_move = []
        img_template = np.copy(img_main)
        cv2.imshow(window_for_Image, img_template)


# **********************************************************************


# Circle Reading 3D function
def CR_3D_function():
    for item in tv_for_data.get_children():
        tv_for_data.delete(item)
    global list_of_move
    global list_of_click
    global window_for_Image
    global cutted_img
    global diameter
    global img_main
    global photo_for_graph
    global dataset
    global file_path_graph
    global entry_for_circle_3D
    global holding_function
    global plot_list
    global plot_list_rgb
    global dataset_1
    global list_allex

    holding_function = "CR_3D_ID"
    try:
        # getting image from main
        img_template_local = np.copy(img_main)
        cv2.arrowedLine(img_template_local, (20, 20), (20, 50), (0, 0, 0), 2)
        cv2.putText(img_template_local, '30 Pixels', (40, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 1)
        cv2.imshow(window_for_Image, img_template_local)
        list_of_click = []
        list_of_move = []
        diameter = 0
    except:
        text.insert('1.0','* image is not imported\n')
        return None
    while True:
        cv2.setMouseCallback(window_for_Image, clickevent_for_CR_3D)
        if cv2.waitKey(20) == ord('q') or len(list_of_click) == 2 or (cv2.getWindowProperty(window_for_Image, 0) == -1):
            break
    cv2.destroyWindow(window_for_Image)
    y_range_start = int(list_of_click[0][1] - diameter)
    y_range_finish = int(list_of_click[0][1] + diameter)
    x_range_start = int(list_of_click[0][0] - diameter)
    x_range_finish = int(list_of_click[0][0] + diameter)
    try:
        cutted_img = img_main[y_range_start:y_range_finish, x_range_start:x_range_finish]
        step = int(entry_for_circle_3D.get())
        average_list = []
        for step_of_loop in range(1, diameter, step):
            Blank = np.zeros((cutted_img.shape[0], cutted_img.shape[1]), dtype='uint8')
            cv2.circle(Blank, (cutted_img.shape[1] // 2, cutted_img.shape[0] // 2), step_of_loop,
                        (255, 255, 255),
                        -1)
            if len(average_list) == 0:
                average = cv2.mean(cutted_img, mask=Blank)
                average_list.append(average)
            else:
                non = step_of_loop - step
                cv2.circle(Blank, (cutted_img.shape[1] // 2, cutted_img.shape[0] // 2), non, (0, 0, 0),
                            -1)
                average = cv2.mean(cutted_img, mask=Blank)
                average_list.append(average)
        list_all = []
        list_allex = []
        list_RGB = []
        list_CIExyz = []
        list_CIExy = []
        plot_list = [[], []]
        plot_list_rgb = []
        Indexg = 0
        for item in average_list:
            values = BGR_to_xy(item[0], item[1], item[2])
            list_all.append(values)
            list_RGB.append(values[2])
            list_CIExyz.append(values[1])
            list_CIExy.append(values[0])
            plot_list[0].append(values[0][0])
            plot_list[1].append(values[0][1])
            plot_list_rgb.append([values[2][2] / 255.0, values[2][1] / 255.0, values[2][0] / 255.0])
            list_allex.append([Indexg]+list(values[0])+list(values[1])+list(values[2]))
            Indexg = Indexg +1

    except:
        text.insert('1.0','* Distribution is not integer or Circle exceed from frame\n')
        return None
        # EREN veriler burda
    dataset = pd.DataFrame(list_all, columns=['CIE1931xy', 'CIE1931xyz', 'RGB'])
    plt.scatter(plot_list[0], plot_list[1], c=plot_list_rgb)
    plt.xlabel('Direction')
    plt.ylabel('Average')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.savefig('deleted.png')
    plt.show()
    plt.close()
    photo_for_graph = Image.open(r'deleted.png')
    photo_for_graph = photo_for_graph.resize((multiplier_for_x(320), multiplier_for_y(240)), Image.ANTIALIAS)
    photo_for_graph = ImageTk.PhotoImage(photo_for_graph)
    file_path_graph = tk.Label(main_root, bg='', image=photo_for_graph)
    file_path_graph.place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(670), y=multiplier_for_y(65))
    for item_1 in range(len(average_list)):
        tv_for_data.insert(parent='', index='end', iid=item_1, text=str(item_1),
                            values=(list_CIExy[item_1], list_CIExyz[item_1], list_RGB[item_1]))
    text.insert('1.0', '* Dataset created\n')

    plot_liste_1 = pd.DataFrame(plot_list[0], columns=["x"])
    plot_liste_2 = pd.DataFrame(plot_list[1], columns=["y"])
    dataset_1 = pd.concat([plot_liste_1, plot_liste_2], axis=1)



def BGR_to_xy(B, G, R):
    global text
    X = 0.4124 * R + 0.3576 * G + 0.1805 * B
    Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
    Z = 0.0193 * R + 0.1192 * G + 0.9505 * B
    x = X / (X + Y + Z)
    y = Y / (X + Y + Z)
    value_return = [(x, y), (X, Y, Z), (R, G, B)]
    return value_return


def CR_3D_methods():
    global main_root
    global value
    global list_of_method
    global entry_for_circle_3D
    # Cleaning Interface
    if len(list_of_method) == 0:
        pass
    else:
        for item in list_of_method:
            item.place_forget()
        list_of_method = []
    for item in tv_for_data.get_children():
        tv_for_data.delete(item)

    value_for_circle_3D = tk.IntVar()
    entry_for_circle_3D = ttk.Entry(main_root, textvariable=value_for_circle_3D)
    entry_for_circle_3D.place(height=multiplier_for_y(20), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(140))
    label_for_entry = tk.Label(main_root, text='Distribution:', bg='', fg='black', font='Helvetica 10')
    label_for_entry.place(x=multiplier_for_x(11), y=multiplier_for_y(115), height=multiplier_for_y(25), width=multiplier_for_x(100))
    tv_for_data['columns'] = ['CIE1931xy', 'CIE1931xyz', 'RGB']
    tv_for_data.column('#0', width=multiplier_for_x(120), minwidth=25)
    tv_for_data.column('CIE1931xy', anchor='w', width=multiplier_for_x(120))
    tv_for_data.column('CIE1931xyz', anchor='w', width=multiplier_for_x(120))
    tv_for_data.column('RGB', anchor='w', width=multiplier_for_x(120))
    tv_for_data.heading('#0', text='Index', anchor='w')
    tv_for_data.heading('CIE1931xy', text='CIE1931xy', anchor='w')
    tv_for_data.heading('CIE1931xyz', text='CIE1931xyz', anchor='w')
    tv_for_data.heading('RGB', text='RGB', anchor='w')
    tv_for_data.place(x=multiplier_for_x(310), y=multiplier_for_y(310), height=multiplier_for_y(280), width=multiplier_for_x(680))
    Button_for_3D_CR = tk.Button(main_root, text='Analysis', bg='gray70', fg='black', command=CR_3D_function)
    Button_for_3D_CR.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(180), y=multiplier_for_y(225))
    clear_button = tk.Button(main_root, text='Clear Data', bg='gray70', fg='black', command=clear)
    clear_button.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(225))
    list_of_method.append(clear_button)
    list_of_method.append(Button_for_3D_CR)
    list_of_method.append(entry_for_circle_3D)
    list_of_method.append(label_for_entry)


button_for_3D_CR = ct.CTkButton(main_root, text='Circle \n3D Reading',
                             command=CR_3D_methods)
button_for_3D_CR.place(height=multiplier_for_y(46), width=multiplier_for_x(92), x=multiplier_for_x(406), y=multiplier_for_y(2))


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


# Rectangle Reading method
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# Click events
# ************************************************************************
def clickarrow_for_RR(event, x, y, flag, param):
    global img_main
    global img_template
    global direction
    if event == cv2.EVENT_LBUTTONDOWN:
        B = img_template[y, x, 0]
        G = img_template[y, x, 1]
        R = img_template[y, x, 2]
        if B == 0 and G == 255 and R == 0:
            direction = 'UP'
        elif B == 255 and G == 0 and R == 0:
            direction = 'RIGHT'
        else:
            pass


def clickevent_for_RR(event, x, y, flag, param):
    global img_main
    global img_template
    global cutted_area
    global list_of_click
    global list_of_move
    global window_for_Image
    if event == cv2.EVENT_MOUSEMOVE and flag == cv2.EVENT_FLAG_CTRLKEY:
        if len(list_of_click) == 1:
            img_backup = np.copy(img_template)
            cv2.rectangle(img_template, list_of_click[0], (x, y), (0, 0, 0), 1)
            cv2.imshow(window_for_Image, img_template)
            img_template = img_backup
        elif len(list_of_click) == 0 or len(list_of_click) == 2:
            pass
    elif event == cv2.EVENT_LBUTTONDOWN and flag == (cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_LBUTTONDOWN):
        if len(list_of_click) < 2:
            list_of_click.append((x, y))
            cv2.circle(img_template, (x, y), 2, (0, 0, 0), -1)
            cv2.imshow(window_for_Image, img_template)
        if len(list_of_click) == 2:
            x_min = min(list_of_click[0][0],list_of_click[1][0])
            x_max = max(list_of_click[0][0],list_of_click[1][0])
            y_min = min(list_of_click[0][1],list_of_click[1][1])
            y_max = max(list_of_click[0][1],list_of_click[1][1])
            cutted_area = img_main[y_min:y_max, x_min:x_max]
            cv2.imshow(window_for_Image, img_template)
    elif event == cv2.EVENT_RBUTTONDOWN:
        img_template = np.copy(img_main)
        list_of_click = []
        list_of_move = []
        cv2.imshow(window_for_Image, img_template)


def RR_function():
    global file_path
    global window_for_Image
    global list_of_click
    global list_of_move
    global img_main
    global img_template
    global direction
    global dataset
    global cutted_area
    global file_path_graph
    global tv_for_data
    global main_root
    global photo_for_graph
    global holding_function
    global average
    global dataset_1
    global list_allex
    holding_function = "RR_ID"
    direction = None
    for item in tv_for_data.get_children():
        tv_for_data.delete(item)
    try:
        img_template = np.copy(img_main)
        cv2.imshow(window_for_Image, img_template)
        list_of_click = []
        list_of_move = []
        # main loop
        while True:

            cv2.setMouseCallback(window_for_Image, clickevent_for_RR)
            if cv2.waitKey(10) == ord('q') or len(list_of_click) == 2 or (cv2.getWindowProperty(window_for_Image, 0) == -1):
                break
        cv2.arrowedLine(img_template, (30, 70), (30, 30), (0, 255, 0), 6)
        cv2.arrowedLine(img_template, (30, 70), (70, 70), (255, 0, 0), 6)
        while True:
            cv2.imshow(window_for_Image, img_template)
            cv2.setMouseCallback(window_for_Image, clickarrow_for_RR)
            if cv2.waitKey(20) == ord('q') or direction is not None or (cv2.getWindowProperty(window_for_Image, 0) == -1):
                break
    except:
        text.insert('1.0', '* Image is not selected\n')

    if direction == 'UP':
        cutted_area = cv2.cvtColor(cutted_area, cv2.COLOR_BGR2GRAY)
        average = np.mean(cutted_area, axis=1)
        dataset = pd.DataFrame(average)
        plt.plot(average)
        plt.xlabel('Direction')
        plt.ylabel('Average')
        plt.savefig('deleted.png')
        plt.show()
        plt.close()
        photo_for_graph = Image.open(r'deleted.png')
        photo_for_graph = photo_for_graph.resize((multiplier_for_x(320), multiplier_for_y(240)), Image.ANTIALIAS)
        photo_for_graph = ImageTk.PhotoImage(photo_for_graph)
        file_path_graph = tk.Label(main_root, bg='', image=photo_for_graph)
        file_path_graph.place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(670), y=multiplier_for_y(65))
        for item_1 in range(average.shape[0]):
            tv_for_data.insert(parent='', index='end', iid=item_1, text=str(item_1), values=(average[item_1]))
        text.insert('1.0', '* Data set created\n')

        index_number = [int(i) for i in range(len(average))]
        index_number = pd.DataFrame(index_number)
        average_1 = pd.DataFrame(average)
        dataset_1 = pd.concat([index_number, average_1], axis=1)
        dataset_1 = dataset_1.fillna(dataset_1.mean())
        list_allex = []
        for i in range(int(len(dataset_1))):
            list_allex.append([dataset_1.iloc[i,0], dataset_1.iloc[i,1]])

    elif direction == 'RIGHT':
        cutted_area = cv2.cvtColor(cutted_area, cv2.COLOR_BGR2GRAY)
        average = np.mean(cutted_area, axis=0)
        # EREN veriler burda
        dataset = pd.DataFrame(average)
        plt.plot(average)
        plt.xlabel('Direction')
        plt.ylabel('Average')
        plt.savefig('deleted.png')
        plt.show()
        plt.close()
        photo_for_graph = Image.open(r'deleted.png')
        photo_for_graph = photo_for_graph.resize((multiplier_for_x(320), multiplier_for_y(240)), Image.ANTIALIAS)
        photo_for_graph = ImageTk.PhotoImage(photo_for_graph)
        file_path_graph = tk.Label(main_root, bg='', image=photo_for_graph)
        file_path_graph.place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(670), y=multiplier_for_y(65))
        for item_1 in range(average.shape[0]):
            tv_for_data.insert(parent='', index='end', iid=item_1, text=str(item_1), values=(average[item_1]))
        text.insert('1.0', '* Data set created\n')

        index_number = [int(i) for i in range(len(average))]
        index_number = pd.DataFrame(index_number)
        average_1 = pd.DataFrame(average)
        dataset_1 = pd.concat([index_number, average_1], axis=1)
        dataset_1 = dataset_1.fillna(dataset_1.mean())
        list_allex = []
        for i in range(int(len(dataset_1))):
            list_allex.append([dataset_1.iloc[i,0], dataset_1.iloc[i,1]])

    else:
        text.insert('1.0', '* No selected direction\n')
    cv2.destroyAllWindows()



def RR_methods():
    global main_root
    global value
    global list_of_method
    if len(list_of_method) == 0:
        pass
    else:
        for item in list_of_method:
            item.place_forget()
        list_of_method = []
    for item in tv_for_data.get_children():
        tv_for_data.delete(item)
    tv_for_data['columns'] = ['Average']
    tv_for_data.column('#0', width=multiplier_for_x(120), minwidth=25)
    tv_for_data.column('Average', anchor='w', width=multiplier_for_x(120))
    tv_for_data.heading('#0', text='Index', anchor='w')
    tv_for_data.heading('Average', text='Average', anchor='w')
    tv_for_data.place(x=multiplier_for_x(310), y=multiplier_for_y(310), height=multiplier_for_y(280), width=multiplier_for_x(680))
    clear_button = tk.Button(main_root, text='Clear Data', bg='gray70', fg='black', command=clear)
    clear_button.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(225))
    Button_for_RR = tk.Button(main_root, text='Analysis', bg='gray70', fg='black', command=RR_function)
    Button_for_RR.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(180), y=multiplier_for_y(225))
    list_of_method.append(clear_button)
    list_of_method.append(Button_for_RR)


button_for_CR = ct.CTkButton(main_root, text='Rectangle\n Reading', 
                          command=RR_methods)
button_for_CR.place(height=multiplier_for_y(46), width=multiplier_for_x(92), x=multiplier_for_x(505), y=multiplier_for_y(2))


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


# Rectangle Reading 3D method
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def clickarrow_for_RR_3D(event, x, y, flag, param):
    global img_main
    global img_template
    global direction
    if event == cv2.EVENT_LBUTTONDOWN:
        B = img_template[y, x, 0]
        G = img_template[y, x, 1]
        R = img_template[y, x, 2]
        if B == 0 and G == 255 and R == 0:
            direction = 'UP'
        elif B == 255 and G == 0 and R == 0:
            direction = 'RIGHT'
        else:
            pass


def clickevent_for_RR_3D(event, x, y, flag, param):
    global img_main
    global img_template
    global cutted_area
    global list_of_click
    global list_of_move
    global window_for_Image
    if event == cv2.EVENT_MOUSEMOVE and flag == cv2.EVENT_FLAG_CTRLKEY:
        if len(list_of_click) == 1:
            img_backup = np.copy(img_template)
            cv2.rectangle(img_template, list_of_click[0], (x, y), (0, 0, 0), 1)
            cv2.imshow(window_for_Image, img_template)
            img_template = img_backup
        elif len(list_of_click) == 0 or len(list_of_click) == 2:
            pass
    elif event == cv2.EVENT_LBUTTONDOWN and flag == (cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_LBUTTONDOWN):
        if len(list_of_click) < 2:
            list_of_click.append((x, y))
            cv2.circle(img_template, (x, y), 2, (0, 0, 0), -1)
            cv2.imshow(window_for_Image, img_template)
        if len(list_of_click) == 2:
            x_min = min(list_of_click[0][0],list_of_click[1][0])
            x_max = max(list_of_click[0][0],list_of_click[1][0])
            y_min = min(list_of_click[0][1],list_of_click[1][1])
            y_max = max(list_of_click[0][1],list_of_click[1][1])
            cutted_area = img_main[y_min:y_max, x_min:x_max]
            cv2.rectangle(img_template, list_of_click[0], list_of_click[1], (0, 0, 0), 1)
            cv2.imshow(window_for_Image, img_template)
    elif event == cv2.EVENT_RBUTTONDOWN:
        img_template = np.copy(img_main)
        list_of_click = []
        list_of_move = []
        cv2.imshow(window_for_Image, img_template)


def RR_3D_function():
    global file_path
    global window_for_Image
    global list_of_click
    global list_of_move
    global img_main
    global img_template
    global direction
    global dataset
    global cutted_area
    global file_path_graph
    global tv_for_data
    global main_root
    global photo_for_graph
    global holding_function
    global plot_liste
    global plot_liste_rgb
    global dataset_1
    global list_allex

    holding_function = "RR_3D_ID"

    for item in tv_for_data.get_children():
        tv_for_data.delete(item)
    direction = None
    try:
        img_template = np.copy(img_main)
        cv2.imshow(window_for_Image, img_template)
        list_of_click = []
        list_of_move = []
        # main loop
        while True:

            cv2.setMouseCallback(window_for_Image, clickevent_for_RR_3D)
            if cv2.waitKey(10) == ord('q') or len(list_of_click) == 2 or (cv2.getWindowProperty(window_for_Image, 0) == -1):
                break
        cv2.arrowedLine(img_template, (30, 70), (30, 30), (0, 255, 0), 6)
        cv2.arrowedLine(img_template, (30, 70), (70, 70), (255, 0, 0), 6)
        while True:
            cv2.imshow(window_for_Image, img_template)
            cv2.setMouseCallback(window_for_Image, clickarrow_for_RR_3D)
            if cv2.waitKey(20) == ord('q') or direction is not None or (cv2.getWindowProperty(window_for_Image, 0) == -1):
                break
    except:
        text.insert('1.0', '* Image is not selected\n')
        return None

    if direction == 'UP':
        average = np.mean(cutted_area, axis=1)
        liste_all = []
        list_allex = []
        liste_RGB = []
        liste_CIExyz = []
        liste_CIExy = []
        plot_liste = [[], []]
        plot_liste_rgb = []
        Indexg= 0
        for item in average:
            values = BGR_to_xy(item[0], item[1], item[2])
            list_allex.append([Indexg]+list(values[0])+list(values[1])+list(values[2]))
            liste_all.append(values)
            liste_RGB.append(values[2])
            liste_CIExyz.append(values[1])
            liste_CIExy.append(values[0])
            plot_liste[0].append(values[0][0])
            plot_liste[1].append(values[0][1])
            plot_liste_rgb.append([values[2][0] / 255.0, values[2][1] / 255.0, values[2][2] / 255.0])
            Indexg= Indexg+1
            # EREN veriler burda
        dataset = pd.DataFrame(liste_all, columns=['CIE1931xy', 'CIE1931xyz', 'RGB'])
        plt.scatter(plot_liste[0], plot_liste[1], c=plot_liste_rgb)
        plt.xlabel('Direction')
        plt.ylabel('Average')
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.savefig('deleted.png')
        plt.show()
        plt.close()
        photo_for_graph = Image.open(r'deleted.png')
        photo_for_graph = photo_for_graph.resize((multiplier_for_x(320), multiplier_for_y(240)), Image.ANTIALIAS)
        photo_for_graph = ImageTk.PhotoImage(photo_for_graph)
        file_path_graph = tk.Label(main_root, bg='', image=photo_for_graph)
        file_path_graph.place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(670), y=multiplier_for_y(65))
        for item_1 in range(average.shape[0]):
            tv_for_data.insert(parent='', index='end', iid=item_1, text=str(item_1),
                               values=(liste_CIExy[item_1], liste_CIExyz[item_1], liste_RGB[item_1]))
        text.insert('1.0', '* Data set created\n')
    elif direction == 'RIGHT':
        average = np.mean(cutted_area, axis=0)
        liste_all = []
        list_allex = []
        liste_RGB = []
        liste_CIExyz = []
        liste_CIExy = []
        plot_liste = [[], []]
        plot_liste_rgb = []
        Indexg=0
        for item in average:
            values = BGR_to_xy(item[0], item[1], item[2])
            liste_all.append(values)
            liste_RGB.append(values[2])
            liste_CIExyz.append(values[1])
            liste_CIExy.append(values[0])
            plot_liste[0].append(values[0][0])
            plot_liste[1].append(values[0][1])
            plot_liste_rgb.append([values[2][0] / 255.0, values[2][1] / 255.0, values[2][2] / 255.0])
            list_allex.append([Indexg]+list(values[0])+list(values[1])+list(values[2]))
            Indexg=Indexg+1
            # EREN veriler burda
        dataset = pd.DataFrame(liste_all, columns=['CIE1931xy', 'CIE1931xyz', 'RGB'])
        plt.scatter(plot_liste[0], plot_liste[1], c=plot_liste_rgb)
        plt.xlabel('Direction')
        plt.ylabel('Average')
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.savefig('deleted.png')
        plt.show()
        plt.close()
        photo_for_graph = Image.open(r'deleted.png')
        photo_for_graph = photo_for_graph.resize((multiplier_for_x(320), multiplier_for_y(240)), Image.ANTIALIAS)
        photo_for_graph = ImageTk.PhotoImage(photo_for_graph)
        file_path_graph = tk.Label(main_root, bg='', image=photo_for_graph)
        file_path_graph.place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(670), y=multiplier_for_y(65))
        for item_1 in range(average.shape[0]):
            tv_for_data.insert(parent='', index='end', iid=item_1, text=str(item_1),
                               values=(liste_CIExy[item_1], liste_CIExyz[item_1], liste_RGB[item_1]))
        text.insert('1.0', '* Data set created\n')

        plot_liste_1 = pd.DataFrame(plot_liste[0], columns=["x"])
        plot_liste_2 = pd.DataFrame(plot_liste[1], columns=["y"])
        dataset_1 = pd.concat([plot_liste_1, plot_liste_2], axis=1)

    else:
        text.insert('1.0', '* No selected direction\n')
    cv2.destroyAllWindows()


# widget to interface
# *********************************************************************************

def RR_3D_methods():
    global main_root
    global value
    global list_of_method
    if len(list_of_method) == 0:
        pass
    else:
        for item in list_of_method:
            item.place_forget()
        list_of_method = []
    for item in tv_for_data.get_children():
        tv_for_data.delete(item)
    tv_for_data['columns'] = ['CIE1931xy', 'CIE1931xyz', 'RGB']
    tv_for_data.column('#0', width=multiplier_for_x(120), minwidth=25)
    tv_for_data.column('CIE1931xy', anchor='w', width=multiplier_for_x(120))
    tv_for_data.column('CIE1931xyz', anchor='w', width=multiplier_for_x(120))
    tv_for_data.column('RGB', anchor='w', width=multiplier_for_x(120))
    tv_for_data.heading('#0', text='Index', anchor='w')
    tv_for_data.heading('CIE1931xy', text='CIE1931xy', anchor='w')
    tv_for_data.heading('CIE1931xyz', text='CIE1931xyz', anchor='w')
    tv_for_data.heading('RGB', text='RGB', anchor='w')
    tv_for_data.place(x=multiplier_for_x(310), y=multiplier_for_y(310), height=multiplier_for_y(280), width=multiplier_for_x(680))
    clear_button = tk.Button(main_root, text='Clear Data', bg='gray70', fg='black', command=clear)
    clear_button.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(225))
    Button_for_RR = tk.Button(main_root, text='Analysis', bg='gray70', fg='black', command=RR_3D_function)
    Button_for_RR.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(180), y=multiplier_for_y(225))
    list_of_method.append(clear_button)
    list_of_method.append(Button_for_RR)


button_for_CR = ct.CTkButton(main_root, text='Rectangle\n3D Reading', 
                          command=RR_3D_methods)
button_for_CR.place(height=multiplier_for_y(46), width=multiplier_for_x(92), x=multiplier_for_x(605), y=multiplier_for_y(2))


# **************************************************************************************************
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


# Image Average Analysis method
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

def AAI_function():
    global list_of_method
    global tv_for_dat
    global dataset
    global height_distribution_entry
    global width_distribution_entry
    global img_main
    global photo_for_graph
    global file_path_graph
    global img_template
    global holding_function
    global array
    global dataset_1
    global list_allex

    holding_function = "AAI_ID"

    for item in tv_for_data.get_children():
        tv_for_data.delete(item)
    try:
        height_distribution = int(height_distribution_entry.get())
        width_distribution = int(width_distribution_entry.get())
        if height_distribution < 5 or width_distribution < 5:
            result = tk.messagebox.askokcancel(title='Warning', message='Are you sure to continue? There is too much data. The operation may take a long time!!!')
            if result == True:
                pass
            else:
                return None
        img_template = np.copy(img_main)
        height_of_img = img_template.shape[0]
        width_of_img = img_template.shape[1]
        height_subtraction = (height_of_img % height_distribution)
        width_subtraction = (width_of_img % width_distribution)
        liste = []
        img_main_cutted = img_template[0:height_of_img + 1 - height_subtraction, 0:width_of_img + 1 - width_subtraction]
        for i in range(0, img_main_cutted.shape[0] - 1, height_distribution):
            for j in range(0, img_main_cutted.shape[1] - 1, width_distribution):
                part_of_img = img_main_cutted[i:i + height_distribution - 1, j:j + width_distribution - 1]
                cv2.rectangle(img_main_cutted, (j, i), (j + width_distribution - 1, i + height_distribution - 1),
                              (0, 0, 255), 1)
                average = round(cv2.mean(part_of_img)[0], 2)
                liste.append(average)
        cv2.imshow('Image', img_main_cutted)
        array = np.array(liste)
        plt.plot(array)
        plt.xlabel('Direction')
        plt.ylabel('Average')
        plt.savefig('deleted.png')
        plt.show()
        plt.close()
        photo_for_graph = Image.open(r'deleted.png')
        photo_for_graph = photo_for_graph.resize((multiplier_for_x(320), multiplier_for_y(240)), Image.ANTIALIAS)
        photo_for_graph = ImageTk.PhotoImage(photo_for_graph)
        file_path_graph = tk.Label(main_root, bg='', image=photo_for_graph)
        file_path_graph.place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(670), y=multiplier_for_y(65))
        for item_1 in range(array.shape[0]):
            tv_for_data.insert(parent='', index='end', iid=item_1, text=str(item_1), values=(array[item_1]))
            # EREN veriler burda
        dataset = pd.DataFrame(array)
        text.insert('1.0', '* Data set created\n')

        index_number = [int(i) for i in range(len(array))]
        index_number = pd.DataFrame(index_number)
        array_1 = pd.DataFrame(array)
        dataset_1 = pd.concat([index_number, array_1], axis=1)
        list_allex = []
        for i in range(int(len(dataset_1))):
            list_allex.append([dataset_1.iloc[i,0], dataset_1.iloc[i,1]])
    except:
        text.insert('1.0', '* Cannot be operated.\n')
    cv2.waitKey(2000)
    cv2.destroyAllWindows()


def IAA_methods():
    global main_root
    global value
    global list_of_method
    global height_distribution_entry, height, width, width_distribution_entry
    if len(list_of_method) == 0:
        pass
    else:
        for item in list_of_method:
            item.place_forget()
        list_of_method = []
    for item in tv_for_data.get_children():
        tv_for_data.delete(item)
    tv_for_data['columns'] = ['Average']
    tv_for_data.column('#0', width=multiplier_for_x(120), minwidth=25)
    tv_for_data.column('Average', anchor='w', width=multiplier_for_x(120))
    tv_for_data.heading('#0', text='Index', anchor='w')
    tv_for_data.heading('Average', text='Average', anchor='w')
    tv_for_data.place(x=multiplier_for_x(310), y=multiplier_for_y(310), height=multiplier_for_y(280), width=multiplier_for_x(680))
    clear_button = tk.Button(main_root, text='Clear Data', bg='gray70', fg='black', command=clear)
    clear_button.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(225))
    Button_for_RR = tk.Button(main_root, text='Analysis', bg='gray70', fg='black', command=AAI_function)
    Button_for_RR.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(180), y=multiplier_for_y(225))
    # 1-)
    height = tk.IntVar()
    height_distribution_entry = ttk.Entry(main_root, textvariable=height)
    height_distribution_entry.place(height=multiplier_for_y(20), width=multiplier_for_x(75), x=multiplier_for_x(25), y=multiplier_for_y(145))
    height_distribution_label = ttk.Label(main_root, text='Height Distribution:')
    height_distribution_label.configure(background='', foreground='black')
    height_distribution_label.place(height=multiplier_for_y(20), width=multiplier_for_x(150), x=multiplier_for_x(25), y=multiplier_for_y(120))
    # 2-)
    width = tk.IntVar()
    width_distribution_entry = ttk.Entry(main_root, textvariable=width)
    width_distribution_entry.place(height=multiplier_for_y(20), width=multiplier_for_x(75), x=multiplier_for_x(25), y=multiplier_for_y(195))
    width_distribution_label = ttk.Label(main_root, text='Width Distribution:')
    width_distribution_label.configure(background='', foreground='black')
    width_distribution_label.place(height=multiplier_for_y(20), width=multiplier_for_x(150), x=multiplier_for_x(25), y=multiplier_for_y(170))
    list_of_method.append(clear_button)
    list_of_method.append(Button_for_RR)
    list_of_method.append(width_distribution_entry)
    list_of_method.append(width_distribution_label)
    list_of_method.append(height_distribution_label)
    list_of_method.append(height_distribution_entry)


button_for_CR = ct.CTkButton(main_root, text='Average \nAnalysis', 
                          command=IAA_methods)
button_for_CR.place(height=multiplier_for_y(46), width=multiplier_for_x(92), x=multiplier_for_x(704), y=multiplier_for_y(2))


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


# Particle Analysis method
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# ----------------------------------------------------------
def click_event_for_param(event, x, y, flag, param):
    global img_main
    global img_template_1
    global list_of_param
    global window_for_Image
    if event == cv2.EVENT_LBUTTONDOWN and flag == (cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_FLAG_LBUTTON) and len(
            list_of_param) < 3:
        list_of_param.append((x, y))
    elif event == cv2.EVENT_MOUSEMOVE and flag == cv2.EVENT_FLAG_CTRLKEY and len(list_of_param) == 1:
        cv2.line(img_template_1, list_of_param[0], (x, y), (0, 0, 0), 2)
    cv2.imshow(window_for_Image, img_template_1)
    img_template_1 = np.copy(img_main)


def parametrize():
    try:
        global img_main
        global img_template_1
        global list_of_param
        global dataset
        global window_for_Image
        global tv_for_data
        global entry
        global value
        img_template_1 = np.copy(img_main)
        cv2.imshow(window_for_Image, img_template_1)
        list_of_param = []
        while True:
            if cv2.waitKey(20) == ord('q') or len(list_of_param) == 2:
                cv2.destroyAllWindows()
                break
            cv2.setMouseCallback(window_for_Image, click_event_for_param)
        ok_value = float(entry.get())
        distance = float(
            sqrt((list_of_param[0][0] - list_of_param[1][0]) ** 2 + (list_of_param[0][1] - list_of_param[1][1]) ** 2))
        param = ok_value / distance
        dataset['Area'] = dataset['Area'] * param
        dataset['Radius'] = dataset['Radius'] * param
        for item in tv_for_data.get_children():
            tv_for_data.delete(item)
        for item_1 in range(dataset['Radius'].shape[0]):
            tv_for_data.insert(parent='', index='end', iid=item_1, text=str(item_1),
                               values=(dataset['Center'][item_1], dataset['Radius'][item_1], dataset['Area'][item_1],
                                       dataset['Average Intensity'][item_1]))
        text.insert('1.0', '* Dataset was parametrized\n')
    except:
        text.insert('1.0', '* Dataset cannot be parametrized\n')


def nothing(x):
    pass


def creating_trackbar(windowname, trackname, start, finish, function):
    cv2.namedWindow(windowname)
    cv2.createTrackbar(trackname, windowname, start, finish, function)


def get_trackbar(windowname, trackname):
    return cv2.getTrackbarPos(trackname, windowname)


def create_blank_2D(height, width):
    return np.zeros((height, width), dtype='uint8')


def create_blank_3D(height, width):
    return np.zeros((height, width, 3), dtype='uint8')


def convert_to_numpy(array):
    return np.transpose(np.array(array))
breakout = None

def PA_function():
    try:
        for item in tv_for_data.get_children():
            tv_for_data.delete(item)
        global Trackbar_Window_1, Trackbar_name_1, Trackbar_Window_2, Trackbar_name_2, img_main, thresh_value_1, thresh_value_2, img_height, img_width, img_main_3D, img_template, img_template_3D
        global root
        global dataset
        global photo_for_graph, file_path_graph
        global holding_function
        global areas
        global average_gray
        global dataset_1
        global breakout
        global list_allex
        breakout = None
        holding_function = "PA_ID"
        def click_trackbar(event,x,y,flag,param):
            global breakout
            if event == cv2.EVENT_LBUTTONDOWN :
                breakout = 'break'
            elif event == cv2.EVENT_RBUTTONDOWN :
                breakout = 'quit'



        try:
            dataset = None
            # Reading image imported
            # ------------------------------------
            try:
                img_template = cv2.cvtColor(np.copy(img_main), cv2.COLOR_BGR2GRAY)
                img_template_3D = np.copy(img_main)
                img_height = img_template.shape[0]
                img_width = img_template.shape[1]
            except:
                text.insert('1.0', '* Image is not found\n')
            # ------------------------------------

            # Creating trackbar
            # ------------------------------------
            Trackbar_Window_1 = 'Trackbar-Window-1'
            Trackbar_name_1 = 'Trackbar-1'
            cv2.namedWindow(Trackbar_Window_1,cv2.WINDOW_NORMAL)
            cv2.resizeWindow(Trackbar_Window_1,img_height,img_width)
            creating_trackbar(Trackbar_Window_1, Trackbar_name_1, 0, 255, nothing)
            cv2.moveWindow(Trackbar_Window_1, 600, 300)
            Trackbar_Window_2 = 'Trackbar-Window-2'
            Trackbar_name_2 = 'Trackbar-2'
            cv2.namedWindow(Trackbar_Window_2,cv2.WINDOW_NORMAL)
            cv2.resizeWindow(Trackbar_Window_2,img_height,img_width)
            creating_trackbar(Trackbar_Window_2, Trackbar_name_2, 0, 255, nothing)
            cv2.moveWindow(Trackbar_Window_2, 400, 300)
        except:
            text.insert('1.0', '* Trackbar blocks cannot be created\n')
        # ------------------------------------

        # Method main loop
        # ------------------------------------
        while True:
            # get thresh value
            # ------------------------------------
            try:
                thresh_value_1 = get_trackbar(Trackbar_Window_1, Trackbar_name_1)
                thresh_value_2 = get_trackbar(Trackbar_Window_2, Trackbar_name_2)
            except:
                text.insert('1.0', '* Thresh value is not taken\n')
            TF_1, THRESH_1 = cv2.threshold(img_template, thresh_value_1, 255, cv2.THRESH_BINARY_INV)
            TF_2, THRESH_2 = cv2.threshold(img_template, thresh_value_2, 255, cv2.THRESH_BINARY_INV)
            # ------------------------------------

            # Creating blank
            # ------------------------------------
            Blank_1 = create_blank_3D(img_height, img_width)
            Blank_2 = create_blank_3D(img_height, img_width)
            Blank_1[:, :, 0] = THRESH_1[:, :]
            Blank_2[:, :, 1] = THRESH_2[:, :]
            # ----------------------------------------------------------------------------------

            # Filtering
            sample_1 = cv2.morphologyEx(Blank_1, cv2.MORPH_OPEN, (9, 9), iterations=1)
            sample_2 = cv2.morphologyEx(Blank_2, cv2.MORPH_OPEN, (9, 9), iterations=1)
            sample_1 = cv2.erode(sample_1, (7, 7))
            sample_2 = cv2.erode(sample_2, (7, 7))
            sample_1 = cv2.dilate(sample_1, (7, 7))
            sample_2 = cv2.dilate(sample_2, (7, 7))
            # ------------------------------------------------------------------------------

            # Thresh to Gray
            # ------------------------------------
            Thresh_1_gray = cv2.cvtColor(sample_1, cv2.COLOR_BGR2GRAY)
            Thresh_2_gray = cv2.cvtColor(sample_2, cv2.COLOR_BGR2GRAY)
            # ------------------------------------

            # Gray to Thresh
            # ------------------------------------
            TF_3, thresh_1 = cv2.threshold(Thresh_1_gray, 20, 255, cv2.THRESH_BINARY)
            TF_4, thresh_2 = cv2.threshold(Thresh_2_gray, 128, 255, cv2.THRESH_BINARY)
            cv2.imshow(Trackbar_Window_1, thresh_1)
            cv2.imshow(Trackbar_Window_2, thresh_2)

            # operation selection
            # ---------------------------------------------------------------
            cv2.setMouseCallback(Trackbar_Window_1, click_trackbar)
            cv2.setMouseCallback(Trackbar_Window_2, click_trackbar)
            if cv2.waitKey(50) == ord('o') or breakout == 'break':
                cv2.destroyWindow(Trackbar_Window_1)
                cv2.destroyWindow(Trackbar_Window_2)
                command = 'Operation'
                break
            if cv2.waitKey(50) == ord('q') or breakout == 'quit':
                command = 'Quit'
                cv2.destroyWindow(Trackbar_Window_1)
                cv2.destroyWindow(Trackbar_Window_2)
                break
            # --------------------------------------------------------------
        # End of selection and destroying
        # --------------------------------------------------------------------

        # ------------------------------------

        # Method main loop-2
        # ------------------------------------
        while command == 'Operation':
            # Combination of Threshes
            # ------------------------------------
            combined = cv2.bitwise_and(thresh_1, thresh_2)
            # ------------------------------------

            # Contour detection and drawing
            # ------------------------------------
            cnts, hier = cv2.findContours(combined, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(img_template_3D, cnts, -1, (0, 0, 255), -1)
            # ------------------------------------

            # operation selection
            # ------------------------------------
            if cv2.waitKey(50) == ord('q') or dataset is not None:
                cv2.destroyWindow('Image')
                break
            else:
                text.insert('1.0', '* Dataset is created\n')
                # Needed lists
                # ------------------------------------
                areas = []
                radiuses = []
                centers = []
                average_gray = []
                # ------------------------------------

                # Particle detection
                # ------------------------------------
                for cnt in cnts:
                    # Taking all data
                    # ------------------------------------
                    area = cv2.contourArea(cnt)
                    # ------------------------------------

                    # area elimination
                    # ------------------------------------
                    if area < int(entry_1.get()):
                        continue
                    (x, y), radius = cv2.minEnclosingCircle(cnt)
                    centers.append((int(x), int(y)))
                    areas.append(round(area, 6))
                    radiuses.append(round(radius, 4))
                    cv2.rectangle(img_template_3D, (int(x - radius), int(y - radius)),
                                  (int(x + radius), int(y + radius)),
                                  (0, 255, 0), 2)
                    particle = img_template[int(y - radius):int(y + radius), int(x - radius):int(x + radius)]
                    thresh_particle = combined[int(y - radius):int(y + radius), int(x - radius):int(x + radius)]
                    mean_gray = cv2.mean(particle, mask=thresh_particle)
                    average_gray.append(round(mean_gray[0], 4))
                # ------------------------------------

                # converting to dataset
                # ------------------------------------
                dataset = {'Center': centers,
                           'Radius': radiuses,
                           'Area': areas,
                           'Average Intensity': average_gray}
                # Eren buraya bakabilirsin
                plt.scatter(areas, average_gray)
                plt.xlabel('Area')
                plt.ylabel('Average')
                plt.savefig('deleted.png')
                plt.show()
                plt.close()
                photo_for_graph = Image.open(r'deleted.png')
                photo_for_graph = photo_for_graph.resize((multiplier_for_x(320), multiplier_for_y(240)), Image.ANTIALIAS)
                photo_for_graph = ImageTk.PhotoImage(photo_for_graph)
                file_path_graph = tk.Label(main_root, bg='', image=photo_for_graph)
                file_path_graph.place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(670), y=multiplier_for_y(65))
                # EREN veriler burda
                dataset = pd.DataFrame(dataset)
                for item_1 in range(len(radiuses)):
                    tv_for_data.insert(parent='', index='end', iid=item_1, text=str(item_1),
                                       values=(centers[item_1], radiuses[item_1], areas[item_1], average_gray[item_1]))
                break
        cv2.imshow('Image', img_template_3D)
            # ------------------------------------
        cv2.destroyAllWindows()
        areas_df = pd.DataFrame(areas, columns=["x"])
        average_gray_df = pd.DataFrame(average_gray, columns=["y"])
        dataset_1 = pd.concat([areas_df, average_gray_df], axis=1)
        list_allex = []
        for i in range(int(len(dataset))):
            list_allex.append([i]+[dataset.iloc[i, 0][0], dataset.iloc[i, 0][1], dataset.iloc[i, 1], dataset.iloc[i, 2],dataset.iloc[i, 3]])
    except:
        cv2.destroyAllWindows()
        text.insert('1.0', '* Operation Error\n')


def PA_methods():
    global main_root
    global value
    global list_of_method
    global entry_1, value_1
    global entry, value
    global height_distribution_entry, height, width, width_distribution_entry
    if len(list_of_method) == 0:
        pass
    else:
        for item in list_of_method:
            item.place_forget()
        list_of_method = []
    for item in tv_for_data.get_children():
        tv_for_data.delete(item)
    tv_for_data['columns'] = ['Center', 'Radius', 'Area', 'Average Density']
    tv_for_data.column('#0', width=multiplier_for_x(120), minwidth=20)
    tv_for_data.column('Center', anchor='w', width=multiplier_for_x(90))
    tv_for_data.column('Radius', anchor='w', width=multiplier_for_x(90))
    tv_for_data.column('Area', anchor='w', width=multiplier_for_x(90))
    tv_for_data.column('Average Density', anchor='w', width=multiplier_for_x(90))
    tv_for_data.heading('#0', text='Index', anchor='w')
    tv_for_data.heading('Center', text='Center', anchor='w')
    tv_for_data.heading('Radius', text='Radius', anchor='w')
    tv_for_data.heading('Area', text='Area', anchor='w')
    tv_for_data.heading('Average Density', text='Average Density', anchor='w')
    tv_for_data.place(x=multiplier_for_x(310), y=multiplier_for_y(310), height=multiplier_for_y(280), width=multiplier_for_x(680))
    clear_button = tk.Button(main_root, text='Clear Data', bg='gray70', fg='black', command=clear)
    clear_button.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(225))
    Button_for_PA = tk.Button(main_root, text='Analysis', bg='gray70', fg='black', command=PA_function)
    Button_for_PA.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(180), y=multiplier_for_y(225))
    value_1 = tk.IntVar()
    entry_1 = ttk.Entry(main_root, textvariable=value_1)
    entry_1.place(height=multiplier_for_y(20), width=multiplier_for_x(150), x=multiplier_for_x(25), y=multiplier_for_y(140))
    label_for_entry = tk.Label(main_root, text='Area Elimination:', bg='', fg='black', anchor='w')
    label_for_entry.place(height=multiplier_for_y(20), width=multiplier_for_x(150), x=multiplier_for_x(26), y=multiplier_for_y(110))
    value = tk.IntVar()
    entry = ttk.Entry(main_root, textvariable=value)
    entry.place(height=multiplier_for_y(25), width=multiplier_for_x(150), x=multiplier_for_x(140), y=multiplier_for_y(180))
    parametrize_button = tk.Button(main_root, text='Parametrize', bg='gray', fg='black', command=parametrize)
    parametrize_button.place(height=multiplier_for_y(25), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(180))
    list_of_method.append(clear_button)
    list_of_method.append(Button_for_PA)
    list_of_method.append(entry_1)
    list_of_method.append(entry)
    list_of_method.append(label_for_entry)
    list_of_method.append(parametrize_button)


button_for_PA = ct.CTkButton(main_root, text='Particle \nAnalysis', 
                          command=PA_methods)
button_for_PA.place(height=multiplier_for_y(46), width=multiplier_for_x(92), x=multiplier_for_x(803), y=multiplier_for_y(2))


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


# Real Time Reading Method
# ------------------------------------
def click_event_for_RTR(event, x, y, flag, param):
    global img_main
    global img_template
    global cutted_area
    global list_of_click
    global list_of_move
    global window_for_Image
    if event == cv2.EVENT_MOUSEMOVE and flag == cv2.EVENT_FLAG_CTRLKEY:
        if len(list_of_click) == 1:
            img_backup = np.copy(img_template)
            cv2.rectangle(img_template, list_of_click[0], (x, y), (0, 0, 0), 1)
            cv2.imshow(window_for_Image, img_template)
            img_template = img_backup
        elif len(list_of_click) == 0 or len(list_of_click) == 2:
            pass
    elif event == cv2.EVENT_LBUTTONDOWN and flag == (cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_LBUTTONDOWN):
        if len(list_of_click) < 2:
            list_of_click.append((x, y))
            cv2.circle(img_template, (x, y), 2, (0, 0, 0), -1)
            cv2.imshow(window_for_Image, img_template)
        if len(list_of_click) == 2:
            cutted_area = img_main[list_of_click[0][1]:list_of_click[1][1], list_of_click[0][0]:list_of_click[1][0]]
            cv2.rectangle(img_template, list_of_click[0], list_of_click[1], (0, 0, 0), 1)
            cv2.imshow(window_for_Image, img_template)
    elif event == cv2.EVENT_RBUTTONDOWN:
        img_template = np.copy(img_main)
        list_of_click = []
        list_of_move = []
        cv2.imshow(window_for_Image, img_template)


def RTR_function():
    global img_main
    global img_template
    global list_of_click
    global list_of_move
    global window_for_Image
    global cap
    global dataset
    global photo_for_graph
    global file_path_graph
    global holding_function
    global dataset
    global dataset_1
    global list_allex

    holding_function = 'RTR_ID'
    average_list = []
    list_of_click = []
    list_of_move = []
    try:
        TF, frame = cap.read()
    except:
        text.insert('1.0','* The video is not selected\n')
        return None
    img_main = np.copy(frame)
    img_template = np.copy(frame)
    cv2.imshow(window_for_Image, img_main)
    while True:
        cv2.setMouseCallback(window_for_Image, click_event_for_RTR)
        if cv2.waitKey(20) == ord('q') or len(list_of_click) == 2:
            cv2.destroyAllWindows()
            break
    starty = list_of_click[0][1]
    startx = list_of_click[0][0]
    finishy = list_of_click[1][1]
    finishx = list_of_click[1][0]
    while True:
        try:
            ort = cv2.cvtColor(frame[starty:finishy, startx:finishx], cv2.COLOR_BGR2GRAY)
            average = cv2.mean(ort)[0]
            average_list.append(average)
            TF, frame = cap.read()
        except:
            break
    dataset = pd.DataFrame(average_list)
    plt.plot(dataset)
    plt.xlabel('Area')
    plt.ylabel('Average')
    plt.savefig('deleted.png')
    plt.show()
    plt.close()
    photo_for_graph = Image.open(r'deleted.png')
    photo_for_graph = photo_for_graph.resize((multiplier_for_x(320), multiplier_for_y(240)), Image.ANTIALIAS)
    photo_for_graph = ImageTk.PhotoImage(photo_for_graph)
    file_path_graph = tk.Label(main_root, bg='', image=photo_for_graph)
    file_path_graph.place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(670), y=multiplier_for_y(65))
    # EREN veriler burda
    dataset = pd.DataFrame(average_list)

    for item_1 in range(len(average_list)):
        tv_for_data.insert(parent='', index='end', iid=item_1, text=str(item_1), values=(average_list[item_1]))
    text.insert('1.0', '* Dataset created\n')

    index_number = [int(i) for i in range(len(dataset))]
    index_number = pd.DataFrame(index_number)
    dataset_1 = pd.concat([index_number, dataset], axis=1)
    list_allex = []
    for i in range(int(len(dataset_1))):
        list_allex.append([dataset_1.iloc[i,0], dataset_1.iloc[i,1]])

def RTR_methods():
    global list_of_method
    global main_root
    if len(list_of_method) == 0:
        pass
    else:
        for item in list_of_method:
            item.place_forget()
        list_of_method = []
    for item in tv_for_data.get_children():
        tv_for_data.delete(item)
    tv_for_data['columns'] = ['Average']
    tv_for_data.column('#0', width=multiplier_for_x(120), minwidth=25)
    tv_for_data.column('Average', anchor='w', width=multiplier_for_x(120))
    tv_for_data.heading('#0', text='Index', anchor='w')
    tv_for_data.heading('Average', text='Average', anchor='w')
    tv_for_data.place(x=multiplier_for_x(310), y=multiplier_for_y(310), height=multiplier_for_y(280), width=multiplier_for_x(680))
    analysis_button = tk.Button(main_root, text='Analysis', bg='gray70', fg='black', command=RTR_function)
    analysis_button.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(225))
    list_of_method.append(analysis_button)


button_for_RTR = ct.CTkButton(main_root, text='Real Time \nReading', 
                           command=RTR_methods)
button_for_RTR.place(height=multiplier_for_y(46), width=multiplier_for_x(92), x=multiplier_for_x(902), y=multiplier_for_y(2))


# ------------------------------------

# Real Time Reading Method
# ------------------------------------

def trend_line(dataframe, color=None):
    global month_cb
    global dataframe_for_fitting
    global photo_for_graph
    model = 0
    try:
        if month_cb is not None:
            model = np.poly1d(np.polyfit(dataframe.iloc[:, 0], dataframe.iloc[:, 1], int(month_cb.get())))
            plt.figure(figsize=(6, 4))
            plt.scatter(dataframe.iloc[:, 0], dataframe.iloc[:, 1], c=color, linewidth=1)
            plt.plot(dataframe.iloc[:, 0], model(dataframe.iloc[:, 0]), label='Fitted function', color='red', linewidth=3)
            plt.xlabel('Direction')
            plt.ylabel('Average')
            plt.savefig('deleted.png')
            plt.show()
            plt.close()
            photo_for_graph = Image.open(r'deleted.png')
            photo_for_graph = photo_for_graph.resize((multiplier_for_x(320), multiplier_for_y(240)), Image.ANTIALIAS)
            photo_for_graph = ImageTk.PhotoImage(photo_for_graph)
            file_path_graph = tk.Label(main_root, bg='gray68', image=photo_for_graph)
            file_path_graph.place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(670), y=multiplier_for_y(65))
    except:
        text.insert('1.0',"* Too much data. Couldn't draw trend line\n")
        plt.scatter(dataframe.iloc[:, 0], dataframe.iloc[:, 1], c=color, linewidth=1)
        plt.xlabel('Direction')
        plt.ylabel('Average')
        plt.savefig('deleted.png')
        plt.show()
        plt.close()
        photo_for_graph = Image.open(r'deleted.png')
        photo_for_graph = photo_for_graph.resize((multiplier_for_x(320), multiplier_for_y(240)), Image.ANTIALIAS)
        photo_for_graph = ImageTk.PhotoImage(photo_for_graph)
        file_path_graph = tk.Label(main_root, bg='gray68', image=photo_for_graph)
        file_path_graph.place(height=multiplier_for_y(240), width=multiplier_for_x(320), x=multiplier_for_x(670), y=multiplier_for_y(65))
        return None



def ploto():
    # Furkan Code Here
    # Pls check whether dataset exists or not and plot data with dataset
    global dataset
    global average_list
    global average
    global photo_for_graph
    global file_path_graph
    global plot_liste
    global array
    global areas
    global average_gray
    global plot_liste_rgb
    global plot_list
    global plot_list_rgb
    global month_cb
    global dataset_1

    try:
        if holding_function == "CR_ID":
            index_number = [int(i) for i in range(len(dataset))]
            index_number = pd.DataFrame(index_number)
            dataset_1 = pd.concat([index_number, dataset], axis=1)

            trend_line(dataset_1)

        elif holding_function == "CR_3D_ID":
            plot_liste_1 = pd.DataFrame(plot_list[0], columns=["x"])
            plot_liste_2 = pd.DataFrame(plot_list[1], columns=["y"])
            dataset_1 = pd.concat([plot_liste_1, plot_liste_2], axis=1)
            data_copied = dataset_1.copy()
            dataset_1 = dataset_1.sort_values(by="x")

            trend_line(dataset_1, plot_list_rgb)

            dataset_1 = data_copied.copy()

        elif holding_function == "RR_ID":
            index_number = [int(i) for i in range(len(average))]
            index_number = pd.DataFrame(index_number)
            average_1 = pd.DataFrame(average)
            dataset_1 = pd.concat([index_number, average_1], axis=1)
            dataset_1 = dataset_1.fillna(dataset_1.mean())

            trend_line(dataset_1)

        elif holding_function == "RR_3D_ID":
            plot_liste_1 = pd.DataFrame(plot_liste[0], columns=["x"])
            plot_liste_2 = pd.DataFrame(plot_liste[1], columns=["y"])
            dataset_1 = pd.concat([plot_liste_1, plot_liste_2], axis=1)
            data_copied = dataset_1.copy()
            dataset_1 = dataset_1.sort_values(by="x")

            trend_line(dataset_1, plot_liste_rgb)

            dataset_1 = data_copied.copy()

        elif holding_function == "AAI_ID":
            index_number = [int(i) for i in range(len(array))]
            index_number = pd.DataFrame(index_number)
            array_1 = pd.DataFrame(array)
            dataset_1 = pd.concat([index_number, array_1], axis=1)

            trend_line(dataset_1)

        elif holding_function == "PA_ID":
            areas_df = pd.DataFrame(areas, columns=["x"])
            average_gray_df = pd.DataFrame(average_gray, columns=["y"])
            dataset_1 = pd.concat([areas_df, average_gray_df], axis=1)
            data_copied = dataset_1.copy()
            dataset_1 = dataset_1.sort_values(by="x")

            trend_line(dataset_1)

            dataset_1 = data_copied.copy()

        elif holding_function == 'RTR_ID':
            index_number = [int(i) for i in range(len(dataset))]
            index_number = pd.DataFrame(index_number)
            dataset_1 = pd.concat([index_number, dataset], axis=1)

            trend_line(dataset_1)
    except:
        text.insert('1.0',"Couldn't draw the trend line.")
        return None





months = ('1', '2', '3', '4', '5', '6',
          '7', '8', '9', '10')
selected_month = tk.StringVar()


def ploting_new():
    global months
    global clear_button
    global list_of_method
    global main_root
    global label_for_plot
    global month_cb
    if len(list_of_method) == 0:
        pass
    else:
        for item in list_of_method:
            item.place_forget()
        list_of_method = []
    month_cb = ttk.Combobox(main_root, textvariable=selected_month)
    month_cb['values'] = months
    month_cb['state'] = 'readonly'  # normal
    month_cb.place(x=multiplier_for_x(25), y=multiplier_for_y(150), width=multiplier_for_x(100), height=multiplier_for_y(20))
    clear_button = tk.Button(main_root, text='Clear Data', bg='gray70', fg='black', command=clear)
    clear_button.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(25), y=multiplier_for_y(225))
    label_for_plot = tk.Label(main_root, text='Plot Style:', bg='', fg='black', anchor='w')
    label_for_plot.place(height=multiplier_for_y(20), width=multiplier_for_x(150), x=multiplier_for_x(26), y=multiplier_for_y(125))
    analysis_button = tk.Button(main_root, text='plot', bg='gray70', fg='black', command=ploto)
    analysis_button.place(height=multiplier_for_y(30), width=multiplier_for_x(100), x=multiplier_for_x(175), y=multiplier_for_y(225))
    list_of_method.append(month_cb)
    list_of_method.append(clear_button)
    list_of_method.append(label_for_plot)
    list_of_method.append(analysis_button)


button_for_RTR = ct.CTkButton(main_root, text='Trend Line', 
                           command=ploting_new)
button_for_RTR.place(height=multiplier_for_y(46), width=multiplier_for_x(92), x=multiplier_for_x(896), y=multiplier_for_y(542))
# ------------------------------------

# Show plot again
# ------------------------------------
def plotting_again():
    global month_cb
    global holding_function
    global dataset_1
    global plot_list
    global plot_list_rgb
    global plot_liste
    global plot_liste_rgb

    try:

        if month_cb is not None:
            ploto()
        else:
            if holding_function=='CR_3D_ID':
                plt.scatter(plot_list[0], plot_list[1], c=plot_list_rgb)
                plt.xlabel('Direction')
                plt.ylabel('Average')
                plt.xlim([0, 1])
                plt.ylim([0, 1])
                plt.show()
                plt.close()
            elif holding_function=='RR_3D_ID':
                plt.scatter(plot_liste[0], plot_liste[1], c=plot_liste_rgb)
                plt.xlabel('Direction')
                plt.ylabel('Average')
                plt.xlim([0, 1])
                plt.ylim([0, 1])
                plt.show()
                plt.close()
            else:
                plt.plot(dataset_1.iloc[:,1])
                plt.xlabel('Direction')
                plt.ylabel('Average')
                plt.show()
                plt.close()
    except:
        text.insert('1.0','* No dataset\n')
        return None


button_for_RTR = ct.CTkButton(main_root, text='Analyze', 
                           command=plotting_again)
button_for_RTR.place(height=multiplier_for_y(46), width=multiplier_for_x(92), x=multiplier_for_x(796), y=multiplier_for_y(542))
# ------------------------------------

# -------------------------------------------------------------------


main_root.mainloop()