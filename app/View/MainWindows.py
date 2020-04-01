import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QStatusBar, QAction, QVBoxLayout, QWidget, QSplitter, \
    QFrame, QComboBox, QGridLayout, QTableWidget, QListWidget, QTableWidgetItem, QPushButton, QGroupBox, QFormLayout, QLineEdit, \
    QSpinBox, QHBoxLayout, QPlainTextEdit, QPlainTextDocumentLayout
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from app.controller import *

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My Awesome App")
        self.setWindowState(Qt.WindowMaximized)
        self.main_layout = QGridLayout()

        self.top_graph()
        self.bottom_graph()

        self.main_layout.addWidget(self.top, 1, 0)
        self.main_layout.addWidget(self.bottom, 2, 0)
        self.main_layout.setRowStretch(1, 1)
        self.main_layout.setRowStretch(2, 1)
        widget = QWidget()
        widget.setLayout(self.main_layout)


        self.setCentralWidget(widget)

    def top_graph(self):
        self.top = QGroupBox("Nhap cac thong tin")
        top_layout = QVBoxLayout()

        # Button
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_click)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.cancel_click)

        button_layout = QHBoxLayout()
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)

        form_layout = QFormLayout()

        form_top_layout = QGridLayout()

        self.line_edit_thoi_gian = QLineEdit()
        self.line_edit_dia_diem = QLineEdit()

        combobox_linh_vuc = QComboBox()

        container_time = QWidget()
        form_thoi_gian_layout = QHBoxLayout()
        form_thoi_gian_layout.addWidget(QLabel("Thời gian: "))
        form_thoi_gian_layout.addWidget(self.line_edit_thoi_gian)
        container_time.setLayout(form_thoi_gian_layout)

        container_location = QWidget()
        form_dia_diem_layout = QHBoxLayout()
        form_dia_diem_layout.addWidget(QLabel("Địa điểm: "))
        form_dia_diem_layout.addWidget(self.line_edit_dia_diem)
        container_location.setLayout(form_dia_diem_layout)

        container_field = QWidget()
        form_linh_vuc_layout = QHBoxLayout()
        form_linh_vuc_layout.addWidget(QLabel("Lĩnh Vực: "))
        form_linh_vuc_layout.addWidget(combobox_linh_vuc)
        container_field.setLayout(form_linh_vuc_layout)

        form_top_layout.addWidget(container_time, 1, 0)
        form_top_layout.addWidget(container_location, 1, 1)
        form_top_layout.addWidget(container_field, 1, 2)

        form_top_layout.setColumnStretch(0, 1)
        form_top_layout.setColumnStretch(1, 1)
        form_top_layout.setColumnStretch(2, 1)

        container = QWidget()
        container.setLayout(form_top_layout)

        form_layout.addRow(container)

        self.plan_text_reason = QPlainTextEdit()
        self.plan_text_result = QPlainTextEdit()
        self.plan_text_solution = QPlainTextEdit()

        form_layout.addRow(form_top_layout)
        form_layout.addRow(QLabel("Nguyen nhan"))
        form_layout.addRow(self.plan_text_reason)
        form_layout.addRow(QLabel("Hau qua"))
        form_layout.addRow(self.plan_text_result)
        form_layout.addRow(QLabel("Bien phap ket qua xu ly"))
        form_layout.addRow(self.plan_text_solution)

        top_layout.addLayout(form_layout)
        top_layout.addLayout(button_layout)

        self.top.setLayout(top_layout)

    def bottom_graph(self):
        self.bottom = QGroupBox()
        bottom_layout = QVBoxLayout()

        table_data = QTableWidget()

        headers = ["id", "time", "location", "result", "reason", "solution", "fields", "time modify"]
        incidents = get_all_incident()

        table_data.setColumnCount(len(headers))
        table_data.setHorizontalHeaderLabels(headers)
        table_data.setRowCount(len(incidents))

        for i in range(0, len(incidents), 1):
            table_data.setItem(i, 0, QTableWidgetItem(str(incidents[i].id)))
            table_data.setItem(i, 1, QTableWidgetItem(str(incidents[i].time)))
            table_data.setItem(i, 2, QTableWidgetItem(incidents[i].location))
            table_data.setItem(i, 3, QTableWidgetItem(incidents[i].result))
            table_data.setItem(i, 4, QTableWidgetItem(incidents[i].reason))
            table_data.setItem(i, 5, QTableWidgetItem(incidents[i].solution))
            table_data.setItem(i, 6, QTableWidgetItem(incidents[i].fields))
            table_data.setItem(i, 7, QTableWidgetItem(str(incidents[i].time)))

        bottom_layout.addWidget(table_data)
        self.bottom.setLayout(bottom_layout)

    def save_click(self):
        time = self.line_edit_thoi_gian.text()
        location = self.line_edit_dia_diem.text()
        fields = "5"
        reason = self.plan_text_reason.toPlainText()
        result = self.plan_text_result.toPlainText()
        solution = self.plan_text_solution.toPlainText()

        if(time == "" or location == "" or fields == "" or reason == "" or result == "" or solution == ""):
            print("chuwa nhap du thong tin")
        else:
            insert_incident(location, result, reason, solution, fields)
            self.bottom_graph()
            self.main_layout.addWidget(self.bottom, 2, 0)
            self.cancel_click()

    def cancel_click(self):
        self.line_edit_thoi_gian.setText("")
        self.line_edit_dia_diem.setText("")
        self.plan_text_reason.setPlainText("")
        self.plan_text_result.setPlainText("")
        self.plan_text_solution.setPlainText("")