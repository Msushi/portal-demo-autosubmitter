import os
import requests
import json

def uploadFileToDrive(filePath, gapiKey):
    folderID = getFolderID(gapiKey)

    url = "https://www.googleapis.com/upload/drive/v3/files"
    params = {"uploadType": "multipart"}
    
    headers = {
        "Authorization": f"Bearer {gapiKey}",
    }
    
    file_name = os.path.basename(filePath)
    
    metadata = {
        "name": file_name,
        "parents": [folderID]
    }
    
    files = {
        "metadata": (None, json.dumps(metadata), "application/json"),
        "file": (file_name, open(filePath, "rb"), "application/octet-stream")
    }
    
    response = requests.post(url, params=params, headers=headers, files=files)
    
    if response.status_code == 200:
        print("File uploaded successfully.")
        data = response.json()
        return getSharedLink(data["id"], gapiKey)
    else:
        print("Error uploading file:", response.status_code)

def getSharedLink(fileID, gapiKey):
    url = f"https://www.googleapis.com/drive/v3/files/{fileID}/permissions"
    
    headers = {
        "Authorization": f"Bearer {gapiKey}",
        "Content-Type": "application/json"
    }
    
    permission = {
        "role": "reader",
        "type": "anyone"
    }
    
    response = requests.post(url, headers=headers, json=permission)
    
    if response.status_code == 200:
        return f"https://drive.google.com/file/d/{fileID}/view?usp=drive_link"
    else:
        print("Error setting permission:", response.status_code)

def getFolderID(gapiKey):
    url = "https://www.googleapis.com/drive/v3/files"
    params = {
        "q": "mimeType='application/vnd.google-apps.folder' and name='Portal Demos' and trashed=false",
        "fields": "files(id,name)"
    }
    headers = {
        "Authorization": f"Bearer {gapiKey}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        folders = data.get("files")
        if folders:
            return folders[0].get("id")
        else:
            return createFolder("Portal Demos", gapiKey)
    else:
        print("Error:", response.status_code)

def createFolder(folderName, gapiKey):
    url = "https://www.googleapis.com/drive/v3/files"
    
    headers = {
        "Authorization": f"Bearer {gapiKey}",
        "Content-Type": "application/json"
    }
    
    metadata = {
        "name": folderName,
        "mimeType": "application/vnd.google-apps.folder"
    }
    
    response = requests.post(url, headers=headers, json=metadata)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("id")
    else:
        print("Error creating folder:", response.status_code)