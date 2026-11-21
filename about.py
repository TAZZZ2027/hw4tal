import webbrowser
from pathlib import Path

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
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
        self.setObjectName("aboutWindow")
        self.setWindowTitle("About Me")
        self.setFixedSize(380, 480)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 22, 24, 22)
        layout.setSpacing(12)

        self.my_name = QLabel("Tal Zer")
        self.my_name.setObjectName("aboutName")
        self.my_name.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.my_name)

        self.my_email = QLabel("Tal.Zer@s.afeka.ac.il")
        self.my_email.setObjectName("aboutEmail")
        self.my_email.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.my_email)

        self.my_picture = ClickableLabel()
        self.my_picture.setObjectName("aboutPicture")
        self.my_picture.setAlignment(Qt.AlignCenter)
        image_path = Path(__file__).with_name("Eeyore.jpg")
        image = QPixmap(str(image_path)).scaled(
            300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.my_picture.setPixmap(image)
        self.my_picture.clicked.connect(self.open_facebook_video)
        layout.addWidget(self.my_picture, 1)

    def open_facebook_video(self):
        url = "https://www.facebook.com/reel/1131406196065440"
        webbrowser.open(url)


if __name__ == '__main__':
    app = QApplication()
    window = AboutWindow()
    window.show()
    app.exec()