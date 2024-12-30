import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
label = QLabel("Hello, PyQt")
label.show()

print("Before event Loop")
app.exec_()
print("After event Loop")