import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class ExcelViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Excel File Viewer')
        self.setGeometry(100, 100, 800, 600)
        
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        
        self.layout = QVBoxLayout(self.centralWidget)
        
        self.openButton = QPushButton('Browse Excel File')
        self.openButton.clicked.connect(self.openFileDialog)
        self.layout.addWidget(self.openButton)
        
        self.viewButton = QPushButton('View')
        self.viewButton.clicked.connect(self.viewExcelFile)
        self.layout.addWidget(self.viewButton)
        
        self.tableWidget = QTableWidget()
        self.layout.addWidget(self.tableWidget)
        
        self.filePath = None
    
    def openFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx *.xls);;All Files (*)", options=options)
        if fileName:
            self.filePath = fileName
    
    def viewExcelFile(self):
        if self.filePath:
            df = pd.read_excel(self.filePath)
            if not df.empty:
                self.tableWidget.setRowCount(df.shape[0])
                self.tableWidget.setColumnCount(df.shape[1])
                self.tableWidget.setHorizontalHeaderLabels(df.columns)
                
                for row in df.itertuples():
                    for col in range(df.shape[1]):
                        self.tableWidget.setItem(row.Index, col, QTableWidgetItem(str(row[col + 1])))
            else:
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(0)
        else:
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)
            self.tableWidget.setHorizontalHeaderLabels([])
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ExcelViewer()
    viewer.show()
    sys.exit(app.exec_())
