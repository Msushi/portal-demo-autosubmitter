import sys
import os
import time
import zipfile
from datetime import timedelta
from demo_parser import *
from settings import *
from category_game_wrapper import *
from google_drive_helper import *
from speedrundotcom_helper import *

def main(): 
    if len(sys.argv) == 1:
        print("No demo file detected.")
        print()
        print("Please try again, make sure you drag demos onto the .exe")
        demo = ["C:/coding/portal-demo-autosubmitter/dist/fullgame_28-12-000.dem"]
        parse_demo(demo[0])
        
        
    else:
        gapiKey, srdcKey = getAPIKeys(sys.argv[0])
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
        game, isIL, levelID, categoryID, runTime, totalTicks, variableID, levelText, categoryText = getSubmissionInfo(mapNames, demoTicks, wakeupFound)
        print()

        td = timedelta(seconds=runTime)

        if (isIL):
            print(f"Are you sure you want to submit your {game} {levelText} {categoryText} {td} speedrun?")
            print()
            input("Press enter to confirm")
            print()
            print("Uploading file to google drive...")
            print()
            link = uploadFileToDrive(sys.argv[1], gapiKey)
            print()
            print("Submitting to speedrun.com...")
            finalLink = submitPortalIL(srdcKey, categoryID, levelID, runTime, totalTicks, link)
                
        else:
            print(f"Are you sure you want to submit your {game} {categoryText} {td} speedrun?")
            print()
            input("Press any key to confirm")
            print()
            print("Zipping demos...")
            print()
            zipName = f"{categoryText}{str(td)}" 
            zipName = zipName.replace(':', '_')
            zipName = zipName.replace('.', '')
            zipName = f"{zipName}.zip"
            with zipfile.ZipFile(zipName, 'w') as zipf:
                for demo in demos:
                    zipf.write(demo, os.path.basename(demo))
                zipf.close()
            print("Uploading file to google drive...")
            print()
            link = uploadFileToDrive(zipName, gapiKey)
            print()
            print("Submitting to speedrun.com...")
            print()
            finalLink = submitPortalRun(srdcKey, categoryID, runTime, variableID, link)
        
        if finalLink != "":
                print("Success! Speedrun submitted.")
                print(finalLink)

    print()
    print()
    print("Program will exit in 10 seconds...")
    time.sleep(10)

if __name__ == "__main__":
    main()