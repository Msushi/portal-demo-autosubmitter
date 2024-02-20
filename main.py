import sys
import os
import time
from parse_demo import *;

def main(): 
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            print(arg)
            #parse(arg)
    else:
        print("none")
        parse("C:/coding/portal-demo-autosubmitter/dist/14il_msushi_1061.dem")
    
    time.sleep(5)

if __name__ == "__main__":
    main()