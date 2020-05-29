import requests
import json
import re

def get_cookie(switchIP):
    f = open("/Users/skilladi/Documents/PyCharm Projects/ArubaSwitchAutomation/src/config/params.json", 'r')
    url = f"http://{switchIP}:80/rest/v1/login-sessions"
    credentials = json.loads(f.read())
    f.close()
    try:
        response = requests.post(url, data=credentials, timeout=5)
        if response.status_code == 200:
            json_response = json(response.text)
            try:
                return json_response["cookie"]
            except Exception as e:
                # print(e)
                try:
                    if json_response["message"] == "Authentication failed.":
                        print("Authentication failed. No cookie to extract")
                except Exception as e:
                    print("Authentication neither passed nor failed")
                    # print(e)
        else:
            print(f"Login did not succeed {response.status_code} error")
    except Exception as e:
        print("Did not receive any response from the device")
        # print(e)
        return None

def getVlanDetails(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_response = json(response.text)
        elements = json_response["vlan_element"]
        vlan_details = []
        try:
            for vlan in elements:
                vlan_details.append({"vlan_name": vlan["name"]}, {"vlan_id": vlan["vlan_id"]})
        except Exception as e:
            print("Did not find the key(s): vlan_id or name")
            # print(e)

    else:
        print(f"Did not return the desired vlan data from the switch coz of {response.status_code} error")
        return None

    return vlan_details

def configVlan(switchIP, cookie, vlan_data):
    headers = {"cookie": cookie}
    url = f"http://{switchIP}:80/rest/v1/vlans"

    try:
        response = requests.post(url, data=vlan_data, headers=headers, timeout=5)
        if response.status_code == 201:
            return True
        else:
            print(f"Config push failed")
            return False
    except Exception as e:
        # print(e)
        print("Did not get any response from the switch. Config failed")
        return False

