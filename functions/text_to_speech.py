# -------------------------------------------------------------------
import pyttsx3


class TTS:
    __engine = None
    __ui = None

    def __init__(self, *args, **kwargs):
        if str(type(args[0])) == "<class 'view.Ui_Dialog'>" :
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 140)
            self.ui = args[0]

    def speech(self, text):
        self.ui.pushButton.setDisabled(True)
        self.engine.say(text)
        self.engine.runAndWait()
        self.ui.pushButton.setDisabled(False)

    def stop(self):
        pass
# -------------------------------------------------------------------
