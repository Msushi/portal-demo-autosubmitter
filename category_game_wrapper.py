def getSubmissionInfo(maps, ticks, wakeup):
	game = getGameFromMap(maps[0])
	isIL = ILDetection(game, maps)
	variableID = "Not Set"
	levelText = "Not Set"
	levelID = "Not Set"
	if isIL:
		levelText, levelID = getIL(game, maps[0])
	categoryText, categoryID, variableID = getCategoryFromUser(game, isIL)
	totalTicks = 0
	for tick in ticks:
		totalTicks += tick
	if game == "Portal":
		#Add vault save time if we never detected a wakeup start.
		if not wakeup and not isIL:
			totalTicks += 3535
		totalTicks += len(ticks)
		time = totalTicks * 0.015
	
	return game, isIL, levelID, categoryID, time, totalTicks, variableID, levelText, categoryText

def ILDetection(game, maps):
	uniqueMaps = set(maps)
	if game == "Portal":
		return len(maps) == 1
	if game == "Portal 2":
		pass

def getCategoryFromUser(game, isIL):
	category = 'z'
	loops = 0
	print("What category is this speedrun?")
	print()
	print()
	if (game == "Portal"):
		if (isIL):
			print("o - Out of Bounds")
			print("i - Inbounds")
			print("g - Glitchless")
			while not(category == 'o' or category == 'i' or category == 'g'):
				if loops > 0:
					print("That is not a valid category. Please try again.")
				print()
				category = input()
				category = category.lower()
				loops += 1
			if (category == 'o'):
				return "Out of Bounds", "xw20jzkn", "Not Set"
			elif (category == "i"):
				return "Inbounds", "xwdmg4dq", "Not Set"
			else:
				return "Glitchless", "02qoxl7k", "Not Set"
		else:
			print("o - Out of Bounds")
			print("i - Inbounds")
			print("g - Glitchless")
			print("l - Inbounds No SLA Legacy")
			print("u - Inbounds No SLA Unrestricted")
			while not(category == 'o' or category == 'i' or category == 'g' or category == "l" or category == "u"):
				if loops > 0:
					print("That is not a valid category. Please try again.")
				print()
				category = input()
				category = category.lower()
				loops += 1
			if (category == 'o'):
				return "Out of Bounds", "lvdowokp", "Not Set"
			elif (category == "i"):
				return "Inbounds", "7wkp6v2r", "Not Set"
			elif (category == "g"):
				return "Glitchless", "wk6pexd1", "Not Set"
			elif (category == "l"):
				return "Inbounds NoSLA Legacy", "n2yq98ko", "jqz97g41"
			elif (category == "u"):
				return "Inbounds NoSLA Legacy", "n2yq98ko", "21g5r9xl"

def getGameFromMap(firstMap):
	portalMaps = ["testchmb_a_00", "testchmb_a_01", "testchmb_a_02", "testchmb_a_03", "testchmb_a_04", "testchmb_a_05", "testchmb_a_06", "testchmb_a_07", "testchmb_a_08", "testchmb_a_09", "testchmb_a_10", "testchmb_a_11", "testchmb_a_13", "testchmb_a_14", "testchmb_a_15", "escape_00", "escape_01", "escape_02"]
	portal2Maps = ["sp_a1_intro1", "sp_a1_intro2", "sp_a1_intro3", "sp_a1_intro4", "sp_a1_intro5", "sp_a1_intro6", "sp_a1_intro7", "sp_a1_wakeup", "sp_a2_intro", "sp_a2_laser_intro", "sp_a2_laser_stairs", "sp_a2_dual_lasers", "sp_a2_laser_over_goo", "sp_a2_catapult_intro", "sp_a2_trust_fling", "sp_a2_pit_flings", "sp_a2_fizzler_intro", "sp_a2_sphere_peek", "sp_a2_ricochet", "sp_a2_bridge_intro", "sp_a2_bridge_the_gap", "sp_a2_turret_intro", "sp_a2_laser_relays", "sp_a2_turret_blocker", "sp_a2_laser_vs_turret", "sp_a2_pull_the_rug", "sp_a2_column_blocker", "sp_a2_laser_chaining", "sp_a2_triple_laser", "sp_a2_bts1", "sp_a2_bts2", "sp_a2_bts3", "sp_a2_bts4", "sp_a2_bts5", "sp_a2_bts6", "sp_a2_core", "sp_a3_00", "sp_a3_01", "sp_a3_03", "sp_a3_jump_intro", "sp_a3_bomb_flings", "sp_a3_crazy_box", "sp_a3_transition01", "sp_a3_speed_ramp", "sp_a3_speed_flings", "sp_a3_portal_intro", "sp_a3_end", "sp_a4_intro", "sp_a4_tb_intro", "sp_a4_tb_trust_drop", "sp_a4_tb_wall_button", "sp_a4_tb_polarity", "sp_a4_tb_catch", "sp_a4_stop_the_box", "sp_a4_laser_catapult", "sp_a4_laser_platform", "sp_a4_speed_tb_catch", "sp_a4_jump_polarity", "sp_a4_finale1", "sp_a4_finale2", "sp_a4_finale3", "sp_a4_finale4"]
	if firstMap in portalMaps:
		return "Portal"
	elif firstMap in portal2Maps:
		return "Portal 2"

def getIL(game, firstMap):
	if (firstMap == "testchmb_a_00"):
		return "00-01", "x5d73q9y"
	elif (firstMap == "testchmb_a_01"): 
		return "02-03", "ykwje09g"
	elif (firstMap == "testchmb_a_02"):
		return "04-05", "nowo2jd6"
	elif (firstMap == "testchmb_a_03"):
		return "06-07", "jxd15zwo"
	elif (firstMap == "testchmb_a_04"):
		return "08", "lewpqy9n"
	elif (firstMap == "testchmb_a_05"):
		return "09", "3y9mpz95"
	elif (firstMap == "testchmb_a_06"):
		return "10", "q5wkrv94"
	elif (firstMap == "testchmb_a_07"):
		return "11-12", "p592o7d6"
	elif (firstMap == "testchmb_a_08"):
		return "13", "329vkqdv"
	elif (firstMap == "testchmb_a_09"):
		return "14", "8xd43q9m"
	elif (firstMap == "testchmb_a_10"):
		return "15", "7xd07mwq"
	elif (firstMap == "testchmb_a_11"):
		return "16", "4rw6npd7"
	elif (firstMap == "testchmb_a_13"):
		return "17", "kn9372d0"
	elif (firstMap == "testchmb_a_14"):
		return "18", "oz986rdl"
	elif (firstMap == "testchmb_a_15"):
		return "19", "krdn05wm"
	elif (firstMap == "escape_00"):
		return "e00", "zldyypd3"
	elif (firstMap == "escape_01"):
		return "e01", "kn9377d0"
	elif (firstMap == "escape_02"):
		return "e02", "oz9867dl"
	elif (firstMap == "testchmb_a_08_advanced"):
		return "Adv 13", "xd0kl849"
	elif (firstMap == "testchmb_a_09_advanced"):
		return "Adv 14", "rw6qrzgd"
	elif (firstMap == "testchmb_a_10_advanced"):
		return "Adv 15", "n93q8rzw"
	elif (firstMap == "testchmb_a_11_advanced"):
		return "Adv 16", "z98rexpd"
	elif (firstMap == "testchmb_a_13_advanced"):
		return "Adv 17", "rdnory7w"
	elif (firstMap == "testchmb_a_14_advanced"):
		return "Adv 18", "ldy1jord"
	else :
		print("No Level found")
