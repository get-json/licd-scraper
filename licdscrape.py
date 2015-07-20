import urllib
import datetime

init = datetime.date(2003, 2, 9)
diff = str(datetime.date.today() - init)
days = int(diff.split()[0])

for i in range(0,days):
	start = datetime.date(2003, 2, 9) + datetime.timedelta(days=i)
	lsstart = str(start).split("-")
	x = "http://www.leasticoulddo.com/wp-content/uploads/"+str(lsstart[0])+"/"+str(lsstart[1])+"/"+str(lsstart[0])+str(lsstart[1])+str(lsstart[2])+".gif"
	y = str(lsstart[0])+str(lsstart[1])+str(lsstart[2])+".gif"
	urllib.urlretrieve(x,y)
