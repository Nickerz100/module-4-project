import requests
import vc__handler__python

def getPublicIPInfo():
    # API endpoint 
    apiURL = "http://ip-api.com/json/"

    # GET request for IP address parsing
    response = requests.get(apiURL)
    ipInfo = response.json()

    # Extract relevant information
    ip = ipInfo['query']
    city = ipInfo['city']
    country = ipInfo['country']
    isp = ipInfo['isp']

    # Display IP information
    print("Public IP Address: " + ip)
    print("City: " + city)
    print("Country: " + country)
    print("ISP: " + isp)

getPublicIPInfo()
