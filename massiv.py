voted = {}
def check_voter(name):
	if voted.get(name):
		print ("Go home")
	else: 
		voted[name] = True
		print ('Go voted')
check_voter("tom")
check_voter("garry")
check_voter("tom")