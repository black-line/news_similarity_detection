import sys
import traceback
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QStackedWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QProcess, QThread, QThreadPool, QObject, pyqtSignal, pyqtSlot, QRunnable
from ui_MainWindows import Ui_MainWindow
from exceptUI import myGoose, post_crawl, check_kw, MySimHash
import jieba.analyse
import logging
import time

logger = logging.getLogger('finalwr_logger')
import subprocess


class WorkerSignals(QObject):
    started = pyqtSignal()
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            self.signals.started.emit()
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


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
        if self.stackedWidget.currentIndex() == 0:
            self.simiBtn.setStyleSheet("""
                                    color: #fff;
                                    text-decoration: none;
                                    background-color: #28a745;
                                    border-color:#28a745;
                                    text-decoration: none;""")
        elif self.stackedWidget.currentIndex() == 1:
            self.kwBtn.setStyleSheet("""
                                    color: #fff;
                                    text-decoration: none;
                                    background-color: #28a745;
                                    border-color:#28a745;
                                    text-decoration: none;""")
        else:
            self.settingsBtn.setStyleSheet("""
                                    color: #fff;
                                    text-decoration: none;
                                    background-color: #28a745;
                                    border-color:#28a745;
                                    text-decoration: none;""")
        # Connect up the buttons.
        self.url1CrawlBtn.clicked.connect(self.url1CrawlBtn_on_click)
        self.url2CrawlBtn.clicked.connect(self.url2CrawlBtn_on_click)
        self.detectBtn.clicked.connect(self.detectBtn_on_click)
        # self.simiBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        # self.kwBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        # self.settingsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        self.simiBtn.clicked.connect(lambda: self.from_to(0, self.simiBtn))
        self.kwBtn.clicked.connect(lambda: self.from_to(1, self.kwBtn))
        self.settingsBtn.clicked.connect(lambda: self.from_to(2, self.settingsBtn))
        self.kwDetectBtn.clicked.connect(self.kwDetectBtn_on_click)
        self.getlistBtn.clicked.connect(self.getlistBtn_on_click)

        self.searchBtn.clicked.connect(self.searchBtn_on_click)
        self.closeSearchBtn.clicked.connect(self.closeSearchBtn_on_click)

        self.mpComfirmBtn.clicked.connect(self.mpComfirmBtn_on_click)

        # QProcess object for external app
        self.process = QProcess(self)
        # QProcess emits `readyRead` when there is data to be read
        self.process.readyRead.connect(self.dataReady)

        # Just to prevent accidentally running multiple times
        # Disable the button when process starts, and enable it when it finishes
        self.process.started.connect(lambda: self.searchBtn.setEnabled(False))
        self.process.finished.connect(lambda: self.searchBtn.setEnabled(True))

        self.coll_name = None


        output = subprocess.Popen(["sed -n '74p' ../news_spider/settings.py"], stdout=subprocess.PIPE,
                                  shell=True).communicate()
        self.SERVERTEXT = output[0].decode('utf-8')
        output = subprocess.Popen(["sed -n '75p' ../news_spider/settings.py"], stdout=subprocess.PIPE,
                                  shell=True).communicate()
        self.PORTTEXT = output[0].decode('utf-8')
        self.configList.setText(self.SERVERTEXT+self.PORTTEXT)
        self.PORT = self.PORTTEXT.split('=')[1]


        # self.threadpool = QThreadPool()
        # print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def mpComfirmBtn_on_click(self):
        mpValue = self.mpValue.text()
        print(mpValue)
        if mpValue:
            self.process.start('sed',
                               ['-i', 's/^MONGODB_PORT=.*/MONGODB_PORT={0}/'.format(mpValue),
                                '../news_spider/settings.py'])
            output = subprocess.Popen(["sed -n '74p' ../news_spider/settings.py"], stdout=subprocess.PIPE,
                                      shell=True).communicate()
            self.SERVERTEXT = output[0].decode('utf-8')
            output = subprocess.Popen(["sed -n '75p' ../news_spider/settings.py"], stdout=subprocess.PIPE,
                                      shell=True).communicate()
            self.PORTTEXT = output[0].decode('utf-8')
            self.configList.clear()
            self.configList.setText(self.SERVERTEXT + self.PORTTEXT)
            self.PORT = self.PORTTEXT.split('=')[1]

    def from_to(self, to, toBtn):
        if self.stackedWidget.currentIndex() == to:
            pass
        else:
            if self.stackedWidget.currentIndex() == 0:
                self.simiBtn.setStyleSheet("""""")
            elif self.stackedWidget.currentIndex() == 1:
                self.kwBtn.setStyleSheet("""""")
            else:
                self.settingsBtn.setStyleSheet("""""")
            self.stackedWidget.setCurrentIndex(to)
            toBtn.setStyleSheet(""" color: #fff;
                                     text-decoration: none;
                                     background-color: #28a745;
                                     border-color:#28a745;
                                     text-decoration: none;
                                 """)

    # def closeStatBtn_on_click(self):
    #     print('stopStat button clicked')
    #     self.statBtn.setEnabled(True)
    #     print(self.p.returncode)
    #     # if self.process.isOpen():
    #     #     self.process.close()
    #     #     print('close process')
    #
    # def statBtn_on_click(self):
    #     print('stat button clicked')
    #     self.statBtn.setEnabled(False)
    #     self.output.clear()
    #     # self.process.start('ping', ['127.0.0.1'])
    #     self.p = subprocess.Popen("scrapy crawl news_spider", cwd='/home/watmel/PycharmProjects/news_similarity_detection/nnorder/news_spider/news_spider/spiders',shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #     cursor = self.output.textCursor()
    #     for line in self.p.stdout.readlines():
    #         cursor.insertText(str(line, 'utf-8'))
    #     if self.p.returncode != 0:
    #         cursor.insertText("error")

    def closeSearchBtn_on_click(self):
        print('stopStat button clicked')
        if self.process.isOpen():
            self.process.close()
            print('close process')

    # def execute_this_fn(self):
    #     pc = post_crawl()
    #     tag_rank = pc.get_tag_rank()
    #     return tag_rank
    def print_output(self, s):
        tag_to_str = """<table><tr><td>{0}</td><td>{1}</td></tr>""".format('关键词', '热度值')
        for t in s:
            tag_to_str += '<tr><td><b>{0}:</b></td><td>{1}</td></tr>'.format(t['_id'], t['value'])
        tag_to_str += """</table>"""
        self.result.setText(tag_to_str)

    def thread_start(self):
        self.statBtn.setEnabled(False)
        print("THREAD START!")

    def thread_complete(self):
        self.statBtn.setEnabled(True)
        print("THREAD COMPLETE!")

    def searchBtn_on_click(self):
        # worker = Worker(self.execute_this_fn)
        # worker.signals.started.connect(self.thread_start)
        # worker.signals.result.connect(self.print_output)
        # worker.signals.finished.connect(self.thread_complete)
        # self.threadpool.start(worker)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        # self.process.start('ping', ['127.0.0.1'])
        kw_urlstyle = self.keyword.text()
        print(kw_urlstyle)
        if kw_urlstyle:
            self.output.clear()
            ck = check_kw(kw_urlstyle, self.PORT)
            flag, coll_name = ck.is_crawled()
            self.coll_name = coll_name
            if not flag:
                self.process.start('sed', ['-i', 's/^\s*kw=".*"/    kw="{0}"/'.format(kw_urlstyle),
                                           '../news_spider/spiders/news_spider.py'])

                self.process.waitForFinished(10)
                # self.process.start('sed',['-i','s/^MONGODB_COLLECTION=".*"/MONGODB_COLLECTION="{0}"/'.format(self.coll_name),'../news_spider/spiders/news_spider.py'])
                self.process.start('sed',
                                   ['-i', 's/^MONGODB_COLLECTION=".*"/MONGODB_COLLECTION="{0}"/'.format(self.coll_name),
                                    '../news_spider/settings.py'])
                self.process.waitForFinished(10)

                self.process.start('scrapy crawl news_spider')
            else:
                self.output.setPlainText('该关键词已抓取,可以直接点击获取列表按钮')

        else:
            pass

    def getlistBtn_on_click(self):
        pc = post_crawl(self.coll_name, self.PORT)
        title_list = pc.get_title_list()
        print("title_list:" + str(title_list))
        self.leftnews.addItems(title_list)
        self.rightnews.addItems(title_list)
        self.leftnews.activated.connect(self.left_combox_on_activate)
        self.rightnews.activated.connect(self.right_combox_on_activate)

    def kwDetectBtn_on_click(self):
        text1 = self.leftnewsContent.toPlainText()
        text2 = self.rightnewsContent.toPlainText()
        if text1 and text2:
            s1, t1 = self.get_simhash(text=text1)
            s2, t2 = self.get_simhash(text=text2)
            dis = self.get_distance(s1, s2)
            self.searchDistance.setText('{0}%, 在32位哈希值有{1}位不同'.format(str((1 - dis / 32) * 100), dis.__str__()))

    def left_combox_on_activate(self):
        title = self.leftnews.currentText()
        pc = post_crawl(self.coll_name, self.PORT)
        text = pc.get_text_by_title(title)
        self.leftnewsContent.setText(text)

    def right_combox_on_activate(self):
        title = self.rightnews.currentText()
        pc = post_crawl(self.coll_name, self.PORT)
        text = pc.get_text_by_title(title)
        self.rightnewsContent.setText(text)

    def dataReady(self):
        cursor = self.output.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(str(self.process.readAll(), 'utf-8'))
        self.output.ensureCursorVisible()

    def url1CrawlBtn_on_click(self):
        # print('url1CrawlBtn clicked')
        self.url1.setText('http://news.sina.com.cn/o/2018-05-16/doc-ihapkuvm6910260.shtml')
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
        self.url2.setText('http://finance.ifeng.com/a/20180515/16279179_0.shtml')
        if self.url2.text():
            clean_text, title = myGoose(url=self.url2.text()).get_cleaned_text()
            # clean_text = '123'
            if clean_text:
                self.news2.setPlainText(clean_text)
                self.title2.setText(title)
            else:
                self.news2.setPlainText(self.crawlNone)

    def tag_to_str(self, tag):
        # tag_to_str=''
        # for t in tag:
        #     tag_to_str+='<b>{0}</b>: {1}<br/>'.format(t[0],t[1])
        tag_to_str = """<table><tr><td>{0}</td><td>{1}</td></tr>""".format('关键词', '权重')
        for t in tag:
            tag_to_str += '<tr><td><b>{0}:</b></td><td>{1}</td></tr>'.format(t[0], t[1])
        tag_to_str += """</table>"""
        return tag_to_str

    def detectBtn_on_click(self):
        print('detectBtn clicked')
        text1 = self.news1.toPlainText()
        text2 = self.news2.toPlainText()
        if text1 and text2:
            s1, t1 = self.get_simhash(text=text1)
            s2, t2 = self.get_simhash(text=text2)
            self.tag1.setText(self.tag_to_str(t1))
            self.tag2.setText(self.tag_to_str(t2))
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
