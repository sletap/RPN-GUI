from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PySide2.QtWidgets import *
from PySide2 import QtGui
import sys
import rpn

class RPNGUI(QWidget):
  def __init__(self, parent = None):
    super(RPNGUI, self).__init__(parent)
  
    layout = QFormLayout()

    self.le1 = QLineEdit()
    self.btn1 = QPushButton("Calculate")
    layout.addRow(self.le1, self.btn1)
    self.end = QPushButton("End")
    layout.addRow(self.end)

    self.le1.returnPressed.connect(self.btn1.click)
    self.btn1.clicked.connect(self.rpnResult)
    self.end.clicked.connect(self.endCalculator)

    self.setLayout(layout)
    self.setWindowTitle("RPN Calculator")
					
  def rpnResult(self):
    text = self.le1.text()
    # print(text)
    try:
      result = rpn.calculate(text)
      # print(result)
      # print()
      self.le1.setText(str(result))
    except:
      pass

  def endCalculator(self):
    sys.exit()
    
if __name__ == '__main__':
  app = QApplication(sys.argv)
  calculator = RPNGUI()
  calculator.show()
  sys.exit(app.exec_())
