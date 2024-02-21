import struct

def parse_demo(filePath):

    wakeupFound = False
    trueStartTick = 0

    with open(filePath, 'rb') as f:
        data = f.read()

    name = data[276:536]
    map = data[536:796]

    name = name.decode('utf-8').rstrip('\x00')
    map = map.decode('utf-8').rstrip('\x00')

    maxTick = -1
    tick = 0
    readBuffer = 1072
    messageType = int.from_bytes(data[readBuffer:readBuffer+1], byteorder='little')
    readBuffer += 1

    
    while (messageType != 7):
        tick = int.from_bytes(data[readBuffer:readBuffer+4], byteorder='little')
        readBuffer += 4

        if (tick < 4294960000 and tick > maxTick):
            maxTick = tick
        
        if (messageType == 1 or messageType == 2):
            #Testing for Portal 1 Wakeup
            if map == "testchmb_a_00": 
                if not wakeupFound:
                    vieworigin = data[readBuffer+4:readBuffer+16]
                    pos1 = struct.unpack('f', vieworigin[0:4])
                    pos2 = struct.unpack('f', vieworigin[4:8])
                    pos3 = struct.unpack('f', vieworigin[8:12])
                    if pos1[0] == -544.0 and pos2[0] == -368.75 and pos3[0] == 160.0:
                        wakeupFound = True
                        trueStartTick = tick+1

            readBuffer += 84
            readBuffer += (int.from_bytes(data[readBuffer:readBuffer+4], byteorder="little") + 4)
        elif (messageType == 4 or messageType == 6 or messageType == 8 or messageType == 9):
            #Testing for Portal 1 Ending
            if map == "escape_02" and messageType == 4: 
                consolecmdLength = int.from_bytes(data[readBuffer:readBuffer+4], byteorder="little")
                consolecmd = data[readBuffer+4:readBuffer+4+consolecmdLength]
                if consolecmd.decode('utf-8').rstrip('\x00') == "startneurotoxins 99999":
                    maxTick += 1
                    break
            readBuffer += (int.from_bytes(data[readBuffer:readBuffer+4], byteorder="little") + 4)
        elif (messageType == 5):
            readBuffer += 4
            readBuffer += (int.from_bytes(data[readBuffer:readBuffer+4], byteorder="little") + 4)
        else:
            if (messageType != 3):
                print("Error in messagetype")
                print(messageType)


        messageType = int.from_bytes(data[readBuffer:readBuffer+1], byteorder='little')
        readBuffer += 1

    

    maxTick = maxTick - trueStartTick

    return map, maxTick, wakeupFound