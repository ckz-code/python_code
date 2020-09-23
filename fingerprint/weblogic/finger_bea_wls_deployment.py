import sys
import requests

def main():
	url = sys.argv[1]
	response = requests.post(url+'/bea_wls_deployment_internal/DeploymentService')
	if response.status_code in (401, 500):
		print("\033[1;37;40m {} \033[0m \033[1;32;40m {} \033[0m".format(url, "finger weblogic dea_wls_deployment"))

if __name__ == '__main__':
	main()
