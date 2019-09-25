import requests

class APILib:
    def getAPI(url,payload,headers):
        response = requests.request("GET",url,data=payload,headers=headers)
        return response

    def postAPI(url,payload,headers):
            response = requests.request("POST", url, data=payload, headers=headers)
            return response

    def putAPI(url,payload, headers):
            response = requests.request("PUT", url, data=payload, headers=headers)
            return response

    def deleteAPI(url,payload, headers):
            response = requests.request("DELETE", url, data=payload, headers=headers)
            return response