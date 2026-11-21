import webbrowser
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal

class ClickableLabel(QLabel):
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()

        
class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('About Me')
        self.setGeometry(100, 100, 360, 460)

        self.my_name = QLabel('Tal Zer', self)
        self.my_name.setGeometry(20, 20, 300, 30)
        self.my_name.setStyleSheet('background-color:lightpink')

        self.my_email = QLabel('Tal.Zer@s.afeka.ac.il', self)
        self.my_email.setGeometry(20, 60, 300, 30)
        self.my_email.setStyleSheet('background-color:lightpink')

        self.my_picture = ClickableLabel(self)
        self.my_picture.setGeometry(20, 110, 300, 300)

        image = QPixmap('Eeyore.jpg').scaled(300, 300)
        self.my_picture.setPixmap(image)
        self.my_picture.clicked.connect(self.open_facebook_video) 
      
    def open_facebook_video(self):
        url = 'https://www.facebook.com/reel/1131406196065440' 
        webbrowser.open(url)






if __name__ == '__main__':
    app = QApplication()
    window = AboutWindow()
    window.show()
    app.exec()