"""This program will open a text document, 
identify words that are more than 2 characters 
long and consist entirely of letters, move the 
first letter to the end of the word, 
and then add ay at the end it will then put the 
words back into a single string, and create a text
doccument named <filename>-pigLatinized"""
#note, 2 letter consonnant sounds like CH and TH are an issue to deal with later


textFile = open(raw_input("type the filename you'd like to piglatinize!  "), "r+")
rawText = textFile.read()
words = rawText.split()


def modWord(w):
	
	first = str(w[0][0])
	minus = w[1:len(w)]
	combo = minus + first + "ay"
	return combo
	
	


newFile = open(textFile.name[0: len(textFile.name) - 4] + "_pigLatinized.txt", "w")


for j in range (0, len(words)):
	output = modWord(words[j])
	printable = output + "  \n" 
	newFile.write(printable)





	