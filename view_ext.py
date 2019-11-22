# pyuic5 -x view.ui -o view.py
from view import *
from functions.text_to_speech import TTS
import sys


def hello():
    print("Hello!")
    ui.textEdit.setText("Ciao a tutti")


def speech_button():
    text = ui.textEdit.toPlainText()
    if text is not '':
        ui.textEdit.clear()
        print('# ', text)
        # sp = TTS()
        sp.speech(text)


def test_engine():
    sp.isBusy()
    sp.stop()


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
print( str(type(ui)) == "<class 'view.Ui_Dialog'>" )
sp = TTS(ui)
ui.pushButton.clicked.connect(speech_button)

Dialog.show()
sys.exit(app.exec_())

#
# if __name__ == "__main__":
#     import sys
#
#     def hello():
#         print("Hello!")
#
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     ui.pushButton.clicked.connect(hello)
#
#     Dialog.show()
#     sys.exit(app.exec_())
