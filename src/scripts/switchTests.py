import src.libs.deviceLib as dLib
import json
import os

f = open("/Users/skilladi/Documents/PyCharm Projects/ArubaSwitchAutomation/src/config/switch_details.json", "r")
ip_list = json.loads(f.read())

SWITCH1 = ip_list[0]["Switch1"]
SWITCH2 = ip_list[1]["Switch2"]
SWITCH3 = ip_list[2]["Switch3"]
f.close()

def main():
    cookie = dLib.get_cookie(SWITCH1)
    if cookie is not None:
        with open("/Users/skilladi/Documents/PyCharm Projects/ArubaSwitchAutomation/src/config/vlan_config.json", "r") as f:
            vlan_data = json.loads(f.read())
            if dLib.configVlan(SWITCH1, cookie, vlan_data):
                print("Config done successfully")

if __name__ == '__main__':
    main()


