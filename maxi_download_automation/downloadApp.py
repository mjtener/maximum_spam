import urllib

NoV = urllib.URLopener()

#Brooklyn #3
NoV.retrieve("http://nycprop.nyc.gov/nycproperty/StatementSearch?bbl=3002500044&stmtDate=20150115&stmtType=NPV", "K-250-44.pdf")

#Manhattan #1

NoV.retrieve("http://nycprop.nyc.gov/nycproperty/StatementSearch?bbl=1000050010&stmtDate=20150115&stmtType=NPV", "M-5-10.pdf")
NoV.retrieve("http://nycprop.nyc.gov/nycproperty/StatementSearch?bbl=1000130001&stmtDate=20150115&stmtType=NPV", "M-13-1.pdf")
NoV.retrieve("http://nycprop.nyc.gov/nycproperty/StatementSearch?bbl=1000510007&stmtDate=20150115&stmtType=NPV", "M-51-7.pdf")
NoV.retrieve("http://nycprop.nyc.gov/nycproperty/StatementSearch?bbl=1000800001&stmtDate=20150115&stmtType=NPV", "M-80-1.pdf")


#Queens #4
NoV.retrieve("http://nycprop.nyc.gov/nycproperty/StatementSearch?bbl=4096770016&stmtDate=20150115&stmtType=NPV", "Q-9677-16.pdf")

#Bronx   #2

#Extraneous
NoV.retrieve("http://webapps.nyc.gov:8084/cics/f704/f403001i?DET=3-00250-0044-", "K-250-44_AccountHistory2015.html")