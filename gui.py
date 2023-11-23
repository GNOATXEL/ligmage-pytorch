import logging
import sys
import threading
from pathlib import Path

from PySide6.QtCore import QObject, Signal, QUrl, Property, Slot
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

        logging.basicConfig(level=logging.CRITICAL)

    @Slot()
    def run_ligmage(self):
        self.thread = threading.Thread(target=self.ligmage.ligmage, args=(self._file_url.toLocalFile(),))
        self.thread.start()

    def get_file_url(self):
        return self._file_url

    def set_file_url(self, file_url):
        if self._file_url != file_url:
            self._file_url = file_url
            self.file_url_Changed.emit(self._file_url)

    file_url = Property(QUrl, fget=get_file_url, fset=set_file_url, notify=file_url_Changed)


@Slot(QUrl)
def on_file_url_changed(file_url):
    print(file_url.toLocalFile())


if __name__ == "__main__":
    # logging.getLogger("PIL.TiffImagePlugin").setLevel(logging.CRITICAL)

    app = QApplication(sys.argv)
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
