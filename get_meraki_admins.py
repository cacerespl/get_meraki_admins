import json
import requests
import sys

#api_key and org_id are passed as arguments
api_key = sys.argv[1]
org_id = sys.argv[2]
url = "https://api.meraki.com/api/v0/organizations/"+org_id+"/admins"

def get_admins(api_key, url):
    """
    This function will return a list of admins for an Organization
    Arguments: api key and url    

    """
    list_admins = []
    headers = { 'x-cisco-meraki-api-key': api_key }
    response = requests.get(url, headers = headers)
    number_admins = len(response.json())
    for i in range(number_admins):
        list_admins.append(response.json()[i]['name'])
    return list_admins


if __name__ == "__main__":
    print get_admins(api_key, url)


