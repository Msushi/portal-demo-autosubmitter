import json
import requests

def submitRun(srdcKey, submission):
    url = "https://speedrun.com/api/v1/runs"
    headers = {
        "Host": "www.speedrun.com",
        "X-API-Key": srdcKey
    }

    response = requests.post(url, headers=headers, json=submission)

    print(response.content)

    data = response.json()
    print("Speedrun successfully submitted to")
    print(data.get("data").get("weblink"))


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
            "variables": {
                "gnx0q06n": {
                    "type": "user-defined",
                    "value": str(ticks),
                },
            }, 
        }
    }

    submitRun(srdcKey, submission)

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

    submitRun(srdcKey, submission)
    

