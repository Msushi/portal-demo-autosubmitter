import sys
import os
import time
from demo_parser import *
from settings import *
from category_game_wrapper import *
from google_drive_helper import *
from speedrundotcom_helper import *

def main(): 
    if len(sys.argv) == 1:
        gapiKey, srdcKey = getAPIKeys()
        print("No demo file.")
        mapName, ticks = parse_demo("C:/coding/portal-demo-autosubmitter/dist/14il_msushi_1061.dem")
        game, IL, category, runTime = categoryDetection([mapName], [ticks])
        link = uploadFileToDrive("C:/coding/portal-demo-autosubmitter/dist/14il_msushi_1061.dem", gapiKey)
        print(link)
        

        submitRun(srdcKey, category, IL, runTime, ticks, link)
        print("Done")
    else:
        gapiKey, srdcKey = getAPIKeys()
        if len(sys.argv) == 2:
            mapName, ticks = parse_demo(sys.argv[1])
            game, IL, category, runTime = categoryDetection([mapName], [ticks])
            link = uploadFileToDrive(sys.argv[1], gapiKey)
            submitRun(srdcKey, category, IL, runTime, ticks, link)

    print()
    print()
    print("Program will exit in 5 seconds...")
    time.sleep(5)

if __name__ == "__main__":
    main()