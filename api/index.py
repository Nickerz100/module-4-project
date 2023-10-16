import requests

def getPublicIPInfo(ip):
    # API endpoint 
    apiURL = "http://ip-api.com/json/" + ip

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

iserIP = input("Enter an IP address or click ENTER to use your current IP: ")
getPublicIPInfo(userIP)
