#coding=UTF-8
import urllib2
import re
import sys
import threading
import globalvariety

class MovieTop250:        
          
    def getPage(i):
        try:
            
            start = i
            URL = 'http://movie.douban.com/top250?start=' + str(start)
            request = urllib2.Request(url = URL, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'})
            response = urllib2.urlopen(request)
            page = response.read().decode('utf-8')
            
            pageNum = (start + 25) / 25
            print '正在抓取第' + str(pageNum) + '页数据...' 
            
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print '抓取失败，具体原因：', e.reason
        
        pattern = re.compile(u'<li>.*?<div.*?class="item">.*?<div.*?class="pic">.*?'
                             + u'<em.*?class="">(.*?)</em>.*?'           # 排名
                             + u'<div.*?class="info">.*?<span.*?class="title">(.*?)</span>.*?'        # 电影名
                             + u'<div.*?class="bd">.*?<p.*?class="">.*?'
                             + u' (.*?)..*?'
                             + u'.*? (.*?)<br>'
                             + u'(.*?)&nbsp;/&nbsp;'      # 年份
                             + u'(.*?)&nbsp;/&nbsp;'      # 原产国
                             + u'(.*?)</p>'               # 类型
                             + u'.*?<div.*?class="star">.*?property="v:average">(.*?)</span>'   # 平均评分
                             + u'.*?<span>(.*?)人评价</span>.*?<p.*?class="quote">.*?'          # 评论数
                             + u'<span.*?class="inq">(.*?)</span>.*?</li>', re.S)                # 简评
                 
        
        movies = re.findall(pattern, page)
        for movie in movies:
            globalvariety.movieList.append([movie[0], movie[1],  movie[2], 
                    movie[3].lstrip(), movie[4].lstrip(), movie[5], movie[6].rstrip(),
                    movie[7], movie[8],movie[9]])
    
    threads = []#多线程就是用来同时执行多个功能函数，提高效率
    for i in range(0, 250, 25):
        t = threading.Thread(target=getPage, args = (i,))#第一个参数后面必须用逗号分隔，不然会被认为是非序列而出错
        threads.append(t)
    
    for i in range(0,10):
        threads[i].start()
 
    for i in range(0,10):
        threads[i].join()                 
    
    
    def writeTxt(self):
        
        filePath = 'E:/Python/movie_data/douban1.txt'  
        fileTop250 = open(filePath, 'w')
        
        try:
            
            for movie in globalvariety.movieList:
                fileTop250.write(movie[0] + '#')
                fileTop250.write(movie[1] + '#')
                fileTop250.write(movie[2] )
                fileTop250.write(movie[3] + '#')
                fileTop250.write(movie[4] + '#')
                fileTop250.write(movie[5] + '#')
                fileTop250.write(movie[6] + '#')
                fileTop250.write(movie[7] + '#')
                fileTop250.write(movie[8] + '#')
                fileTop250.write(movie[9] )
                fileTop250.write("\n")
            print '文件写入成功...'
        finally:
            fileTop250.close()
                     
    def main(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        print '正在从豆瓣电影Top250抓取数据...'
        #self.getMovie()
        self.writeTxt()
        print '抓取完毕...'
                 
DouBanSpider = MovieTop250()
DouBanSpider.main()

