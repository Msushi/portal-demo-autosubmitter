import sys
import os
import time
from datetime import timedelta
from demo_parser import *
from settings import *
from category_game_wrapper import *
from google_drive_helper import *
from speedrundotcom_helper import *

def main(): 
    if len(sys.argv) == 1:
        print("No demo file.")
        test = ["C:/coding/portal-demo-autosubmitter/dist/escape_01.dem", "C:/coding/portal-demo-autosubmitter/dist/escape_02.dem"]
        mapNames = []
        demoTicks = []
        wakeupFound = False
        for demo in test:
                mapName, ticks, wakeup = parse_demo(demo)
                mapNames.append(mapName)
                demoTicks.append(ticks)
                if wakeup:
                    wakeupFound = True
        game, isIL, levelID, categoryID, runTime, totalTicks, levelText, categoryText = getSubmissionInfo(mapNames, demoTicks, wakeupFound)

        td = timedelta(seconds=runTime)

        if (isIL):
            print(f"Are you sure you want to submit your {game} {levelText} {categoryText} {td} speedrun?")
        else:
            print(f"Are you sure you want to submit your {game} {categoryText} {td} speedrun?")

    else:
        gapiKey, srdcKey = getAPIKeys()
        if len(sys.argv) == 2:
            mapName, ticks, wakeup = parse_demo(sys.argv[1])
            game, IL, category, runTime, totalTicks = getSubmissionInfo([mapName], [ticks], False)
            link = uploadFileToDrive(sys.argv[1], gapiKey)
            #submitRun(srdcKey, category, IL, runTime, totalTicks, link)
        else:
            demos = sys.argv[1:]
            mapNames = []
            demoTicks = []
            wakeupFound = False
            for demo in demos:
                mapName, ticks, wakeup = parse_demo(demo)
                mapNames.append(mapName)
                demoTicks.append(ticks)
                if wakeup:
                    wakeupFound = True
            game, isIL, levelID, categoryID, runTime, totalTicks, levelText, categoryText = getSubmissionInfo(mapNames, demoTicks, wakeupFound)

            td = timedelta(seconds=runTime)

            if (isIL):
                print(f"Are you sure you want to submit your {game} {levelText} {categoryText} {td[:-2]} speedrun?")
            else:
                print(f"Are you sure you want to submit your {game} {categoryText} {td[:-2]} speedrun?")

    print()
    print()
    print("Program will exit in 5 seconds...")
    time.sleep(10)

if __name__ == "__main__":
    main()