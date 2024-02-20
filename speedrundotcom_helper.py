import json
import requests
def submitRun(srdcKey, category, level, time, ticks, demoLink):
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

    url = "https://speedrun.com/api/v1/runs"
    headers = {
        "Host": "www.speedrun.com",
        "X-API-Key": srdcKey
    }

    response = requests.post(url, headers=headers, json=submission)

    data = response.json()
    print("Speedrun successfully submitted to")
    print(data.get("data").get("weblink"))