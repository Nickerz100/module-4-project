import requests

def get_public_ip_info():
    # Define the API endpoint
    api_url = 'http://ip-api.com/json/'

    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            ip_info = response.json()

            # Extract relevant information
            ip = ip_info['query']
            city = ip_info['city']
            country = ip_info['country']
            isp = ip_info['isp']

            # Display the formatted information
            print(f"Public IP Address: {ip}")
            print(f"City: {city}")
            print(f"Country: {country}")
            print(f"ISP: {isp}")
        else:
            print("Failed to retrieve IP information.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    get_public_ip_info()
