# from nba_html import  nbaHtml
# from nba_url import  nbaUrl
# from nba_parse import HtmlParse

import nba.nba_url as url
import nba.nba_html as html
import nba.nba_parse as parse

class nbaMain :

    def __init__(self):
        # self.urlmanage = url.nbaUrl()
        self.html = html.nbaHtml()
        self.myParse = parse.HtmlParse()
    def do(self, url):
        content = self.html.getContent(url)
        news = self.myParse.parse(url,content) #所有球员的详细资料的地址
        for i in news:
            print(i)
        mylist= self.myParse.getAllPlayers(news)
        print(len(mylist))
        for j in mylist:
            print(j)


if __name__ == "__main__" :
    url = "http://stat-nba.com/playerList.php"
    nba = nbaMain()
    nba.do(url)


