import sys
from PySide6.QtGui import QFont,QPixmap,QAction,QIcon,QCursor,QMouseEvent
from PySide6.QtWidgets import QApplication, QLabel,QSlider,QMenu,QHeaderView,QTableWidget, QMainWindow,QSplitter ,QTabWidget,QPushButton, QWidget,QFileDialog, QMessageBox, QLineEdit, QTextEdit ,QVBoxLayout, QGridLayout, QFrame
from PySide6.QtCore import Qt
from datetime import datetime


app = QApplication(sys.argv)


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reader")
        self.setFixedSize(1000,700)
        self.setCentralWidget(Layouts.main_widget)
        self.first_image = QPixmap("C:/Users/ozany/OneDrive/Masaüstü/Python/Reader/codest1.png")
        images.imagelabel_1.setPixmap(self.first_image)
        self.Menu()

    def Menu(self):
        fileselection = QAction(QIcon("C:/Users/ozany/OneDrive/Masaüstü/Python/Reader/johnxina2.ico"),"Import File",self)
        fileselection.setStatusTip("Import your image or video")
        fileselection.triggered.connect(functions.imageselect)

        menubar = self.menuBar()
        filemenu = QMenu("File")
        menubar.addMenu(filemenu)
        filemenu.addAction(fileselection)



class functions():

    def imageselect():
        file = QFileDialog.getOpenFileName(None,"Select File","C:/Users/ozany/OneDrive/Masaüstü/Görseller","Image files (*.jpg *.png)")
        image1 = QPixmap(file[0])

        images.imagelabel_1.setPixmap(image1)
        images.imagelabel_1.show()
        if file[0] == "":
            # immage = QPixmap("C:/Users/ozany/OneDrive/Masaüstü/Python/Reader/johnxina.jpg")
            images.imagelabel_1.setPixmap(QPixmap("C:/Users/ozany/OneDrive/Masaüstü/Python/Reader/codest1.png"))
            images.imagelabel_1.show()
            Layouts.history.insertPlainText(f"*** {datetime.today()} No image is selected\n\n")
        else:
            Layouts.history.insertPlainText(f"*** {datetime.today()} Image Selected: {file}\n\n")

    def clearlayout():
        for i in reversed(range(Layouts.setting_layout.count())):
            removedwidget = Layouts.setting_layout.itemAt(i).widget()
            removedwidget.setParent(None)
            Layouts.setting_layout.removeWidget(removedwidget)

    def func1():
        functions.clearlayout()
        Layouts.setting_layout.addWidget(buttons.testbutton1)
        Layouts.setting_layout.addWidget(buttons.testbutton2)

    def func2():
        Table.table1.removeRow(1)



    def sizes(event):
        fsizes = str(images.imagelabel_1.size())
        l1 = fsizes.split("(")
        l1s = l1[-1].split(")")
        l1ss = l1s[0].split(",")
        imagewidth = int(l1ss[0])
        imageheight = int(l1ss[1])
        Layouts.history.insertPlainText(f"*** Image sizes are : {imagewidth},{imageheight}\n\n")

    def imagewidthh():
        fsizes = str(images.imagelabel_1.size())
        l1 = fsizes.split("(")
        l1s = l1[-1].split(")")
        l1ss = l1s[0].split(",")
        imagewidth = int(l1ss[0])
        return imagewidth

    def imageheightt():
        fsizes = str(images.imagelabel_1.size())
        l1 = fsizes.split("(")
        l1s = l1[-1].split(")")
        l1ss = l1s[0].split(",")
        imageheight = int(l1ss[1])
        return imageheight

    def changewvalue(value):
        images.imagelabel_1.setFixedWidth(value)

    def changehvalue(value):
        images.imagelabel_1.setFixedHeight(value)

    def resize():
        functions.clearlayout()
        wslider = QSlider(Qt.Horizontal)
        hslider = QSlider(Qt.Horizontal)
        wslider.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        hslider.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        wslider.setMaximum(500)
        hslider.setMaximum(400)
        wslider.setValue(functions.imagewidthh())
        hslider.setValue(functions.imageheightt())
        wlabel = QLabel("Width: {}".format(wslider.value()))
        hlabel = QLabel("Height: {}".format(hslider.value()))
        Layouts.setting_layout.addWidget(wlabel)
        Layouts.setting_layout.addWidget(wslider)
        Layouts.setting_layout.addWidget(hlabel)
        Layouts.setting_layout.addWidget(hslider)


        wslider.valueChanged[int].connect(functions.changewvalue)
        wslider.valueChanged[int].connect(lambda:wlabel.setText(f"Width: {str(wslider.value())}"))
        hslider.valueChanged[int].connect(functions.changehvalue)
        hslider.valueChanged[int].connect(lambda:hlabel.setText(f"Height: {str(hslider.value())}"))

    def add_row():
        Table.table1.insertRow(1)

    def testbut1():
        for i in reversed(range(Table.table1.rowCount()-1)):
            Table.table1.removeRow(i)
        for j in range(5):
            Table.table1.insertRow(1)





class buttons():

    button1 = QPushButton("Button 1", clicked = functions.imageselect)
    button1.setStyleSheet("background-color: magenta")
    button1.setFixedSize(100,50)

    button2 = QPushButton("Button 2", clicked = functions.func1)
    button2.setFixedSize(100,50)
    button2.setStyleSheet("background-color: red")

    button3 = QPushButton("Button 3", clicked = functions.func2)
    button3.setFixedSize(100,50)
    button3.setStyleSheet("background-color: orange")

    button4 = QPushButton("Button 4")
    button4.setFixedSize(100,50)
    button4.setStyleSheet("background-color: yellow")

    button5 = QPushButton("Button 5", clicked = functions.resize)
    button5.setFixedSize(100,50)
    button5.setStyleSheet("background-color: green")

    button6 = QPushButton("Button 6", clicked = functions.add_row)
    button6.setFixedSize(100,50)
    button6.setStyleSheet("background-color: cyan")

    testbutton1 = QPushButton("select", clicked = functions.testbut1)
    testbutton2 = QPushButton("resize")
    testbutton3 = QPushButton("test3")



class images():

    imagelabel_1 = QLabel()
    imagelabel_1.setScaledContents(True)
    imagelabel_1.installEventFilter(None)
    imagelabel_1.setMaximumSize(500,400)
    imagelabel_1.setCursor(QCursor(Qt.PointingHandCursor))
    imagelabel_1.mousePressEvent = functions.sizes


    imagelabel_2 = QLabel()
    imagelabel_2.setScaledContents(True)
    imagelabel_2.installEventFilter(None)
    imagelabel_2.setMaximumSize(400,400)


class Table():
    table1 = QTableWidget(1,3)
    table1.setFixedHeight(150)
    h_header = table1.horizontalHeader()
    h_header.setSectionResizeMode(0,QHeaderView.Stretch)
    h_header.setSectionResizeMode(1,QHeaderView.Stretch)
    h_header.setSectionResizeMode(2,QHeaderView.Stretch)


class Layouts():

    frame_layout = QGridLayout()

    #Buttons -----------------------------------------

    button_frame = QFrame()
    button_frame.setFrameShape(QFrame.StyledPanel)
    button_frame.setFixedWidth(150)
    button_layout = QGridLayout()
    button_layout.addWidget(buttons.button1)
    button_layout.addWidget(buttons.button2)
    button_layout.addWidget(buttons.button3)
    button_layout.addWidget(buttons.button4)
    button_layout.addWidget(buttons.button5)
    button_layout.addWidget(buttons.button6)
    button_frame.setLayout(button_layout)
    frame_layout.addWidget(button_frame,0,0,6,1)


    #Settings ---------------------------------------

    setting_frame = QFrame()
    setting_frame.setFrameShape(QFrame.StyledPanel)
    # setting_frame.setFixedWidth(300)
    setting_layout = QGridLayout()
    setting_frame.setLayout(setting_layout)



    #History ----------------------------------------

    history_frame = QFrame()
    history_frame.setFixedSize(300,300)
    history_frame.setFrameShape(QFrame.StyledPanel)
    history_layout = QGridLayout()
    history = QTextEdit()
    history.setReadOnly(True)
    history_layout.addWidget(history,0,0)
    history_frame.setLayout(history_layout)

    #Splitter ----------------------------------------

    splitter_frame = QFrame()
    splitter_frame.setFrameShape(QFrame.StyledPanel)
    splitter_layout = QVBoxLayout()
    splitter = QSplitter(Qt.Vertical)
    splitter.addWidget(setting_frame)
    splitter.addWidget(history_frame)
    splitter_layout.addWidget(splitter)
    splitter_frame.setLayout(splitter_layout)
    frame_layout.addWidget(splitter,0,1,6,1)

    #Images -----------------------------------------

    image_frame = QFrame()
    # image_frame.setFrameShape(QFrame.StyledPanel)
    image_layout = QGridLayout()
    image_layout.addWidget(images.imagelabel_1)
    image_frame.setLayout(image_layout)

    #Graph ----------------------------------------

    image2 = QPixmap("C:/Users/ozany/OneDrive/Masaüstü/Python/Reader/kazandi.jpg")
    image_frame2 = QFrame()
    # image_frame2.setFrameShape(QFrame.StyledPanel)
    image_layout2 = QGridLayout()
    images.imagelabel_2.setPixmap(image2)
    images.imagelabel_2.show()
    image_layout2.addWidget(images.imagelabel_2)
    image_frame2.setLayout(image_layout2)

    #Tabs ------------------------------------------

    tabs = QTabWidget()
    # tabs.setFixedSize(520,520)
    tabs.addTab(image_frame,"Image")
    tabs.addTab(image_frame2,"Graph")
    frame_layout.addWidget(tabs,0,2,6,1)

    #Tables ---------------------------------------

    table_frame = QFrame()
    table_layout = QGridLayout()
    table_layout.addWidget(Table.table1)
    table_frame.setLayout(table_layout)
    frame_layout.addWidget(table_frame,7,0,1,3)

    #Main Widget ----------------------------------

    main_widget = QWidget()
    main_widget.setLayout(frame_layout)



if __name__ == "__main__":

    gui = Window()
    gui.show()
    app.exec()
