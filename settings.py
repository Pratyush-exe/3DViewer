# By Pratyush Kumar Patnaiks

from configparser import ConfigParser
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

GRADIENTIMAGE = 'Data/colorpicker.jpg'

class SettingUIMW(object):

    def __init__(self):

        self.file = 'config.ini'
        self.defFile = 'defaultConfig.ini'
        self.config = ConfigParser()
        self.config.read(self.file)

    def SettingsetupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 730)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(-30, -20, 1601, 1031))
        self.Background.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.WindowSettings = QtWidgets.QGroupBox(self.centralwidget)
        self.WindowSettings.setGeometry(QtCore.QRect(20, 20, 551, 131))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.WindowSettings.setPalette(palette)
        self.WindowSettings.setObjectName("WindowSettings")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.WindowSettings)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 511, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.h1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.h1.setContentsMargins(0, 0, 0, 0)
        self.h1.setObjectName("h1")
        self.c11 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.c11.setObjectName("c11")
        self.h1.addWidget(self.c11)
        self.c12 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.c12.setObjectName("c12")
        self.h1.addWidget(self.c12)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.WindowSettings)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 70, 511, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.h2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.h2.setContentsMargins(0, 0, 0, 0)
        self.h2.setObjectName("h2")
        self.c21 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.c21.setObjectName("c21")
        self.h2.addWidget(self.c21)
        self.c22 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.c22.setObjectName("c22")
        self.h2.addWidget(self.c22)
        self.WindowSettings_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.WindowSettings_2.setGeometry(QtCore.QRect(20, 250, 551, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.WindowSettings_2.setPalette(palette)
        self.WindowSettings_2.setObjectName("WindowSettings_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.WindowSettings_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 30, 511, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.formLayoutWidget)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_2)
        self.BackgroundCOlorBox = QtWidgets.QGroupBox(self.centralwidget)
        self.BackgroundCOlorBox.setGeometry(QtCore.QRect(20, 170, 551, 61))
        self.BackgroundCOlorBox.setStyleSheet("color:white;")
        self.BackgroundCOlorBox.setObjectName("BackgroundCOlorBox")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.BackgroundCOlorBox)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(110, 10, 421, 51))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Bar1 = QtWidgets.QSlider(self.horizontalLayoutWidget_7)
        self.Bar1.setOrientation(QtCore.Qt.Horizontal)
        self.Bar1.setObjectName("Bar1")
        self.horizontalLayout.addWidget(self.Bar1)
        self.Bar2 = QtWidgets.QSlider(self.horizontalLayoutWidget_7)
        self.Bar2.setOrientation(QtCore.Qt.Horizontal)
        self.Bar2.setObjectName("Bar2")
        self.horizontalLayout.addWidget(self.Bar2)
        self.Bar3 = QtWidgets.QSlider(self.horizontalLayoutWidget_7)
        self.Bar3.setOrientation(QtCore.Qt.Horizontal)
        self.Bar3.setObjectName("Bar3")
        self.horizontalLayout.addWidget(self.Bar3)
        self.label = QtWidgets.QLabel(self.BackgroundCOlorBox)
        self.label.setGeometry(QtCore.QRect(40, 25, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.movementDefault = QtWidgets.QGroupBox(self.centralwidget)
        self.movementDefault.setGeometry(QtCore.QRect(20, 370, 551, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.movementDefault.setPalette(palette)
        self.movementDefault.setObjectName("movementDefault")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.movementDefault)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 30, 531, 41))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.h3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.h3.setContentsMargins(0, 0, 0, 0)
        self.h3.setObjectName("h3")
        self.VerticalBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_8)
        self.VerticalBox.setObjectName("VerticalBox")
        self.h3.addWidget(self.VerticalBox)
        self.HorizontalVBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_8)
        self.HorizontalVBox.setObjectName("HorizontalVBox")
        self.h3.addWidget(self.HorizontalVBox)
        self.scaleBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_8)
        self.scaleBox.setObjectName("scaleBox")
        self.h3.addWidget(self.scaleBox)
        self.SmoothMoveBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_8)
        self.SmoothMoveBox.setObjectName("SmoothMoveBox")
        self.h3.addWidget(self.SmoothMoveBox)
        self.movementDefault_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.movementDefault_2.setGeometry(QtCore.QRect(20, 480, 551, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.movementDefault_2.setPalette(palette)
        self.movementDefault_2.setObjectName("movementDefault_2")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.movementDefault_2)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(20, 0, 511, 80))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_9)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_9)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.movementDefault_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.movementDefault_3.setGeometry(QtCore.QRect(20, 580, 550, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.movementDefault_3.setPalette(palette)
        self.movementDefault_3.setObjectName("movementDefault_3")
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.movementDefault_3)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(20, 0, 341, 80))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.colorPicker = QtWidgets.QLabel(self.BackgroundCOlorBox)
        self.colorPicker.setGeometry(QtCore.QRect(16, 25, 16, 16))
        self.colorPicker.setText("")
        self.colorPicker.setPixmap(QtGui.QPixmap(GRADIENTIMAGE))
        self.colorPicker.setScaledContents(True)
        self.colorPicker.setObjectName("colorPicker")
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_10)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_4.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_10)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_4.addWidget(self.checkBox)
        self.label_4 = QtWidgets.QLabel(self.movementDefault_3)
        self.label_4.setGeometry(QtCore.QRect(390, 31, 91, 16))
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(self.movementDefault_3)
        self.spinBox.setGeometry(QtCore.QRect(490, 28, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(40, 669, 511, 51))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_11)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_11)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_2.clicked.connect(self.save)
        self.pushButton.clicked.connect(self.reset)
        self.colorPicker.mousePressEvent = self.picker

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def picker(self, _):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.Bar1.setValue(int(color.red() / 2.55))
            self.Bar2.setValue(int(color.green() / 2.55))
            self.Bar3.setValue(int(color.blue() / 2.55))

    def reset(self):
        self.build(file=self.defFile)
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Settings")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Settings are reset to default")
        msg.addButton(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def save(self):
        if self.c11.isChecked():
            self.config.set('window', 'CameraWindow', 'True')
        else:
            self.config.set('window', 'CameraWindow', 'False')
        if self.c12.isChecked():
            self.config.set('window', 'DetectionWindow', 'True')
        else:
            self.config.set('window', 'DetectionWindow', 'False')
        if self.c21.isChecked():
            self.config.set('window', 'LoadPrevModel', 'True')
        else:
            self.config.set('window', 'LoadPrevModel', 'False')
        if self.c22.isChecked():
            self.config.set('window', 'AskCamAccessEverytime', 'True')
        else:
            self.config.set('window', 'AskCamAccessEverytime', 'False')

        self.config.set('backgroundColor', 'red', str(self.Bar1.value()))
        self.config.set('backgroundColor', 'green', str(self.Bar2.value()))
        self.config.set('backgroundColor', 'blue', str(self.Bar3.value()))

        self.config.set('modelViewerSettings', 'SensitivityConstant', str(self.horizontalSlider.value()))
        self.config.set('modelViewerSettings', 'SpeedMovement', str(self.horizontalSlider_2.value()))

        if self.VerticalBox.isChecked():
            self.config.set('DefaultMovements', 'Vertical', 'True')
        else:
            self.config.set('DefaultMovements', 'Vertical', 'False')
        if self.HorizontalVBox.isChecked():
            self.config.set('DefaultMovements', 'Horizontal', 'True')
        else:
            self.config.set('DefaultMovements', 'Horizontal', 'False')
        if self.scaleBox.isChecked():
            self.config.set('DefaultMovements', 'Scale', 'True')
        else:
            self.config.set('DefaultMovements', 'Scale', 'False')
        if self.SmoothMoveBox.isChecked():
            self.config.set('DefaultMovements', 'SmoothMove', 'True')
        else:
            self.config.set('DefaultMovements', 'SmoothMove', 'False')

        if self.checkBox_2.isChecked():
            self.config.set('others', 'negate', 'True')
        else:
            self.config.set('others', 'negate', 'False')
        if self.checkBox.isChecked():
            self.config.set('others', 'continuousPressMovement', 'True')
        else:
            self.config.set('others', 'continuousPressMovement', 'False')
        self.config.set('others', 'defaultCamera', str(self.spinBox.value()))

        with open(self.file, 'w') as self.configfile:
            self.config.write(self.configfile)
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Settings")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Settings are saved")
        msg.addButton(QtWidgets.QMessageBox.Ok)
        msg.addButton(QtWidgets.QMessageBox.Close)
        x = msg.exec_()
        if x == QtWidgets.QMessageBox.Close:
            sys.exit()

    def build(self, file='config.ini'):

        self.config = ConfigParser()
        self.config.read(file)

        if self.config['window']['CameraWindow'] == 'True':
            self.c11.setChecked(True)
        else:
            self.c11.setChecked(False)
        if self.config['window']['DetectionWindow'] == 'True':
            self.c12.setChecked(True)
        else:
            self.c12.setChecked(False)
        if self.config['window']['LoadPrevModel'] == 'True':
            self.c21.setChecked(True)
        else:
            self.c21.setChecked(False)
        if self.config['window']['AskCamAccessEverytime'] == 'True':
            self.c22.setChecked(True)
        else:
            self.c22.setChecked(False)
        self.c11.repaint()
        self.c12.repaint()
        self.c21.repaint()
        self.c22.repaint()

        r = self.config['backgroundColor']['red']
        self.Bar1.setValue(int(r))
        g = self.config['backgroundColor']['green']
        self.Bar2.setValue(int(g))
        b = self.config['backgroundColor']['blue']
        self.Bar3.setValue(int(b))
        self.Bar1.repaint()
        self.Bar2.repaint()
        self.Bar3.repaint()

        SensitivityConstant = self.config['modelViewerSettings']['SensitivityConstant']
        self.horizontalSlider.setValue(int(SensitivityConstant))
        SpeedMovement = self.config['modelViewerSettings']['SpeedMovement']
        self.horizontalSlider_2.setValue(int(SpeedMovement))
        self.horizontalSlider.repaint()
        self.horizontalSlider_2.repaint()

        if self.config['DefaultMovements']['Vertical'] == 'True':
            self.VerticalBox.setChecked(True)
        else:
            self.VerticalBox.setChecked(False)
        if self.config['DefaultMovements']['Horizontal'] == 'True':
            self.HorizontalVBox.setChecked(True)
        else:
            self.HorizontalVBox.setChecked(False)
        if self.config['DefaultMovements']['Scale'] == 'True':
            self.scaleBox.setChecked(True)
        else:
            self.scaleBox.setChecked(False)
        if self.config['DefaultMovements']['SmoothMove'] == 'True':
            self.SmoothMoveBox.setChecked(True)
        else:
            self.SmoothMoveBox.setChecked(False)
        self.VerticalBox.repaint()
        self.HorizontalVBox.repaint()
        self.scaleBox.repaint()
        self.SmoothMoveBox.repaint()

        if self.config['Controller']['keyboard'] == 'True':
            self.radioButton_2.setChecked(True)
        else:
            self.radioButton_2.setChecked(False)
        if self.config['Controller']['pai'] == 'True':
            self.radioButton.setChecked(True)
        else:
            self.radioButton.setChecked(False)

        if self.config['others']['negate'] == 'True':
            self.checkBox_2.setChecked(True)
        else:
            self.checkBox_2.setChecked(False)
        if self.config['others']['continuousPressMovement'] == 'True':
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)
        self.radioButton.repaint()
        self.radioButton_2.repaint()
        self.checkBox.repaint()
        self.checkBox_2.repaint()

        s = self.config['others']['defaultCamera']
        self.spinBox.setValue(int(s))
        self.spinBox.repaint()

    def retranslateUi(self, MainWindow):

        self.c21.setDisabled(True)
        self.radioButton.setDisabled(True)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.WindowSettings.setTitle(_translate("MainWindow", "Window Settings"))
        self.c11.setText(_translate("MainWindow", "Camera Window"))
        self.c12.setText(_translate("MainWindow", "Detection Window"))
        self.c21.setText(_translate("MainWindow", "Load Previous Model"))
        self.c22.setText(_translate("MainWindow", "Ask Camera Access Everytime"))
        self.WindowSettings_2.setTitle(_translate("MainWindow", "Model Viewer Settings"))
        self.label_2.setText(_translate("MainWindow", "Sensitivity Constant"))
        self.label_3.setText(_translate("MainWindow", "Speed Movement"))
        self.BackgroundCOlorBox.setTitle(_translate("MainWindow", "BackGround Color"))
        self.label.setText(_translate("MainWindow", "RGB"))
        self.movementDefault.setTitle(_translate("MainWindow", "Default Allowed Movements"))
        self.VerticalBox.setText(_translate("MainWindow", "Vertical"))
        self.HorizontalVBox.setText(_translate("MainWindow", "Horizontal"))
        self.scaleBox.setText(_translate("MainWindow", "Scale"))
        self.SmoothMoveBox.setText(_translate("MainWindow", "Smooth Move"))
        self.movementDefault_2.setTitle(_translate("MainWindow", "Controller"))
        self.radioButton_2.setText(_translate("MainWindow", "Keyboard Controller"))
        self.radioButton.setText(_translate("MainWindow", "Pai Controller"))
        self.movementDefault_3.setTitle(_translate("MainWindow", "Others"))
        self.checkBox_2.setText(_translate("MainWindow", "Negate Buttons"))
        self.checkBox.setText(_translate("MainWindow", "Continous Press Movement"))
        self.label_4.setText(_translate("MainWindow", "Default Camera"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.pushButton.setText(_translate("MainWindow", "Reset"))

        self.build()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SettingUIMW()
    ui.SettingsetupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
