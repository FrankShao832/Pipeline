
from PySide2.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel
)


class MainWindow(QMainWindow):
    """The main window of pipeline launcher.

    Args:
        QMainWindow (_type_): _description_
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("Y Pipeline")
        self.resize(800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        label = QLabel("Y Pipeline ready")
        layout.addWidget(label)


if __name__ == "__main__":
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
