from PyQt5.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget, QGridLayout, QTableWidget, QTableWidgetItem, \
    QPushButton, QGroupBox, QLineEdit, QFileDialog
from PyQt5.QtCore import Qt
import datetime

from app.controller import *


class ExportWindows(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ExportWindows, self).__init__(*args, **kwargs)
        self.setWindowTitle("My Awesome App")
        self.setWindowState(Qt.WindowMaximized)
        self.main_layout = QVBoxLayout()

        self.top_graph()
        self.bottom_graph(True)

        self.main_layout.addWidget(self.top)
        self.main_layout.addWidget(self.bottom)
        # self.main_layout.setRowStretch(1, 1)
        # self.main_layout.setRowStretch(2, 1)
        widget = QWidget()
        widget.setLayout(self.main_layout)

        self.setCentralWidget(widget)

    def top_graph(self):
        self.top = QGroupBox()
        search_layout = QGridLayout()

        search_label = QLabel("                 Lĩnh vực")

        self.search_field = QLineEdit()

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_button_clicked)

        export_button = QPushButton("Export")
        export_button.clicked.connect(self.export_button_clicked)

        search_layout.addWidget(search_label , 1, 0)
        search_layout.addWidget(self.search_field, 1, 1)
        search_layout.addWidget(search_button, 1, 2)
        search_layout.addWidget(export_button, 1, 3)

        search_layout.setColumnStretch(0, 1)
        search_layout.setColumnStretch(1, 3)
        search_layout.setColumnStretch(2, 1)
        search_layout.setColumnStretch(3, 1)

        self.top.setLayout(search_layout)

    def bottom_graph(self, flag):
        self.bottom = QGroupBox()
        bottom_layout = QVBoxLayout()

        table_data = QTableWidget()

        headers = ["Id", "Thời gian", "Địa điểm", "Kết quả", "Lý do", "Giải pháp", "Lĩnh vực", "Thời gian chỉnh sửa"]
        if(flag):
            self.incidents = get_all_incident()

        table_data.setColumnCount(len(headers))
        table_data.setHorizontalHeaderLabels(headers)
        table_data.setRowCount(len(self.incidents))
        for i in range(0, len(self.incidents), 1):
            table_data.setItem(i, 0, QTableWidgetItem(str(self.incidents[i].id)))
            table_data.setItem(i, 1, QTableWidgetItem(str(self.incidents[i].time)))
            table_data.setItem(i, 2, QTableWidgetItem(self.incidents[i].location))
            table_data.setItem(i, 3, QTableWidgetItem(self.incidents[i].result))
            table_data.setItem(i, 4, QTableWidgetItem(self.incidents[i].reason))
            table_data.setItem(i, 5, QTableWidgetItem(self.incidents[i].solution))
            table_data.setItem(i, 6, QTableWidgetItem(self.incidents[i].fields))
            table_data.setItem(i, 7, QTableWidgetItem(str(self.incidents[i].time)))

        bottom_layout.addWidget(table_data)
        self.bottom.setLayout(bottom_layout)

    def search_button_clicked(self):
        self.main_layout.removeWidget(self.bottom)
        self.incidents = get_incident_field(self.search_field.text())
        self.bottom_graph(False)
        self.main_layout.addWidget(self.bottom)
    def export_button_clicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", datetime.datetime.now().strftime("%Y-%m-%d_%Hh%M")+".csv",
                                                  "All Files (*);;CSV Files (*.csv)", options=options)
        export(self.incidents, fileName)