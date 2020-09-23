import sys
import requests

def main():
	url = sys.argv[1]
	response = requests.get(url+'/solr')
	finger = ["Solr Admin", "Apache SOLR", "Dashboard","solr"]
	count = [x for x in finger if x in response.text]
	if count:
		print("\033[1;37;40m {} \033[0m \033[1;32;40m {} \033[0m".format(url, "finger solr Admin"))

if __name__ == '__main__':
	main()
