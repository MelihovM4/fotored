import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton,QGroupBox,QButtonGroup,QTextEdit,QListWidget,QLineEdit,QInputDialog
from PIL import Image 
from PIL import ImageFilter

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files,extensions):
    result = list()
    for i in files:
        for j in extensions:
            if i.endwith(j) == True:
                result.append(i)
    return result

def showFilenamesList():
    chooseWorkdir()
    extensions = ('.png','.jpd','.jpeg','.bmp')
    files = os.listdir(workdir)
    filename = filter(files,extensions)
    pics.clear()
    for k in filename:
        pics.addItem(k)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.file = None
        self.pdp = 'pic'

    def saveImage():
        path = os.path.join(workdir,self.pdp)
        if not(os.path.exist(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path,self.filename)
        self.image.save(image_path)

    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir,self.pdp,self.filename)
        self.showImage(image_path)

    def right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path1 = os.path.join(workdir,self.pdp,self.filename)
        self.showImage(image_path1)

    def left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path1 = os.path.join(workdir,self.pdp,self.filename)
        self.showImage(image_path1)

    def zer(self):
        self.image = self.image.transpose(Image.ROTATE_180)
        self.saveImage()
        image_path1 = os.path.join(workdir,self.pdp,self.filename)
        self.showImage(image_path1)

    def blur(self):
        self.image = self.image.transpose(ImageFilter.BLUR)
        self.saveImage()
        image_path1 = os.path.join(workdir,self.pdp,self.filename)
        self.showImage(image_path1)

    def loadImage(self,filename):
        self.filename = filename
        image_path = os.path.join(workdir,filename)
        self.image = Image.open(image_path)

    def showImage(self,path):
        pic.hide()
        pixmapimage = QPixmap(path)
        w, h = pic.width(),pic.height()
        pixmapimage = pixmapimage.scaled(w,d,Qt.KeepAspectRatio)
        pic.setPixmap(pixmapimage)
        pic.show()

workimage = ImageProcessor()

def showChosenImage():
    if pics.currentRow() >= 0:
        filename = pics.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir,workimage.filename)
        workimage.showImage(image_path)

app = QApplication([])
win = QWidget()
win.setWindowTitle('XXX')

papka = QPushButton('Папка')
inte1 = QPushButton('Влево')
inte2 = QPushButton('Вправо')
inte3 = QPushButton('Зеркально')
inte4 = QPushButton('Размытие')
inte5 = QPushButton('ч/б')
pics = QListWidget()
pic = QLabel('Картинка')
pics.currentRowChanged.connect(showChosenImage)

vt1 = QVBoxLayout()
vt2 = QVBoxLayout()
osn = QHBoxLayout()
hor = QHBoxLayout()

vt1.addWidget(papka)
vt1.addWidget(pics)
vt2.addWidget(pic)
hor.addWidget(inte1)
hor.addWidget(inte2)
hor.addWidget(inte3)
hor.addWidget(inte4)
hor.addWidget(inte5)
vt2.addLayout(hor)
osn.addLayout(vt1,20)
osn.addLayout(vt2,80)

inte1.clicked.connect(workimage.left)
inte2.clicked.connect(workimage.right)
inte3.clicked.connect(workimage.zer)
inte4.clicked.connect(workimage.blur)
inte5.clicked.connect(workimage.do_bw)
papka.clicked.connect(showFilenamesList)
win.setLayout(osn)

win.show()
app.exec()


    


