from pathlib import Path
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class GradeManagerWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Student Grade Manager")
        self.resize(960, 680)
        self.setMinimumSize(720, 520)

        central_widget = QWidget()
        central_widget.setObjectName("centralWidget")
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(32, 28, 32, 24)
        layout.setSpacing(18)

        heading = QLabel("Student Grade Manager")
        heading.setObjectName("pageTitle")
        layout.addWidget(heading)

        actions = QHBoxLayout()
        actions.setSpacing(12)

        self.choose_button = QPushButton("Choose a Student")
        self.choose_button.setObjectName("chooseButton")
        self.update_button = QPushButton("Update File")
        self.update_button.setObjectName("updateButton")
        self.about_button = QPushButton("About")
        self.about_button.setObjectName("aboutButton")
        self.about_button.clicked.connect(self.show_about)

        actions.addWidget(self.choose_button)
        actions.addWidget(self.update_button)
        actions.addStretch()
        actions.addWidget(self.about_button)
        layout.addLayout(actions)

        self.table = QTableWidget(50, 3)
        self.table.setObjectName("gradesTable")
        self.table.setHorizontalHeaderLabels(
            ["ID", "Original Grades", "Corrected Grades"]
        )
        self.table.verticalHeader().setVisible(False)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.setAlternatingRowColors(True)
        self.table.setShowGrid(False)
        self.table.setEditTriggers(
            QTableWidget.EditTrigger.DoubleClicked
            | QTableWidget.EditTrigger.EditKeyPressed
        )
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setColumnWidth(0, 170)
        self.table.setColumnWidth(1, 260)
        self.table.setSortingEnabled(False)

        for row in range(50):
            for column in range(3):
                item = QTableWidgetItem()
                if column == 0:
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
                    )
                else:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(row, column, item)

        layout.addWidget(self.table, 1)

        footer = QLabel("50 student records")
        footer.setObjectName("tableFooter")
        layout.addWidget(footer)

    def show_about(self) -> None:
        QMessageBox.about(
            self,
            "About Student Grade Manager",
            "Student Grade Manager\nReview original grades and enter corrections.",
        )


def main() -> int:
    app = QApplication(sys.argv)
    stylesheet_path = Path(__file__).with_name("ex1.qss")
    app.setStyleSheet(stylesheet_path.read_text(encoding="utf-8"))

    window = GradeManagerWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
