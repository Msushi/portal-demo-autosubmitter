def categoryDetection(maps, ticks):
	game = getGameFromMap(maps[0])
	IL = getIL(game, maps[0])
	category = getCategoryFromUser(game, IL)
	totalTicks = 0
	for tick in ticks:
		totalTicks += tick
	if game == "4pd0n31e":
		totalTicks += len(ticks)
		time = totalTicks * 0.015
	
	return game, IL, category, time

def getCategoryFromUser(game, IL):
	category = 'z'
	loops = 0
	print("What category is this speedrun?")
	print()
	print()
	if (game == "4pd0n31e"): #Portal
		print("o - Out of Bounds")
		print("i - Inbounds")
		print("g - Glitchless")
		while not(category == 'o' or category == 'i' or category == 'g'):
			if loops > 0:
				print("That is not a valid category. Please try again.")
			category = input()
			category = category.lower()
			loops += 1
		if (category == 'o'):
			return "xw20jzkn"
		elif (category == "i"):
			return "xwdmg4dq"
		else:
			return "02qoxl7k"
	

def getGameFromMap(firstMap):
    if (firstMap == "testchmb_a_00" or firstMap == "testchmb_a_01" or firstMap == "testchmb_a_02" or firstMap == "testchmb_a_03"
	or firstMap == "testchmb_a_04" or firstMap == "testchmb_a_05" or firstMap == "testchmb_a_06" or firstMap == "testchmb_a_07"
	or firstMap == "testchmb_a_08" or firstMap == "testchmb_a_09" or firstMap == "testchmb_a_10" or firstMap == "testchmb_a_11"
	or firstMap == "testchmb_a_13" or firstMap == "testchmb_a_14" or firstMap == "testchmb_a_15" or firstMap == "escape_00"
	or firstMap == "escape_01" or firstMap == "escape_02" or firstMap == "testchmb_a_08_advanced" or firstMap == "testchmb_a_09_advanced"
	or firstMap == "testchmb_a_08_advanced" or firstMap == "testchmb_a_09_advanced" or firstMap == "testchmb_a_10_advanced"
	or firstMap == "testchmb_a_11_advanced" or firstMap == "testchmb_a_12_advanced" or firstMap == "testchmb_a_13_advanced"):
        return "4pd0n31e"
    elif (firstMap == "sp_a1_intro1" or firstMap == "sp_a2_laser_intro" or firstMap == "sp_a2_sphere_peek"
    or firstMap == "sp_a2_column_blocker" or firstMap == "sp_a2_bts3" or firstMap == "sp_a3_00"
    or firstMap == "sp_a3_speed_ramp" or firstMap == "sp_a4_intro" or firstMap == "sp_a4_finale1"):
        return "om1mw4d2"

def getIL(game, firstMap):
	if (firstMap == "testchmb_a_00"):
		return "x5d73q9y"
	elif (firstMap == "testchmb_a_01"): 
		return "ykwje09g"
	elif (firstMap == "testchmb_a_02"):
		return "nowo2jd6"
	elif (firstMap == "testchmb_a_03"):
		return "jxd15zwo"
	elif (firstMap == "testchmb_a_04"):
		return "lewpqy9n"
	elif (firstMap == "testchmb_a_05"):
		return "3y9mpz95"
	elif (firstMap == "testchmb_a_06"):
		return "q5wkrv94"
	elif (firstMap == "testchmb_a_07"):
		return "p592o7d6"
	elif (firstMap == "testchmb_a_08"):
		return "329vkqdv"
	elif (firstMap == "testchmb_a_09"):
		return "8xd43q9m"
	elif (firstMap == "testchmb_a_10"):
		return "7xd07mwq"
	elif (firstMap == "testchmb_a_11"):
		return "4rw6npd7"
	elif (firstMap == "testchmb_a_13"):
		return "kn9372d0"
	elif (firstMap == "testchmb_a_14"):
		return "oz986rdl"
	elif (firstMap == "testchmb_a_15"):
		return "krdn05wm"
	elif (firstMap == "escape_00"):
		return "zldyypd3"
	elif (firstMap == "escape_01"):
		return "kn9377d0"
	elif (firstMap == "escape_02"):
		return "oz9867dl"
	elif (firstMap == "testchmb_a_08_advanced"):
		return "xd0kl849"
	elif (firstMap == "testchmb_a_09_advanced"):
		return "rw6qrzgd"
	elif (firstMap == "testchmb_a_10_advanced"):
		return "n93q8rzw"
	elif (firstMap == "testchmb_a_11_advanced"):
		return "z98rexpd"
	elif (firstMap == "testchmb_a_13_advanced"):
		return "rdnory7w"
	elif (firstMap == "testchmb_a_14_advanced"):
		return "ldy1jord"
	else :
		print("No Level found")
