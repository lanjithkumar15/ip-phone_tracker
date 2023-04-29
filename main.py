import requests
import json
from colorama import Fore, Style
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import pyfiglet as pyg
from termcolor import colored
import sys

def banner():
    text = "IPPHONE-OSINT"
    by = "BY:"
    name = "crazyoh123"
    print(colored(pyg.figlet_format(text, font="xsbook",direction="left",justify="auto",width=100), 'red')+"\n")
    print(colored(by, 'green')+"\n")
    print(colored(name+"//", 'green')+"\n")


def ipaddress():
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

def phonenumber():
     KEY_VALUE = Fore.RED
     VALUE_KEY = Fore.GREEN

     phone = input(KEY_VALUE+"ENTER THE PHONE NUMBER FORMAT +92xxxxxxx >> ")
     parsed_number = phonenumbers.parse(phone)
     print(VALUE_KEY+"COUNTRY CODE OF THE GIVEN PHONE NUMBER >> "+KEY_VALUE+f"+{parsed_number.country_code}")
     print(VALUE_KEY+"LOCAL NUMBER OF THE GIVEN PHONE NUMBER >> "+KEY_VALUE+f"{parsed_number.national_number}")
     print(VALUE_KEY+"LOCATION OF THE GIVEN NUMBER >> "+KEY_VALUE+f"{geocoder.description_for_number(parsed_number, 'en')}")
     print(VALUE_KEY+"REGION CODE FOR THE PHONE NUMBER >> "+KEY_VALUE+f"{geocoder.region_code_for_number(parsed_number)}")
     print(VALUE_KEY+"TIMEZONE OF THE GIVEN PHONE NUMBER >> "+KEY_VALUE+f"{timezone.time_zones_for_number(parsed_number)}")
     print(VALUE_KEY+"OPERATOR OF THE GIVEN NUMBER >> "+KEY_VALUE+f"{carrier.name_for_number(parsed_number, 'en')}")
     x = phonenumbers.is_valid_number(parsed_number)
     print(VALUE_KEY+"VALID OR  NOT = "+KEY_VALUE+"IS VALID PHONE NUMBER!!" if x else KEY_VALUE+"VALID OR NOT = "+VALUE_KEY+"IT IS NOT VALID PHONE NUMBER!!")
     y = phonenumbers.is_possible_number(parsed_number)
     print(KEY_VALUE+"THIS IS POSSIBLE NUMBER!!" if y else VALUE_KEY+"THIS IS NOT POSSIBLE NUMBER!!")
     print(VALUE_KEY+"INTERNATIONAL FORMAT OF THE PHONE NUMBER >> +"+str(parsed_number.country_code)+" "+str(parsed_number.national_number))
     number_type = phonenumbers.number_type(parsed_number)
     if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(VALUE_KEY+"TYPE >> "+KEY_VALUE+"This is an Mobile Number")
     elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(VALUE_KEY+"TYPE >> "+KEY_VALUE+"This is a fixed-line number")
     else:
        print(VALUE_KEY+"TYPE >> "+KEY_VALUE+"This is another type of number")

if __name__ == "__main__":
    banner()
    number = str((input("ENTER THE NUMBER 1 FOR THE IP ADDRESS AND 2 FOR THE PHONE NUMBER")))
    if number == '1':
        ipaddress()
    elif number == '2':
        phonenumber()
    else:
        sys.exit(0)
