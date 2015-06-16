import urllib
NoV = urllib.URLopener()
bbl = [1000800001]

for item in bbl:
	NoV.retrieve("http://nycprop.nyc.gov/nycproperty/StatementSearch?bbl={}&stmtDate=20150115&stmtType=NPV".format(bbl), "NOV-2015_{}.pdf".format(bbl))
#error
# NoV.retrieve("http://nycprop.nyc.gov/nycproperty/StatementSearch?bbl={}&stmtDate=
# "NOV-2015_{}.pdf".format(bbl))
#  File "C:\Python27\lib\urllib.py", line 245, in retrieve
#    fp = self.open(url, data)
#  File "C:\Python27\lib\urllib.py", line 213, in open
#    return getattr(self, name)(url)
#  File "C:\Python27\lib\urllib.py", line 364, in open_http
#    return self.http_error(url, fp, errcode, errmsg, headers)
#  File "C:\Python27\lib\urllib.py", line 381, in http_error
#    return self.http_error_default(url, fp, errcode, errmsg, headers)
#  File "C:\Python27\lib\urllib.py", line 386, in http_error_default
#    raise IOError, ('http error', errcode, errmsg, headers)
#IOError: ('http error', 302, 'Found', <httplib.HTTPMessage instance at 0x02021DF0>)