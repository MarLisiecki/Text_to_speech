# This Python file uses the following encoding: utf-8
import sys
import os
import subprocess
import sys
from run import run

try:
    from PySide2.QtGui import QGuiApplication
    from PySide2.QtQml import QQmlApplicationEngine

except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'PySide2'])

finally:
    from PySide2.QtGui import QGuiApplication
    from PySide2.QtQml import QQmlApplicationEngine
    from PySide2.QtCore import QObject, Slot, Signal
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'google-cloud'])



class main_window(QObject):
    def __init__(self):
        QObject.__init__(self)

    getText = Signal(str)

    @Slot(str)
    def genText(self, text):
        self.getText.emit(text)
        run.run(text)

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    main = main_window()
    engine.rootContext().setContextProperty("backend", main)



    engine.load(os.path.join(os.path.dirname(__file__), "qml/main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
