import requests
import json
from colorama import Fore, Style

KEY_COLOR = Fore.RED
VALUE_COLOR = Fore.GREEN

ipaddress = input(KEY_COLOR+"ENTER THE IP ADDRESS >> ")

x = requests.get("https://ipapi.co/" + ipaddress +"/json/")
json_string = x.text

try:
    json_data = json.loads(json_string)
except json.JSONDecodeError:
    print(Fore.RED + "Invalid response received from the server. Please try again later.")
    exit()

if "error" in json_data:
    print(Fore.RED + "Error:", json_data["error"])
    print(Fore.RED+"INVALID IP ADDRESS OR RESERVED IP ADDRESS")
else:
    try:
        print(KEY_COLOR+"Internet Protocol Address : "+VALUE_COLOR+json_data["ip"])
        print(KEY_COLOR+"Organization/ISP Name : "+VALUE_COLOR+json_data["org"])
        print(KEY_COLOR+"City : "+VALUE_COLOR+json_data["city"])
        print(KEY_COLOR+"Region/State : "+VALUE_COLOR+json_data["region"])
        print(KEY_COLOR+"Region/State Code :"+VALUE_COLOR+json_data["region_code"])
        print(KEY_COLOR+"Country Code : "+VALUE_COLOR+json_data["country_code"])
        print(KEY_COLOR+"Country Name : "+VALUE_COLOR+json_data["country_name"])
        print(KEY_COLOR+"Country Capital : "+VALUE_COLOR+json_data["country_capital"])
        print(KEY_COLOR+"Country Top-Level Domain : "+VALUE_COLOR+json_data["country_tld"])
        print(KEY_COLOR+"Continent Code : "+VALUE_COLOR+json_data["continent_code"])
        print(KEY_COLOR+"Postal/ZIP Code : "+VALUE_COLOR+json_data["postal"])
        print(KEY_COLOR+"Latitude : "+VALUE_COLOR+str(json_data["latitude"]))
        print(KEY_COLOR+"Longitude : "+VALUE_COLOR+str(json_data["longitude"]))
        print(KEY_COLOR+"Timezone : "+VALUE_COLOR+json_data["timezone"])
        print(KEY_COLOR+"Country Calling Code : "+VALUE_COLOR+json_data["country_calling_code"])
        print(KEY_COLOR+"Currency : "+VALUE_COLOR+json_data["currency"])
        print(KEY_COLOR+"Currency Name : "+VALUE_COLOR+json_data["currency_name"])
        print(KEY_COLOR + "GOOGLE MAP LINK : " + VALUE_COLOR + "https://www.google.com/maps?q="+str(json_data["latitude"])+","+str(json_data["longitude"]))
    except KeyError:
        print(Fore.RED + "Error: Required information not found in the server response.")
