# pip install python-geoip-geolite2
import collections
from geoip import geolite2


countries = []
with open("ips.txt") as iplist:
	ips = iplist.readlines()
	for ip in ips:
		resp = geolite2.lookup(ip.rstrip())
		countries.append(resp.country)
print(collections.Counter(countries))
