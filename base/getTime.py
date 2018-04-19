#coding=utf-8
import time

ticks = time.time()
print "当前时间戳为：{}".format(ticks)
#当前时间戳为：1524150172.8

#获取当前时间  从返回浮点数的时间戳方式向时间元组转换
localtime = time.localtime(time.time())
print "本地时间：{}".format(localtime)
#本地时间：time.struct_time(tm_year=2018, tm_mon=4, tm_mday=19, tm_hour=23, tm_min=2, tm_sec=52, tm_wday=3, tm_yday=109, tm_isdst=0)

#获取格式化时间 time.strftime(format[,t])
localtime = time.asctime( time.localtime(time.time()) )
print "本地时间：{}".format(localtime)
#本地时间：Thu Apr 19 23:21:35 2018

# 格式化成2016-03-20 11:45:39形式
baseTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print baseTime
#2018-04-19 23:21:35

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime(time.time()))
#Thu Apr 19 23:21:35 2018

#
print "当前时间:{}".format(time.strftime("%Y%m%d%H%M",time.localtime(time.time())))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
#1459175064.0

# python中时间日期格式化符号：

#     %y 两位数的年份表示（00-99）
#     %Y 四位数的年份表示（000-9999）
#     %m 月份（01-12）
#     %d 月内中的一天（0-31）
#     %H 24小时制小时数（0-23）
#     %I 12小时制小时数（01-12）
#     %M 分钟数（00=59）
#     %S 秒（00-59）
#     %a 本地简化星期名称
#     %A 本地完整星期名称
#     %b 本地简化的月份名称
#     %B 本地完整的月份名称
#     %c 本地相应的日期表示和时间表示
#     %j 年内的一天（001-366）
#     %p 本地A.M.或P.M.的等价符
#     %U 一年中的星期数（00-53）星期天为星期的开始
#     %w 星期（0-6），星期天为星期的开始
#     %W 一年中的星期数（00-53）星期一为星期的开始
#     %x 本地相应的日期表示
#     %X 本地相应的时间表示
#     %Z 当前时区的名称
#     %% %号本身

#获取某月日历
import calendar
cal = calendar.month(2016,1)
print cal




