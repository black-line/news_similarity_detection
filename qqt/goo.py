from goose3 import Goose
from goose3.configuration import Configuration
from goose3.text import StopWordsChinese

class myGoose(object):
    def __init__(self, url):
        self.url = url
        self.cleaned_text = None
        self.config = Configuration()
        self.config.browser_user_agent = 'Mozilla 5.0'
        self.config.stopwords_class = StopWordsChinese

    def get_cleaned_text(self):
        with Goose(config=self.config, ) as g:
            article = g.extract(url=self.url)
            self.cleaned_text = article.cleaned_text
            self.title = article.title
        return self.cleaned_text, self.title

# mg = myGoose(url='http://news.sina.com.cn/o/2018-05-16/doc-ihapkuvm6910260.shtml')
# print(mg.get_cleaned_text())