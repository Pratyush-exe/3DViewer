# By Pratyush Kumar Patnaiks
# Used 'pyinstaller --hidden-import vtk --hidden-import mediapipe --hidden-import vtkmodules.all --hidden-import vtk.vtkmodules.qt --noconsole --icon="./Data/icon.ico" 3DViewer
# .py' code in terminal to convert to .exe format

from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5 import QtGui, QtWidgets, QtCore
from configparser import ConfigParser
from PyQt5.QtCore import *
import mediapipe as mp
import webbrowser
import settings
import math
import vtk
import cv2

file = 'config.ini'
config = ConfigParser()
config.read(file)

cameraNum = int(config['others']['defaultCamera'])

BLACKIMAGE = r'Data/black.jpg'
WHITEIMAGE = r'Data/white.jpg'


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()

        self.website = "https://github.com/Pratyush-exe"
        self.SensitivityConstant = int(config['modelViewerSettings']['SensitivityConstant'])
        self.Speed = int(config['modelViewerSettings']['SpeedMovement'])
        self.path = config['File']['path']
        self.cur_x, self.cur_y, self.last_x, self.last_y = None, None, None, None
        self.prev_length = 0

        self.negationKeys = config['others']['negate'] == 'True'
        self.refresh = True
        self.ContinuePressForMovement = config['others']['continuousPressMovement'] == 'True'

        # self.useController = True
        # self.command = 3
        # self.arduinoData = serial.Serial('COM3', 9600)

        self.hor = config['DefaultMovements']['Vertical'] == 'True'
        self.ver = config['DefaultMovements']['Horizontal'] == 'True'
        self.scale = config['DefaultMovements']['Scale'] == 'True'
        self.smoothMove = config['DefaultMovements']['smoothmove'] == 'True'

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1479, 918)
        MainWindow.setFixedSize(1479, 918)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.HandDet = QtWidgets.QLabel(self.centralwidget)
        self.HandDet.setGeometry(QtCore.QRect(10, 434, 550, 413))
        self.HandDet.setStyleSheet("background-color: rgb(170, 85, 255);\n"
                                   "border-style: outset;\n"
                                   "border-width: 1px;\n"
                                   "border-color: white;")
        self.HandDet.setText("")
        self.HandDet.setPixmap(QtGui.QPixmap(BLACKIMAGE))
        self.HandDet.setObjectName("HandDet")
        self.openGLWindow = QtWidgets.QLabel(self.centralwidget)
        self.openGLWindow.setGeometry(QtCore.QRect(570, 9, 900, 900))
        self.openGLWindow.setStyleSheet("border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-color: white;")
        self.openGLWindow.setText("")
        self.openGLWindow.setObjectName("openGLWindow")
        self.Camera = QtWidgets.QLabel(self.centralwidget)
        self.Camera.setGeometry(QtCore.QRect(10, 10, 550, 413))
        self.Camera.setStyleSheet("background-color: rgb(170, 85, 255);\n"
                                  "border-style: outset;\n"
                                  "border-width: 1px;\n"
                                  "border-color: white;")
        self.Camera.setText("")
        self.Camera.setPixmap(QtGui.QPixmap(BLACKIMAGE))
        self.Camera.setScaledContents(False)
        self.Camera.setObjectName("Camera")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 1601, 1031))
        self.Background.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.HandDet_CheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.HandDet_CheckBox.setGeometry(QtCore.QRect(20, 820, 16, 20))
        self.HandDet_CheckBox.setText("")
        self.HandDet_CheckBox.setObjectName("HandDet_CheckBox")
        self.Camera_CheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.Camera_CheckBox.setGeometry(QtCore.QRect(20, 390, 16, 20))
        self.Camera_CheckBox.setText("")
        self.Camera_CheckBox.setObjectName("Camera_CheckBox")
        self.OpenGL_CheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.OpenGL_CheckBox.setGeometry(QtCore.QRect(580, 880, 16, 20))
        self.OpenGL_CheckBox.setText("")
        self.OpenGL_CheckBox.setObjectName("OpenGL_CheckBox")
        self.OpenGLFrame = QtWidgets.QFrame(self.centralwidget)
        self.OpenGLFrame.setGeometry(QtCore.QRect(571, 10, 898, 898))
        self.OpenGLFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.OpenGLFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OpenGLFrame.setObjectName("OpenGLFrame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 859, 551, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.HLayoutCont_Shaodws = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.HLayoutCont_Shaodws.setContentsMargins(0, 0, 0, 0)
        self.HLayoutCont_Shaodws.setSpacing(30)
        self.HLayoutCont_Shaodws.setObjectName("HLayoutCont_Shaodws")
        self.Shadow_about = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Shadow_about.setStyleSheet("background-color: rgb(251, 207, 0);\n"
                                        "border-radius: 20px;")
        self.Shadow_about.setText("")
        self.Shadow_about.setObjectName("Shadow_about")
        self.HLayoutCont_Shaodws.addWidget(self.Shadow_about)
        self.Shadow_update = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Shadow_update.setStyleSheet("background-color: rgb(251, 207, 0);\n"
                                         "border-radius: 20px;")
        self.Shadow_update.setText("")
        self.Shadow_update.setObjectName("Shadow_update")
        self.HLayoutCont_Shaodws.addWidget(self.Shadow_update)
        self.Shadow_upload = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Shadow_upload.setStyleSheet("background-color: rgb(251, 207, 0);\n"
                                         "border-radius: 20px;")
        self.Shadow_upload.setText("")
        self.Shadow_upload.setObjectName("Shadow_upload")
        self.HLayoutCont_Shaodws.addWidget(self.Shadow_upload)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(7, 856, 551, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.HLayoutCont = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.HLayoutCont.setContentsMargins(0, 0, 0, 0)
        self.HLayoutCont.setSpacing(30)
        self.HLayoutCont.setObjectName("HLayoutCont")
        self.Upload_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Upload_label.setFont(font)
        self.Upload_label.setStyleSheet("background-color: rgb(255, 242, 0);\n"
                                        "border-radius: 20px;\n"
                                        "color: rgb(79, 79, 79);")
        self.Upload_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Upload_label.setObjectName("Upload_label")
        self.HLayoutCont.addWidget(self.Upload_label)
        self.Update_Label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Update_Label.setFont(font)
        self.Update_Label.setStyleSheet("background-color: rgb(255, 242, 0);\n"
                                        "border-radius: 20px;\n"
                                        "color: rgb(79, 79, 79);")
        self.Update_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Update_Label.setObjectName("Update_Label")
        self.HLayoutCont.addWidget(self.Update_Label)
        self.About_Label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.About_Label.setFont(font)
        self.About_Label.setStyleSheet("background-color: rgb(255, 242, 0);\n"
                                       "border-radius: 20px;\n"
                                       "color: rgb(79, 79, 79);")
        self.About_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.About_Label.setObjectName("About_Label")
        self.HLayoutCont.addWidget(self.About_Label)
        self.Background.raise_()
        self.HandDet.raise_()
        self.Camera.raise_()
        self.HandDet_CheckBox.raise_()
        self.Camera_CheckBox.raise_()
        self.openGLWindow.raise_()
        self.OpenGLFrame.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.OpenGL_CheckBox.raise_()
        self.Camera_CheckBox.setChecked(True)
        self.HandDet_CheckBox.setChecked(True)

        self.init_openGL()

        if config['window']['askcamaccesseverytime'] == 'True':
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Grant Access")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Camera access required. Allow?")
            msg.addButton(QtWidgets.QMessageBox.Yes)
            msg.addButton(QtWidgets.QMessageBox.No)
            x = msg.exec_()
            if x == QtWidgets.QMessageBox.Yes:
                self.worker = WorkerClassCamera()
                self.worker.start()
                self.worker.ImageUpdate.connect(self.ImageUpdateSlot)
            else:
                quit()
        else:
            self.worker = WorkerClassCamera()
            self.worker.start()
            self.worker.ImageUpdate.connect(self.ImageUpdateSlot)
        self.Upload_label.mousePressEvent = self.open_file
        MainWindow.keyPressEvent = self.keyPress
        if self.ContinuePressForMovement: MainWindow.keyReleaseEvent = self.keyRel

        self.Update_Label.mousePressEvent = self.settings_func
        self.About_Label.mousePressEvent = self.web

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def web(self, _):
        webbrowser.open_new(self.website)

    def settings_func(self, _):
        self.SettingsMW = QtWidgets.QMainWindow()
        self.SettingsUI = settings.SettingUIMW()
        self.SettingsUI.SettingsetupUi(self.SettingsMW)
        MainWindow.close()
        self.SettingsMW.show()

    def change_model(self):
        self.ren.RemoveAllViewProps()
        self.Creatobj(self.ren)

    def init_openGL(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setGeometry(QtCore.QRect(570, 10, 901, 901))
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(570, 10, 901, 901))
        self.vtkWidget = QVTKRenderWindowInteractor()
        self.verticalLayout.addWidget(self.vtkWidget)
        self.ren = vtk.vtkRenderer()
        self.ren.SetBackground(int(config['backgroundColor']['red']) / 100,
                               int(config['backgroundColor']['green']) / 100,
                               int(config['backgroundColor']['blue']) / 100)
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        self.Creatobj(self.ren)

        self.renwin = self.vtkWidget.GetRenderWindow()
        self.renwin.AddRenderer(self.ren)

        self.iren.Initialize()
        self.iren.Start()
        self.frame.setLayout(self.verticalLayout)

    def keyRel(self, _):
        self.hor = self.ver = self.scale = True

    def keyPress(self, event):

        if event.key() == Qt.Key_N:
            if self.negationKeys:
                self.negationKeys = False
            else:
                self.negationKeys = True
        if event.key() == Qt.Key_R:
            if self.refresh:
                self.hor = self.ver = self.scale = True
                self.refresh = True
            else:
                self.hor = self.ver = self.scale = False
                self.refresh = False
        if not self.negationKeys:
            if event.key() == Qt.Key_V:
                self.ver = True
                self.hor = self.scale = False
            if event.key() == Qt.Key_H:
                self.hor = True
                self.ver = self.scale = False
            if event.key() == Qt.Key_S:
                self.scale = True
                self.hor = self.ver = False
        elif self.negationKeys:
            if event.key() == Qt.Key_V:
                self.ver = False
                self.hor = self.scale = True
            if event.key() == Qt.Key_H:
                self.hor = False
                self.ver = self.scale = True
            if event.key() == Qt.Key_S:
                self.scale = False
                self.hor = self.ver = True

    def Creatobj(self, ren):
        filename = self.path
        reader = vtk.vtkOBJReader()
        reader.SetFileName(filename)
        reader.Update()

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        ren.AddActor(actor)
        ren.ResetCamera()

    def Rotate(self, camera, x, y, lastX, lastY):
        camera.Azimuth(lastX - x)
        camera.Elevation(lastY - y)
        camera.OrthogonalizeViewUp()
        self.renwin.Render()

    def Zoom(self, camera, length):
        if 100 > length > 10 and abs(self.prev_length - length) > 1:
            zoomFactor = (length-self.SensitivityConstant) / 70
            camera.Zoom(zoomFactor)
            self.renwin.Render()
            self.prev_length = length

    def ImageUpdateSlot(self, Image1, Image2, length, cur_x, cur_y, last_x, last_y):

        self.cur_x, self.cur_y = cur_x, cur_y
        self.last_x, self.last_y = last_x, last_y
        self.length = length

        xypos = self.iren.GetEventPosition()
        x, y = xypos[0], xypos[1]

        center = self.renwin.GetSize()
        self.centerX, self.centerY = center[0] / 2.0, center[1] / 2.0

        if self.scale: self.Zoom(self.ren.GetActiveCamera(), self.length)
        if self.hor: self.horizontal_movements(x, y)
        if self.ver: self.vertical_movements(x, y)

        if config['window']['camerawindow'] == 'True':
            self.Camera_CheckBox.setChecked(True)
        else:
            self.Camera_CheckBox.setChecked(False)

        if config['window']['detectionwindow'] == 'True':
            self.HandDet_CheckBox.setChecked(True)
        else:
            self.HandDet_CheckBox.setChecked(False)

        if self.Camera_CheckBox.isChecked():
            self.Camera.setPixmap(QtGui.QPixmap.fromImage(Image1))
        else:
            self.Camera.setPixmap(QtGui.QPixmap(BLACKIMAGE))

        if self.HandDet_CheckBox.isChecked():
            self.HandDet.setPixmap(QtGui.QPixmap(Image2))
        else:
            self.HandDet.setPixmap(QtGui.QPixmap(BLACKIMAGE))

    def horizontal_movements(self, x, y):
        if abs(self.cur_x - self.last_x) >= self.SensitivityConstant and self.last_x != -1:
            if self.cur_x < self.last_x:
                if self.smoothMove:
                    for i in range(self.Speed):
                        self.Rotate(self.ren.GetActiveCamera(), x, y, x + pow(1.02, i / 10), y)
                else:
                    self.Rotate(self.ren.GetActiveCamera(), x, y, x + self.Speed, y)
            if self.cur_x > self.last_x:
                if self.smoothMove:
                    for i in range(self.Speed):
                        self.Rotate(self.ren.GetActiveCamera(), x, y, x - pow(1.02, i / 10), y)
                else:
                    self.Rotate(self.ren.GetActiveCamera(), x, y, x - self.Speed, y)

    def vertical_movements(self, x, y):
        if abs(self.cur_y - self.last_y) >= self.SensitivityConstant and self.last_y != -1:
            if self.cur_y < self.last_y:
                if self.smoothMove:
                    for i in range(self.Speed):
                        self.Rotate(self.ren.GetActiveCamera(), x, y, x, y - pow(1.02, i / 10))
                else:
                    self.Rotate(self.ren.GetActiveCamera(), x, y, x, y - self.Speed)
            if self.cur_y > self.last_y:
                if self.smoothMove:
                    for i in range(self.Speed):
                        self.Rotate(self.ren.GetActiveCamera(), x, y, x, y + pow(1.02, i / 10))
                else:
                    self.Rotate(self.ren.GetActiveCamera(), x, y, x, y + self.Speed)

    def open_file(self, _):
        while True:
            self.path, _ = QtWidgets.QFileDialog.getOpenFileName()
            x = self.path.split(".")
            if x[-1] == "obj":
                self.change_model()

                config.set('File', 'path', self.path)
                with open(file, 'w') as configfile:
                    config.write(configfile)

                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Open OBJ File")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(self.path + " file opened")
                msg.addButton(QtWidgets.QMessageBox.Ok)
                msg.exec_()
                break

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Upload_label.setText(_translate("MainWindow", "Upload New"))
        self.Update_Label.setText(_translate("MainWindow", "Settings"))
        self.About_Label.setText(_translate("MainWindow", "About"))


def convertToQImage(Image):
    return QtGui.QImage(Image.data, Image.shape[1], Image.shape[0], QtGui.QImage.Format_RGB888)


class WorkerClassCamera(QThread):
    ImageUpdate = QtCore.pyqtSignal(QtGui.QImage, QtGui.QImage, int, int, int, int, int)

    def run(self):
        self.ActiveThread = True
        Captured = cv2.VideoCapture(cameraNum)
        mpHands = mp.solutions.hands
        mpHands = mp.solutions.hands
        hands = mpHands.Hands(max_num_hands=1)
        mpDraw = mp.solutions.drawing_utils

        set_8_prev_x, set_8_prev_y = 0, 0

        while self.ActiveThread:
            ret, frame = Captured.read()
            set = []
            HandDetBack = cv2.cvtColor(cv2.imread(WHITEIMAGE), cv2.COLOR_RGB2BGR)
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                Flipped = cv2.flip(Image, 1)
                results = hands.process(Flipped)
                set = []
                if results.multi_hand_landmarks:
                    for hand in results.multi_hand_landmarks:
                        for id, lm in enumerate(hand.landmark):
                            h, w, c = frame.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            set.append((cx, cy))

                        mpDraw.draw_landmarks(Flipped, hand, mpHands.HAND_CONNECTIONS)
                        mpDraw.draw_landmarks(HandDetBack, hand, mpHands.HAND_CONNECTIONS)
                    ConvertedImage1 = convertToQImage(Flipped).scaled(550, 413, QtCore.Qt.KeepAspectRatio)
                    ConvertedImage2 = convertToQImage(HandDetBack).scaled(550, 413, QtCore.Qt.KeepAspectRatio)
                    length = -1
                else:
                    ConvertedImage1 = convertToQImage(Flipped).scaled(550, 413, QtCore.Qt.KeepAspectRatio)
                    ConvertedImage2 = convertToQImage(HandDetBack).scaled(550, 413, QtCore.Qt.KeepAspectRatio)

                if set:
                    length = int(math.sqrt(math.pow(set[4][0] - set[8][0], 2) + math.pow(set[4][1] - set[8][1], 2)))
                    self.ImageUpdate.emit(ConvertedImage1, ConvertedImage2, length, set[8][0], set[8][1],
                                          set_8_prev_x,
                                          set_8_prev_y)
                else:
                    self.ImageUpdate.emit(ConvertedImage1, ConvertedImage2, -1, -1, -1,
                                          -1,
                                          -1)
                try:
                    set_8_prev_x = set[8][0]
                    set_8_prev_y = set[8][1]
                except:
                    IndexError

    def stop(self):
        self.ActiveThread = False
        self.quit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('3DViewer-v1.0')
    MainWindow.setWindowIcon(QtGui.QIcon('Data/icon.ico'))
    MainWindow.show()
    sys.exit(app.exec_())
