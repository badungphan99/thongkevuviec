import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar, QStatusBar, QAction, QVBoxLayout, QWidget, QSplitter, \
    QFrame, QComboBox, QGridLayout, QTableWidget, QListWidget, QTableWidgetItem, QPushButton, QGroupBox, QFormLayout, QLineEdit, QSpinBox, QHBoxLayout, QPlainTextEdit
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from app.controller import *

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My Awesome App")
        self.setWindowState(Qt.WindowMaximized)
        main_layout = QGridLayout()



        top = QGroupBox("Nhap cac thong tin")
        top_layout = QVBoxLayout()

        #Button
        save_button = QPushButton("Save")

        cancel_button = QPushButton("Cancel")

        button_layout = QHBoxLayout()
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)

        form_layout = QFormLayout()

        form_top_layout = QGridLayout()


        line_edit_thoi_gian = QLineEdit()
        line_edit_dia_diem = QLineEdit()

        combobox_linh_vuc = QComboBox()

        container_time = QWidget()
        form_thoi_gian_layout = QHBoxLayout()
        form_thoi_gian_layout.addWidget(QLabel("Thời gian: "))
        form_thoi_gian_layout.addWidget(line_edit_thoi_gian)
        container_time.setLayout(form_thoi_gian_layout)


        container_location = QWidget()
        form_dia_diem_layout = QHBoxLayout()
        form_dia_diem_layout.addWidget(QLabel("Địa điểm: "))
        form_dia_diem_layout.addWidget(line_edit_dia_diem)
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

        form_layout.addRow(form_top_layout)
        form_layout.addRow(QLabel("Nguyen nhan"))
        form_layout.addRow(QPlainTextEdit())
        form_layout.addRow(QLabel("Hau qua"))
        form_layout.addRow(QPlainTextEdit())
        form_layout.addRow(QLabel("Bien phap ket qua xu ly"))
        form_layout.addRow(QPlainTextEdit())


        top_layout.addLayout(form_layout)
        top_layout.addLayout(button_layout)

        top.setLayout(top_layout)

        # Phan layout hien thi thong tin o duoi
        bottom = QGroupBox()
        bottom_layout = QVBoxLayout()

        table_data = QTableWidget()

        headers = ["id", "time", "location", "result", "reason", "solution", "fields", "time modify"]
        incidents = get_all_incident()

        table_data.setColumnCount(len(headers))
        table_data.setHorizontalHeaderLabels(headers)
        table_data.setRowCount(len(incidents))

        for i in range(0,len(incidents),1):
            table_data.setItem(i, 0, QTableWidgetItem(str(incidents[i].id)))
            table_data.setItem(i, 1, QTableWidgetItem(str(incidents[i].time)))
            table_data.setItem(i, 2, QTableWidgetItem(incidents[i].location))
            table_data.setItem(i, 3, QTableWidgetItem(incidents[i].result))
            table_data.setItem(i, 4, QTableWidgetItem(incidents[i].reason))
            table_data.setItem(i, 5, QTableWidgetItem(incidents[i].solution))
            table_data.setItem(i, 6, QTableWidgetItem(incidents[i].fields))
            table_data.setItem(i, 7, QTableWidgetItem(str(incidents[i].time)))

        bottom_layout.addWidget(table_data)
        bottom.setLayout(bottom_layout)

        # Ket thuc phan danh cho hien thi layout

        main_layout.addWidget(top, 1, 0)
        main_layout.addWidget(bottom, 2, 0)
        main_layout.setRowStretch(1, 1)
        main_layout.setRowStretch(2, 1)
        widget = QWidget()
        widget.setLayout(main_layout)


        self.setCentralWidget(widget)
