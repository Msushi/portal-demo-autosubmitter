import json
import requests

def submitRun(srdcKey, submission):
    url = "https://speedrun.com/api/v1/runs"
    headers = {
        "Host": "www.speedrun.com",
        "X-API-Key": srdcKey,
        "User-Agent": "MsushiPortalAutosubmitter/b0.1"
    }

    response = requests.post(url, headers=headers, json=submission)


    if (response.status_code == 201):
        data = response.json()
        return (data.get("data").get("weblink"))
    else:
        print("Error submitting speedrun")
        print(response.content)
        return ""


def submitPortalIL(srdcKey, category, level, time, ticks, demoLink):
    submission = {
        "run": {
            "category": category,
            "level": level,
            "platform": "8gej2n93",
            "times": {
                "realtime": time,
                "realtime_noloads": time,
            },
            "emulated": False,
            "comment": demoLink,
        }
    }

    return submitRun(srdcKey, submission)

def submitPortalRun(srdcKey, category, time, variableID, demoLink):
    submission = {
        "run": {
            "category": category,
            "platform": "8gej2n93",
            "times": {
                "realtime_noloads": time,
            },
            "emulated": False,
            "comment": demoLink,
            "variables": {
                "kn0mz7ol": {
                    "type": "pre-defined",
                    "value": "jq6nxjnl"
                }
            },
        }
    }

    return submitRun(srdcKey, submission)
    

