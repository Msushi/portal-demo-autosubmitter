def parse(filePath):
    f = open(filePath, 'rb')
    data = f.read()
    f.close()

    name = data[276:536]
    map = data[536:796]

    maxTick = -1
    tick = 0
    readBuffer = 1072
    messageType = int.from_bytes(data[readBuffer:readBuffer+1], byteorder='little')
    readBuffer += 1

    
    while (messageType != 7):
        tick = int.from_bytes(data[readBuffer:readBuffer+4], byteorder='little')
        print(tick)
        readBuffer += 4

        if (tick < 4294964510 and tick > maxTick):
            maxTick = tick
        
        if (messageType == 1 or messageType == 2):
            readBuffer += 84
            readBuffer += (int.from_bytes(data[readBuffer:readBuffer+4], byteorder="little") + 4)
        elif (messageType == 4 or messageType == 6 or messageType == 8 or messageType == 9):
            readBuffer += (int.from_bytes(data[readBuffer:readBuffer+4], byteorder="little") + 4)
        elif (messageType == 5):
            readBuffer += 4
            readBuffer += (int.from_bytes(data[readBuffer:readBuffer+4], byteorder="little") + 4)
        else:
            print("Error in messagetype")

        messageType = int.from_bytes(data[readBuffer:readBuffer+1], byteorder='little')
        readBuffer += 1

    print(name)
    print(map)
    print(maxTick)