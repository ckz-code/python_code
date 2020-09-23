import sys
import requests

def main():
	url = sys.argv[1]
	response = requests.get(url+'/uddiexplorer/')
	if "UDDI Explorer" in response.text:
		print("\033[1;37;40m {} \033[0m \033[1;32;40m {} \033[0m".format(url, "finger weblogic uddi"))

if __name__ == '__main__':
	main()
