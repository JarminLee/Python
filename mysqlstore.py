import pymysql
if __name__=="__main__":
    connect = pymysql.connect(      #连接数据库  
        user = "root",  
        password = "hust",  
        host = "127.0.0.1",  
        db = "douban",  
        port = 3307,  
        charset = ("utf8"),    #注意编码一定要设置，否则gbk你懂的  
        use_unicode=True,  
        )
    con = connect.cursor()    #设置游标  
    # con.execute('SET NAMES UTF8')  
    con.execute("drop database douban")       #以下7行表示删除原有的数据库和其中的表，新建数据库和表  
    con.execute("create database douban")  
    con.execute("use douban")                 #使用douban这个数据库  
    #con.execute("drop table if exists t_doubantop")  
    sql = "create table doubantop(num VARCHAR(200),name VARCHAR(400) NOT NULL,director_charactor VARCHAR(400),year VARCHAR(400), nation VARCHAR(100), type VARCHAR(100),score VARCHAR(20), people VARCHAR(400),remark VARCHAR(400)) DEFAULT CHARSET=utf8" 
    con.execute(sql)    #sql中的字符表示创建一个表 对应的信息有   num  name  charactor  remark  score  
        
    f = open("E:\\Python/movie_data/douban.txt","r")     #打开路径复制其中的数据，以便导入数据库    
    while True:
      line = f.readline()
             
      if line:    
        line = line.strip("\n")  
        line = line.split("#")   
        num = line[0]               #将需要的几个量复制  
        name = line[1]
        director_charactor = line[2]  
         
        year = line[3]
        nation = line[4]
        type = line[5]   
        score = line[6]
        people = line[7] 
        remark = line[8]
        #print num,name,director,charactor,year,nation,type,score,people,remark
        con.execute("insert into doubantop(num,name,director_charactor,year,nation,type,score,people,remark)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",[num,name,director_charactor,year,nation,type,score,people,remark])
      else:
        break    
    connect.commit()          #这句记得写上提交数据，否则导入为空(有的DDL是不需要导入的)  
    con.close()          #最后记得关掉连接  
    connect.close()  
    f.close()
