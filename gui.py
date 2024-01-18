import logging
import sys
import threading
from pathlib import Path

from PySide6.QtCore import QObject, Signal, QUrl, Property, Slot, QtMsgType, qInstallMessageHandler
from PySide6.QtGui import QImage, QClipboard, QIcon
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication

from ligmage import Ligmage


class Progress(QObject):

    def __init__(self, parent=None):
        super(Progress, self).__init__(parent)


class Backend(QObject):
    file_url_Changed = Signal(QUrl)

    def __init__(self, parent=None):
        super(Backend, self).__init__(parent)
        self.ligmage = Ligmage()
        self._file_url = QUrl()
        self.thread = None
        self.chemin = ""
        self._recursive = True

        logging.basicConfig(level=logging.CRITICAL)

    @Slot(str)
    def run_ligmage(self, recherche):
        self.chemin = self._file_url.toLocalFile()
        self.ligmage.set_chemin(self.chemin, self.recursive)
        self.thread = threading.Thread(target=self.ligmage.ligmage, args=(recherche,))
        self.thread.start()

    @Slot(str)
    def copy_image(self, image_path):
        image = QImage(image_path)
        clipboard = QApplication.clipboard()
        clipboard.setImage(image, QClipboard.Clipboard)
        # clipboard.setText("youpi", mode=QClipboard.Clipboard)

    def get_file_url(self):
        return self._file_url

    def set_file_url(self, file_url):
        if self._file_url != file_url:
            self._file_url = file_url
            self.file_url_Changed.emit(self._file_url)

    def get_recursive(self):
        return self._recursive

    def set_recursive(self, rec):
        self._recursive = rec


    file_url = Property(QUrl, fget=get_file_url, fset=set_file_url, notify=file_url_Changed)
    recursive = Property(bool, fget=get_recursive, fset=set_recursive)


@Slot(QUrl)
def on_file_url_changed(file_url):
    print(file_url.toLocalFile())


# Custom message handler to redirect QML console.log messages to Python print
def qmlMessageHandler(msg_type, context, msg):
    if msg_type == QtMsgType.QtDebugMsg:
        prefix = "Debug"
    elif msg_type == QtMsgType.QtInfoMsg:
        prefix = "Info"
    elif msg_type == QtMsgType.QtWarningMsg:
        prefix = "Warning"
    elif msg_type == QtMsgType.QtCriticalMsg:
        prefix = "Critical"
    elif msg_type == QtMsgType.QtFatalMsg:
        prefix = "Fatal"
    else:
        prefix = "Unknown"

    print(f"{prefix}: {msg}")


if __name__ == "__main__":
    # logging.getLogger("PIL.TiffImagePlugin").setLevel(logging.CRITICAL)

    app = QApplication(sys.argv)

    my_icon = QIcon()
    my_icon.addFile('madman.png')

    app.setWindowIcon(my_icon)


# Install the custom message handler
    qInstallMessageHandler(qmlMessageHandler)
    engine = QQmlApplicationEngine()

    qml_file = Path(__file__).parent / 'view.qml'

    backend = Backend()
    backend.file_url_Changed.connect(on_file_url_changed)

    engine.rootContext().setContextProperty("backend", backend)
    engine.rootContext().setContextProperty("ligmage", backend.ligmage)

    engine.load(qml_file)

    # progressText = engine.rootObjects()[0].findChild(QObject, "progressText")
    # engine.rootObjects()[0].progress_changed.connect(progressText.setText)

    if not engine.rootObjects():
        sys.exit(-1)
    # del engine
    sys.exit(app.exec())
