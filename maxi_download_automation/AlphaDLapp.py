import urllib

NoV = urllib.URLopener()
#Borough
#data =  input("Enter BBL 1 5 4 format /(ex:1000800001 for M-80-1/): ")
data1 = raw_input("borough:")
data2 = raw_input("block:")
data3 = raw_input("lot:")
#data4 = raw_input("Do you want the payment history as well? (Y/N) ")

#Brooklyn #3
NoV.retrieve("http://nycprop.nyc.gov/nycproperty/StatementSearch?bbl={}{}{}&stmtDate=20150115&stmtType=NPV".format(data1,data2,data3), "{0}-{1}-{2}-15.pdf".format(data1,data2,data3))
#NoV.retrieve("http://nycprop.nyc.gov/nycproperty/StatementSearch?bbl={}{}{}&stmtDate=20140115&stmtType=NPV".format(data1,data2,data3), "{0}-{1}-{2}-14.pdf".format(data1,data2,data3))
#NoV.retrieve("http://nycprop.nyc.gov/nycproperty/StatementSearch?bbl={}{}{}&stmtDate=20130115&stmtType=NPV".format(data1,data2,data3), "{0}-{1}-{2}-13.pdf".format(data1,data2,data3))
#NoV.retrieve("http://nycprop.nyc.gov/nycproperty/StatementSearch?bbl={}{}{}&stmtDate=20120115&stmtType=NPV".format(data1,data2,data3), "{0}-{1}-{2}-12.pdf".format(data1,data2,data3))
#NoV.retrieve("http://nycprop.nyc.gov/nycproperty/StatementSearch?bbl={}{}{}&stmtDate=20110115&stmtType=NPV".format(data1,data2,data3), "{0}-{1}-{2}-11.pdf".format(data1,data2,data3))
#NoV.retrieve("http://nycprop.nyc.gov/nycproperty/StatementSearch?bbl={}{}{}&stmtDate=20100115&stmtType=NPV".format(data1,data2,data3), "{0}-{1}-{2}-10.pdf".format(data1,data2,data3))

#NoV.retrieve("http://webapps.nyc.gov:8084/cics/f704/f403001i?DET=%s-%s-%s-"%(data1, data2, data3), "%s-%s-%s_AccountHistory2015.html"%(data1,data2,data3))

print ("The NoV and payment history has been downloaded for {0} Block {1} Lot {2} as {0}-{1}-{2}.pdf".format(data1, data2, data3))

#another way may be to have data[string] and have all bbl's in there, then have it go one by one...