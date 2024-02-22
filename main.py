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
    print(sys.argv)
    if len(sys.argv) == 1:
        print("No demo file.")
        gapiKey, srdcKey = getAPIKeys("C:/coding/portal-demo-autosubmitter/dist/main.exe")
        demos = ['C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\escape_01_1.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\escape_02.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_00.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_01.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_02.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_03.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_04.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_05.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_06.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_07.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_08.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_08_1.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_09.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_10.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_11.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_13.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_13_1.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_14.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\testchmb_a_15.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\vault.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\escape_00.dem', 'C:\\coding\\portal-demo-autosubmitter\\dist\\glitchless_15_13\\escape_01.dem']
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

        td = timedelta(seconds=runTime)

        if (isIL):
            print(f"Are you sure you want to submit your {game} {levelText} {categoryText} {td} speedrun?")
                
        else:
            print(f"Are you sure you want to submit your {game} {categoryText} {td} speedrun?")
            zipName = f"{categoryText}{str(td)}" 
            zipName = zipName.replace(':', '_')
            zipName = zipName.replace('.', '')
            zipName = f"{zipName}.zip"
            with zipfile.ZipFile(zipName, 'w') as zipf:
                for demo in demos:
                    zipf.write(demo, os.path.basename(demo))
                zipf.close()
            link = uploadFileToDrive(zipName, gapiKey)
            submitPortalRun(srdcKey, categoryID, runTime, variableID, link)
    else:
        gapiKey, srdcKey = getAPIKeys(sys.argv[0])
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
            game, isIL, levelID, categoryID, runTime, totalTicks, variableID, levelText, categoryText = getSubmissionInfo(mapNames, demoTicks, wakeupFound)

            td = timedelta(seconds=runTime)

            if (isIL):
                print(f"Are you sure you want to submit your {game} {levelText} {categoryText} {td} speedrun?")
                
            else:
                print(f"Are you sure you want to submit your {game} {categoryText} {td} speedrun?")
                zipName = f"{categoryText}{str(td)}" 
                zipName = zipName.replace(':', '_')
                zipName = zipName.replace('.', '')
                zipName = f"{zipName}.zip"
                with zipfile.ZipFile(zipName, 'w') as zipf:
                    for demo in demos:
                        zipf.write(demo, os.path.basename(demo))
                    zipf.close()
                link = uploadFileToDrive(zipName, gapiKey)
                submitPortalRun(srdcKey, categoryID, runTime, variableID, link)


            

            

    print()
    print()
    print("Program will exit in 5 seconds...")
    time.sleep(10)

if __name__ == "__main__":
    main()