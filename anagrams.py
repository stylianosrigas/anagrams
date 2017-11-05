#https://www.codeproject.com/Articles/498404/TDD-the-Anagrams-Kata


# Write a program to generate all potential anagrams of an input string. 
# For example, the potential anagrams of "biro" are 
# biro bior brio broi boir bori 
# ibro ibor irbo irob iobr iorb 
# rbio rboi ribo riob roib robi 
# obir obri oibr oirb orbi orib  
########################################################################################
 # def of(x):
	# return ""
########################################################################################
# def of(x):
# 	if x == "":
# 		return ""
# 	else:
# 		return x
########################################################################################
# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	else:
# 		return ["AB", "BA"]

########################################################################################
# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	else:
# 		return [x,  x[1:2] + x[:1]]

########################################################################################
# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		"ABC", 
# 		"ACB", 
# 		"BAC", 
# 		"BCA", 
# 		"CAB", 
# 		"CBA"
# 		]
########################################################################################

# There is a pattern above

# [
#    "A" + "BC", 
#    "A" + "CB", 
#    "B" + "AC", 
#    "B" + "CA", 
#    "C" + "AB", 
#    "C" + "BA"
# ]


# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		"A" + "BC", 
# 		"A" + "CB", 
# 		"B" + "AC", 
# 		"B" + "CA", 
# 		"C" + "AB", 
# 		"C" + "BA"
# 		]
########################################################################################
# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		x[:1] + "BC", 
# 		x[:1] + "CB", 
# 		x[1:2] + "AC", 
# 		x[1:2] + "CA", 
# 		x[2:3] + "AB", 
# 		x[2:3] + "BA"
# 		]
########################################################################################
# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		x[:1] + of("BC")[0], 
# 		x[:1] + of("BC")[1], 
# 		x[1:2] + "AC", 
# 		x[1:2] + "CA", 
# 		x[2:3] + "AB", 
# 		x[2:3] + "BA"
# 		]

########################################################################################

# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		x[:1] + of("BC")[0], 
# 		x[:1] + of("BC")[1], 
# 		x[1:2] + of("AC")[0], 
# 		x[1:2] + of("AC")[1], 
# 		x[2:3] + of("AB")[0], 
# 		x[2:3] + of("AB")[1]
# 		]
########################################################################################
# With the above procedure we eliminated half of the literal values 

# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		x[:1] + of(dropcharacter(x,0))[0], 
# 		x[:1] + of(dropcharacter(x,0))[1], 
# 		x[1:2] + of("AC")[0], 
# 		x[1:2] + of("AC")[1], 
# 		x[2:3] + of("AB")[0], 
# 		x[2:3] + of("AB")[1]
# 		]

# def dropcharacter(s, index):
# 	return "BC"
########################################################################################

# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		x[:1] + of(dropcharacter(x,0))[0], 
# 		x[:1] + of(dropcharacter(x,0))[1], 
# 		x[1:2] + of(dropcharacter(x,1))[0], 
# 		x[1:2] + of(dropcharacter(x,1))[1], 
# 		x[2:3] + of("AB")[0], 
# 		x[2:3] + of("AB")[1]
# 		]

# def dropcharacter(s, index):
# 	if index == 0:
# 		return "BC"
# 	else: 
# 		return "AC"
########################################################################################

# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		x[:1] + of(dropcharacter(x,0))[0], 
# 		x[:1] + of(dropcharacter(x,0))[1], 
# 		x[1:2] + of(dropcharacter(x,1))[0], 
# 		x[1:2] + of(dropcharacter(x,1))[1], 
# 		x[2:3] + of(dropcharacter(x,2))[0], 
# 		x[2:3] + of(dropcharacter(x,2))[1]
# 		]

# def dropcharacter(x, index):
# 	if index == 0:
# 		return "BC"
# 	elif index == 1: 
# 		return "AC"
# 	else:
# 		return "AB"
########################################################################################
# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		x[:1] + of(dropcharacter(x,0))[0], 
# 		x[:1] + of(dropcharacter(x,0))[1], 
# 		x[1:2] + of(dropcharacter(x,1))[0], 
# 		x[1:2] + of(dropcharacter(x,1))[1], 
# 		x[2:3] + of(dropcharacter(x,2))[0], 
# 		x[2:3] + of(dropcharacter(x,2))[1]
# 		]

# def dropcharacter(x, index):
# 	if index == 0:
# 		return x[1:3]
# 	elif index == 1: 
# 		return x[0:1] + x[2:3]
# 	else:
# 		return x[0:2]

########################################################################################

# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		x[:1] + of(dropcharacter(x,0))[0], 
# 		x[:1] + of(dropcharacter(x,0))[1], 
# 		x[1:2] + of(dropcharacter(x,1))[0], 
# 		x[1:2] + of(dropcharacter(x,1))[1], 
# 		x[2:3] + of(dropcharacter(x,2))[0], 
# 		x[2:3] + of(dropcharacter(x,2))[1]
# 		]

# def dropcharacter(x, index):
# 	if index == 0:
# 		return x[1:3]
# 	elif index == 1: 
# 		return x[0:1] + x[2:3]
# 	else:
# 		return x[0:2]

########################################################################################

# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		x[:1] + of(dropcharacter(x,0))[0], 
# 		x[:1] + of(dropcharacter(x,0))[1], 
# 		x[1:2] + of(dropcharacter(x,1))[0], 
# 		x[1:2] + of(dropcharacter(x,1))[1], 
# 		x[2:3] + of(dropcharacter(x,2))[0], 
# 		x[2:3] + of(dropcharacter(x,2))[1]
# 		]

# def dropcharacter(x, index):
# 	if index == 0:
# 		return x[1:3]
# 	elif index == 1: 
# 		return x[0:index] + x[2:3]
# 	else:
# 		return x[0:index]

########################################################################################

# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		x[:1] + of(dropcharacter(x,0))[0], 
# 		x[:1] + of(dropcharacter(x,0))[1], 
# 		x[1:2] + of(dropcharacter(x,1))[0], 
# 		x[1:2] + of(dropcharacter(x,1))[1], 
# 		x[2:3] + of(dropcharacter(x,2))[0], 
# 		x[2:3] + of(dropcharacter(x,2))[1]
# 		]

# def dropcharacter(x, index):
# 	before = x[0:index]
# 	if index == 0:
# 		return x[1:3]
# 	elif index == 1: 
# 		return before + x[2:3]
# 	else:
		# return before

########################################################################################


# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		x[:1] + of(dropcharacter(x,0))[0], 
# 		x[:1] + of(dropcharacter(x,0))[1], 
# 		x[1:2] + of(dropcharacter(x,1))[0], 
# 		x[1:2] + of(dropcharacter(x,1))[1], 
# 		x[2:3] + of(dropcharacter(x,2))[0], 
# 		x[2:3] + of(dropcharacter(x,2))[1]
# 		]

# def dropcharacter(x, index):
# 	before = x[0:index]
# 	if index == 0:
# 		return x[index + 1:3]
# 	elif index == 1: 
# 		return before + x[index + 1:3]
# 	else:
# 		return before


########################################################################################


# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		x[:1] + of(dropcharacter(x,0))[0], 
# 		x[:1] + of(dropcharacter(x,0))[1], 
# 		x[1:2] + of(dropcharacter(x,1))[0], 
# 		x[1:2] + of(dropcharacter(x,1))[1], 
# 		x[2:3] + of(dropcharacter(x,2))[0], 
# 		x[2:3] + of(dropcharacter(x,2))[1]
# 		]

# def dropcharacter(x, index):
# 	before = x[0:index]
# 	if index == 0:
# 		return x[index + 1:len(x)]
# 	elif index == 1: 
# 		return before + x[index + 1:len(x)]
# 	else:
# 		return before

########################################################################################


# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		x[:1] + of(dropcharacter(x,0))[0], 
# 		x[:1] + of(dropcharacter(x,0))[1], 
# 		x[1:2] + of(dropcharacter(x,1))[0], 
# 		x[1:2] + of(dropcharacter(x,1))[1], 
# 		x[2:3] + of(dropcharacter(x,2))[0], 
# 		x[2:3] + of(dropcharacter(x,2))[1]
# 		]

# def dropcharacter(x, index):
# 	before = x[0:index]
# 	after = x[index + 1:len(x)]
# 	if index == 0:
# 		return after
# 	elif index == 1: 
# 		return before + after
# 	else:
# 		return before


########################################################################################


# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		return [
# 		x[:1] + of(dropcharacter(x,0))[0], 
# 		x[:1] + of(dropcharacter(x,0))[1], 
# 		x[1:2] + of(dropcharacter(x,1))[0], 
# 		x[1:2] + of(dropcharacter(x,1))[1], 
# 		x[2:3] + of(dropcharacter(x,2))[0], 
# 		x[2:3] + of(dropcharacter(x,2))[1]
# 		]

# def dropcharacter(x, index):
# 	before = x[0:index]
# 	after = x[index + 1:len(x)]
# 	return before + after
	
########################################################################################


# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		anagrams = []
# 		for i in range(0,3):
# 			anagrams.append(x[i:i+1] + of(dropcharacter(x,i))[0])
# 			anagrams.append(x[i:i+1] + of(dropcharacter(x,i))[1])
# 		return anagrams

# def dropcharacter(x, index):
# 	before = x[0:index]
# 	after = x[index + 1:len(x)]
# 	return before + after

########################################################################################


# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		anagrams = []
# 		for i in range(0,3):
# 			for j in range(0,2):
# 				anagrams.append(x[i:i+1] + of(dropcharacter(x,i))[j])
# 		return anagrams

# def dropcharacter(x, index):
# 	before = x[0:index]
# 	after = x[index + 1:len(x)]
# 	return before + after


########################################################################################

# def of(x):
# 	if len(x) <= 1:
# 		return x
# 	elif len(x) == 2:
# 		return [x,  x[1:2] + x[:1]]
# 	else:
# 		anagrams = []
# 		for i in range(0,len(x)):
# 			for j in range(0,len(x)-1):
# 				anagrams.append(x[i:i+1] + of(dropcharacter(x,i))[j])
# 		return anagrams

# def dropcharacter(x, index):
# 	before = x[0:index]
# 	after = x[index + 1:len(x)]
# 	return before + after

########################################################################################

def of(x):
	if len(x) <= 1:
		return x
	elif len(x) == 2:
		return [x,  x[1:2] + x[:1]]
	else:
		anagrams = []
		for i in range(0,len(x)):
			for j in range(0,len(of(dropcharacter(x,i)))):
				anagrams.append(x[i:i+1] + of(dropcharacter(x,i))[j])
		return anagrams

def dropcharacter(x, index):
	before = x[0:index]
	after = x[index + 1:len(x)]
	return before + after

########################################################################################
