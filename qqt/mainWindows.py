import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QStackedWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QProcess
from ui_MainWindows import Ui_MainWindow
from goo import myGoose
import jieba.analyse
import logging

logger = logging.getLogger('finalwr_logger')
from MySimHash import MySimHash


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # Make some local modifications.
        # self.colorDepthCombo.addItem("2 colors (1 bit per pixel)")
        # self.setWindowIcon(QIcon('images/icons8-google-news-24.png'))
        self.crawlNone = 'Nothing had been crawled, try another url.'
        self.exit.triggered.connect(self.close)
        # Connect up the buttons.
        # self.okButton.clicked.connect(self.accept)
        # self.cancelButton.clicked.connect(self.reject)
        self.url1CrawlBtn.clicked.connect(self.url1CrawlBtn_on_click)
        self.url2CrawlBtn.clicked.connect(self.url2CrawlBtn_on_click)
        self.detectBtn.clicked.connect(self.detectBtn_on_click)
        self.simiBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.kwBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.settingsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        self.statBtn.clicked.connect(self.statBtn_on_click)
        self.closeStatBtn.clicked.connect(self.closeStatBtn_on_click)
        # QProcess object for external app
        self.process = QProcess(self)
        # QProcess emits `readyRead` when there is data to be read
        self.process.readyRead.connect(self.dataReady)

        # Just to prevent accidentally running multiple times
        # Disable the button when process starts, and enable it when it finishes
        self.process.started.connect(lambda: self.statBtn.setEnabled(False))
        self.process.finished.connect(lambda: self.statBtn.setEnabled(True))


    def closeStatBtn_on_click(self):
        print('stopStat button clicked')
        if self.process.isOpen():
            self.process.close()
            print('close process')

    def statBtn_on_click(self):
        print('stat button clicked')
        self.output.clear()
        self.process.start('ping', ['127.0.0.1'])

    def dataReady(self):
        cursor = self.output.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(str(self.process.readAll(), 'utf-8'))
        self.output.ensureCursorVisible()

    def url1CrawlBtn_on_click(self):
        # print('url1CrawlBtn clicked')
        # self.url1.setText('http://news.sina.com.cn/o/2018-05-16/doc-ihapkuvm6910260.shtml')
        if self.url1.text():
            clean_text, title = myGoose(url=self.url1.text()).get_cleaned_text()
            # clean_text = '123'
            if clean_text:
                self.news1.setPlainText(clean_text)
                self.title1.setText(title)
            else:
                self.news1.setPlainText(self.crawlNone)

    def url2CrawlBtn_on_click(self):
        # print('url2CrawlBtn clicked')
        # self.url2.setText('http://finance.ifeng.com/a/20180515/16279179_0.shtml')
        if self.url2.text():
            clean_text, title = myGoose(url=self.url2.text()).get_cleaned_text()
            # clean_text = '123'
            if clean_text:
                self.news2.setPlainText(clean_text)
                self.title2.setText(title)
            else:
                self.news2.setPlainText(self.crawlNone)

    def detectBtn_on_click(self):
        print('detectBtn clicked')
        s1, p1 = self.get_simhash(text=self.news1.toPlainText())
        s2, p2 = self.get_simhash(text=self.news2.toPlainText())
        self.tag1.setPlainText(p1.__str__())
        self.tag2.setPlainText(p2.__str__())
        dis = self.get_distance(s1, s2)
        self.distance.setText('{0}%, 在32位哈希值有{1}位不同'.format(str((1 - dis / 32) * 100), dis.__str__()))

    def get_simhash(self, text):
        pair = jieba.analyse.extract_tags(text, topK=20, withWeight=True)
        return MySimHash().get_simhash(pair), pair

    def get_distance(self, s1, s2):
        return MySimHash().get_distance(s1, s2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
