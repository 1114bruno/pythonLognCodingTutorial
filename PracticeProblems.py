
def mostFrequent(L):
	if len(L) == 0:
		return None
	counter = 0
	num = L[0]
	for i in L:
		frequency = L.count(i)
		if frequency>counter:
			counter = frequency
			num = i
	return num

print(mostFrequent([2, 5, 3, 4, 6, 4, 2, 4, 5]))


def mostFrequent2(L):
	maxValue = None
	maxCount = 0
	counts = dict()
	for element in L:
		count = counts.get(element,0) + 1
		counts[element] = count
		if count > maxCount:
			maxCount = count
			maxValue = element
	return maxValue



def testmostFrequent():
	print("testing...")
	assert(mostFrequent([2, 5, 3, 4, 6, 4, 2, 4, 5]) == 4)
	assert(mostFrequent([2, 3, 4, 3, 5, 3, 6, 3, 7]) == 3)
	assert(mostFrequent([42]) == 42)
	assert(mostFrequent([]) == None)
	print("done")
print(testmostFrequent())




def awards(oscarResults):

	oscar = dict(list(oscarResults))
	names = list(oscar.values())
	frequency = {}
	for name in names:
		if name in frequency:
			frequency[name] += 1
		else:
			frequency[name] = 1
	
	return frequency


print(awards({("Best Picture", "Green Book"), ("Best Actor", "Bohemian Rhapsody"), ("Best Actress", "The Favourite"), ("Film Editing", "Bohemian Rhapsody"), ("Best Original Score", "Black Panther"), ("Costume Design", "Black Panther"), ("Sound Editing", "Bohemian Rhapsody"), ("Best Director", "Roma")}))









