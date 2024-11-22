import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt6.QtGui import QFont
from fractions import Fraction

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set up the main layout
        self.setWindowTitle("Калькулятор с дробями")
        self.setGeometry(100, 100, 400, 600)
        self.layout = QVBoxLayout()

        # Input field
        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Arial", 20))
        self.layout.addWidget(self.input_field)

        # Grid layout for buttons
        self.grid_layout = QGridLayout()
        self.create_buttons()
        self.layout.addLayout(self.grid_layout)

        self.setLayout(self.layout)

    def create_buttons(self):
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('+', 3, 3),
            ('(', 4, 0), (')', 4, 1), ('=', 4, 2),
        ]

        for btn_text, row, col in buttons:
            button = QPushButton(btn_text)
            button.setFont(QFont("Arial", 18))
            button.clicked.connect(lambda checked, text=btn_text: self.on_button_click(text))
            self.grid_layout.addWidget(button, row, col)

    def on_button_click(self, text):
        if text == "C":
            self.input_field.clear()
        elif text == "=":
            self.calculate()
        else:
            self.input_field.setText(self.input_field.text() + text)

    def calculate(self):
        try:
            # Replace fractions in the input with Python Fraction objects
            expression = self.input_field.text()

            # Tokenize and replace fractions
            tokens = expression.split()
            for i, token in enumerate(tokens):
                if '/' in token and len(token.split('/')) == 2:
                    numerator, denominator = token.split('/')
                    tokens[i] = f"Fraction({numerator}, {denominator})"

            # Reconstruct the expression and evaluate it
            expression = ' '.join(tokens)
            result = eval(expression, {"Fraction": Fraction})
            self.input_field.setText(str(result))
        except Exception as e:
            self.input_field.setText("Ошибка")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
