import sys
import requests

def main():
	url = sys.argv[1]
	response = requests.get(url+'/wls-wsat/CoordinatorPortType')
	if "wsdl" in response.text:
		print("\033[1;37;40m {} \033[0m \033[1;32;40m {} \033[0m".format(url, "finger weblogic wls-wsat"))

if __name__ == '__main__':
	main()
