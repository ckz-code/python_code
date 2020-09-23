import sys
import requests

def main():
	url = sys.argv[1]
	response = requests.get(url+'/_async/AsyncResponseService')
	if response.status_code == 202:
		print("\033[1;37;40m {} \033[0m \033[1;32;40m {} \033[0m".format(url, "finger weblogic wls_async"))

if __name__ == '__main__':
	main()
