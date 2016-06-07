from datetime import datetime


date_start = '01-02-2013'
date_stop = '07-27-2015'

date_1 = datetime.strptime(date_start, "%m-%d-%Y")
date_2 = datetime.strptime(date_stop, "%m-%d-%Y")

print date_2-date_1

date_start = '12312013'
date_stop = '05282015'

date_1 = datetime.strptime(date_start, "%m%d%Y")
date_2 = datetime.strptime(date_stop, "%m%d%Y")

print date_2-date_1

date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

date_1 = datetime.strptime(date_start, "%d-%b-%Y")
date_2 = datetime.strptime(date_stop, "%d-%b-%Y")

print date_2-date_1
