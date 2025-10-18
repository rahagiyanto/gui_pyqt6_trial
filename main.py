from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize application main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Example GUI component
        example_button = QPushButton('Pencett!')
        def on_button_click():
            print("beep")
        example_button.clicked.connect(on_button_click)

        self.setCentralWidget(example_button)

app = QApplication([])
window = MainWindow()
window.show() # Windows are hidden by default
app.exec() # Start the event loop