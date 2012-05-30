#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
db=MySQLdb.connect(host="openserver",user="root",passwd="",db="stden",use_unicode=True)
db.set_character_set('utf8')
c=db.cursor()
# Избыточные установки utf8 - может в некоторых случаях не избыточные? :)
#c.execute('SET NAMES utf8;')
#c.execute('SET CHARACTER SET utf8;')
#c.execute('SET character_set_connection=utf8;')

# Устанавливаем UTF-8 для вывода в консоли
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Перенаправляем вывод в файл
sys.stdout = open('MySQLdb_example.log', 'w')

# Создаём запрос и выполняем его 
sql = "SELECT * FROM user"
c.execute(sql)

# Fetch all results from the cursor into a sequence and close the connection
print u"Запрос: "+sql # Все строки надо делать в Unicode, хех :)
res = c.fetchall()
for row in res:
  print u"-- Новая строка --"
  for f in row:
    print f
db.close()