def parse_demo(filePath):
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
            if (messageType != 3):
                print("Error in messagetype")
                print(messageType)

        messageType = int.from_bytes(data[readBuffer:readBuffer+1], byteorder='little')
        readBuffer += 1

    print(name)
    print(map)
    print(maxTick)

    return map, maxTick