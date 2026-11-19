from pathlib import Path
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QDoubleSpinBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QSpinBox
)


class GradeManagerWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.l_student = []
        self.student_ids = [] 
        self.original_grades = [] 
        self.corrected_grades = [] 
        self.selected_file = ''


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
        self.choose_button.clicked.connect(self.Choose_file_fun)

        self.update_button = QPushButton("Update File")
        self.update_button.setObjectName("updateButton")
        
        self.update_grade_button = QPushButton("Update Grade")
        self.update_grade_button.setObjectName("updateGradeButton")
        self.update_grade_button.clicked.connect(self.show_update_grade_dialog)

        self.about_button = QPushButton("About")
        self.about_button.setObjectName("aboutButton")
        self.about_button.clicked.connect(self.show_about)

        actions.addWidget(self.choose_button)
        actions.addWidget(self.update_button)
        actions.addWidget(self.update_grade_button)
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

    def show_update_grade_dialog(self) -> None:
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Grade")

        layout = QVBoxLayout(dialog)

        student_id_label = QLabel("Student ID")
        self.student_id_combo = QComboBox()
        self.student_id_combo.setEditable(True)
        self.student_id_combo.addItems(str(student_id) for student_id in self.student_ids)
        layout.addWidget(student_id_label)
        layout.addWidget(self.student_id_combo)

        score_label = QLabel("Score / Bonus")
        self.score_input = QSpinBox()
        layout.addWidget(score_label)
        layout.addWidget(self.score_input)

        submit_button = QPushButton("Submit")
        layout.addWidget(submit_button)
        submit_button.clicked.connect(self.update_grade)

        dialog.exec()

    def show_about(self) -> None:
        QMessageBox.about(
            self,
            "About Student Grade Manager",
            "Student Grade Manager\nReview original grades and enter corrections.",
        )


    def Choose_file_fun(self):
      self.selected_file = "grades.csv" 
      if self.selected_file:
        with open(self.selected_file, 'r') as f:
            next(f)
            for l in f:
                self.l_student = l.split(',')
                self.student_ids.append(int(self.l_student[0]))
                self.original_grades.append(int(self.l_student[1]))
                self.corrected_grades.append(int(self.l_student[1]))
        self.update_table()


    def update_table(self):
        num_rows = 49
        self.table.setRowCount(num_rows)

        for i in range(num_rows):
            self.table.setItem(i, 0, QTableWidgetItem(str(self.student_ids[i])))
            self.table.setItem(i, 1, QTableWidgetItem(str(self.original_grades[i])))
            self.table.setItem(i, 2, QTableWidgetItem(str(self.corrected_grades[i])))
    
    def update_grade(self):
       self.id_choose=self.student_id_combo.currentText()
       self.update_num =self.score_input.value() 
       for i in range(len(self.student_ids)) :
           if int(self.id_choose) == int(self.student_ids[i]):
               grade = self.original_grades[i]
               grade = grade + self.update_num
               if(grade >= 100):
                   grade = 100
                   self.corrected_grades[i] = grade
               else:
                   self.corrected_grades[i] = grade

                   
       self.update_table()

 #   def update_exal(self):
    #new = []
#       with open(self.selected_file, 'r') as f:
  #          kotert = next(f)
  #         for l in f:
   #             exal = l.split(',')
  #              if int(exal[0]) == int(self.student_ids):
                    
                   



 
               



def main() -> int:
    app = QApplication(sys.argv)
    stylesheet_path = Path(__file__).with_name("ex1.qss")
    app.setStyleSheet(stylesheet_path.read_text(encoding="utf-8"))

    window = GradeManagerWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
