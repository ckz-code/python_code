import sys
import requests

def main():
	url = sys.argv[1]
	finger = ['/wls_utc', '/wsutc/begin.do', '/ws_utc/config.do']
	for i in finger:
		response = requests.get(url+i)
		if "administrator" in response.text:
			count+=1
	if count:
		print("\033[1;37;40m {} \033[0m \033[1;32;40m {} \033[0m".format(url, "finger weblogic ws_utc"))

if __name__ == '__main__':
	main()
