import requests
import os
from google_secret import *

def getAPIKeys(pathToExe):

    gapiRefreshKey = ""
    gapiKey = ""
    srdcKey = ""
    dir = os.path.dirname(pathToExe)
    try:
        with open(f"{dir}\\settings.cfg", "r") as f:
            gapiRefreshKey = f.readline()
            srdcKey = f.readline()
            gapiKey, gapiRefreshKey = getGapiKeyFromToken(gapiRefreshKey, True)
    except FileNotFoundError:
        pass

    gapiEdited = False
    while (not checkValidGapiKey(gapiKey)):
        if gapiEdited:
            print("Your previous response didn't authenticate properly. Please try again.")
            print()
        gapiKey, gapiRefreshKey = getGapiKey()
        gapiEdited = True
    print("Valid Google Drive API Key.")
    print()

    srdcEdited = False
    while (not checkValidSRDCKey(srdcKey)):
        if srdcEdited:
            print("Your previous response didn't authenticate properly. Please try again.")
            print()
        srdcKey = getSRDCKey()
        srdcEdited = True
    print("Valid Speedrun.com API Key.")
    print()
        
    if gapiEdited or srdcEdited:
        writeToFile(gapiRefreshKey, srdcKey, dir)

    return gapiKey, srdcKey

def getGapiKey():
    print("You do not have a valid google account linked.")
    print("Please click on the link below and login to grant access to your google drive")
    print(oauth_url)
    gapiKey = input("Authorization Code:")
    print()
    return getGapiKeyFromToken(gapiKey, False)

def getGapiKeyFromToken(authCode, refreshToken):
    url = "https://accounts.google.com/o/oauth2/token"


    if (refreshToken):
        data = {
            "refresh_token": authCode,
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "refresh_token",
            "redirect_uri": "urn:ietf:wg:oauth:2.0:oob"
        }
    else:
        data = {
            "code": authCode,
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "authorization_code",
            "redirect_uri": "urn:ietf:wg:oauth:2.0:oob"
        }

    response = requests.post(url, data=data)


    if response.status_code == 200:
        refresh_token = response.json().get("refresh_token")
        access_token = response.json().get("access_token")
        return access_token, refresh_token
    else:
        print("Error:", response.status_code)
        return "", ""

def checkValidGapiKey(gapiKey):
    url = "https://www.googleapis.com/drive/v3/files"
    params = {
        "q": "mimeType='application/vnd.google-apps.folder' and name='Test' and trashed=false",
        "fields": "files(id,name)"
    }
    headers = {
        "Authorization": f"Bearer {gapiKey}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, params=params, headers=headers)

    return (response.status_code == 200)



def getSRDCKey():
    print("You are not currently do not have a speedrun.com linked. Please follow these steps to link your account:")
    print("   Go to https://www.speedrun.com")
    print("   Go to your profile (top right corner)")
    print("   Click settings (middle right of the page)")
    print("   Scroll down to API Key (left side of the screen, below 'Developers'")
    print("   Click show API Key, copy it, and paste it below:")
    srdcKey = input("API Key:")
    print()
    return srdcKey


def checkValidSRDCKey(srdcKey):
    url = "https://speedrun.com/api/v1/profile"
    headers = {
        "Host": "www.speedrun.com",
        "X-API-Key": srdcKey,
        "User-Agent": "MsushiPortalAutosubmitter/b0.1"
    }

    response = requests.get(url, headers=headers)

    return (response.status_code == 200)

def writeToFile(gapiRefreshKey, srdcKey, dir):
    with open(f"{dir}\\settings.cfg", 'w') as f:
        f.write(gapiRefreshKey)
        f.write("\n")
        f.write(srdcKey)
