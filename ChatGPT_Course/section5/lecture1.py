import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Temperature Converter')
        self.setGeometry(100, 100, 300, 150)

        # Create layout
        vbox = QVBoxLayout()

        # Input fields and labels
        self.celsius_label = QLabel('Celsius:', self)
        self.celsius_input = QLineEdit(self)

        self.fahrenheit_label = QLabel('Fahrenheit:', self)
        self.fahrenheit_input = QLineEdit(self)

        # Buttons
        self.c_to_f_button = QPushButton('Celsius to Fahrenheit', self)
        self.c_to_f_button.clicked.connect(self.celsius_to_fahrenheit)

        self.f_to_c_button = QPushButton('Fahrenheit to Celsius', self)
        self.f_to_c_button.clicked.connect(self.fahrenheit_to_celsius)

        # Add widgets to layout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.celsius_label)
        hbox1.addWidget(self.celsius_input)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.fahrenheit_label)
        hbox2.addWidget(self.fahrenheit_input)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.c_to_f_button)
        hbox3.addWidget(self.f_to_c_button)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)

    def celsius_to_fahrenheit(self):
        try:
            celsius = float(self.celsius_input.text())
            fahrenheit = celsius * 9/5 + 32
            self.fahrenheit_input.setText(f'{fahrenheit:.2f}')
        except ValueError:
            self.show_error_message('Please enter a valid number for Celsius.')

    def fahrenheit_to_celsius(self):
        try:
            fahrenheit = float(self.fahrenheit_input.text())
            celsius = (fahrenheit - 32) * 5/9
            self.celsius_input.setText(f'{celsius:.2f}')
        except ValueError:
            self.show_error_message('Please enter a valid number for Fahrenheit.')

    def show_error_message(self, message):
        error_msg = QMessageBox()
        error_msg.setIcon(QMessageBox.Critical)
        error_msg.setWindowTitle('Error')
        error_msg.setText(message)
        error_msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TemperatureConverter()
    ex.show()
    sys.exit(app.exec_())
