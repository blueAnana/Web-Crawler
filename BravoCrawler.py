import urllib2
import re


class Crawler:

    def __init__(self):
        self.url = 'http://www.mzitu.com/all'

    def climb(self):
        # Get url and name of all pictures
        regex = ': <a href="(http://www.mzitu.com/\d*?)" target="_blank">(.*?)</a>'
        page = self.getPage(self.url)
        items = self.getPatternItems(page, regex)
        for item in items:
            # print item[0], item[1]
            # Get pictures
            regex = '<img src="(.*?)" alt="'
            picPage = self.getPage(item[0])
            pics = self.getPatternItems(picPage, regex)
            print pics
            for pic in pics:
                self.save(pic, item[1])
            #     print pic

    def getPage(self, url):
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            page = response.read().decode('utf-8')
            return page
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

    def getPatternItems(self, page, regex):
        pattern = re.compile(regex, re.S)
        items = re.findall(pattern, page)
        return items

    def save(self, url, name):
        name = name.replace('?', '').strip()
        name = name.replace('/', '').strip()
        fname = 'E:\Github\Web Crawler\pictures\\' + name + '.jpg'
        f = open(fname, 'ab')
        pic = urllib2.urlopen(url).read()
        f.write(pic)
        f.close()


crawler = Crawler()
crawler.climb()


