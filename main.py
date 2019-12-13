
import sys, platform
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)

    if len(sys.argv) != 2:
        # Avaliable track: line and circle
        print("Usage: %s <line | circle>" % sys.argv[0])
        exit()

    if sys[1].lower() == "line":
        from FollowLine import MainWindow
    elif sys[1].lower() == "circle":
        from FollowCircle import MainWindow

    # 2018.2.17 Enable high dpi pixmaps to show high definition icons for MacOsX
    if platform.system() == "Darwin":
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True);
        QApplication.setAttribute(Qt.AA_DontShowIconsInMenus, True)

    view = MainWindow()
    view.show()

    # 2018.2.17 Center main window
    # frameGeometry() can only return the right geometry after the window has shown up
    currentGeometry = view.frameGeometry()
    screenCenter = QDesktopWidget().availableGeometry().center()
    currentGeometry.moveCenter(screenCenter)
    view.move(currentGeometry.topLeft())

    sys.exit(app.exec_())
