'''djbrowser.py - a simple web browser using the PyQt5 toolkit'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    '''Main Window Class'''
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("DjBrowser")
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.show()

        navigation_bar = QToolBar("Navigation")
        self.addToolBar(navigation_bar)

        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navigation_bar.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navigation_bar.addAction(forward_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navigation_bar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navigation_bar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navigation_bar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)
    
    def navigate_home(self):
        '''navigate to home'''
        self.browser.setUrl(QUrl("http://google.com"))

    def navigate_to_url(self):
        '''navigate to url'''
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    
    def update_url(self, q):
        '''update url'''
        self.url_bar.setText(q.toString())
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName("DjBrowser")
    window = MainWindow()
    app.exec_()
