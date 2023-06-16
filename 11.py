import pymysql

# 连接到MySQL数据库
mydb = pymysql.connect(host="localhost",\
    user="root",\
    password="123456",\
    database="student",\
    charset="utf8mb4"

)

# 创建游标对象
mycursor = mydb.cursor()

# 定义SQL查询语句
sql = "SELECT * from studen WHERE c >= 60 AND python >= 60;"

# 执行SQL查询
mycursor.execute(sql)

# 获取查询结果
result = mycursor.fetchall()

# 输出查询结果
for row in result:
    print("Name:", row[0])
    print("Sex:", row[1])
    print("Class:", row[2])
    print("C language grade:", row[3])
    print("Python grade:", row[4])
