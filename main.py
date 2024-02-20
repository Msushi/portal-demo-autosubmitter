import sys
import os
import time
from parse_demo import *;
from settings import *;

def main(): 
    if len(sys.argv) == 1:
        getAPIKeys()
        print("No demo file.")
        parse("C:/coding/portal-demo-autosubmitter/dist/14il_msushi_1061.dem")
    else:
        getAPIKeys()
        if len(sys.argv) == 2:
            for arg in sys.argv[1:]:
                print(arg)
                parse(arg)

    time.sleep(5)

if __name__ == "__main__":
    main()