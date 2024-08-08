import random# Use an import statement at the top

word_file = "Downloads/words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

def generate_password():
	words = random.sample(word_list, 3)# Add your function generate_password here
	password = '_'.join(words)# It should return a string consisting of three random words 
	return password# concatenated together without spaces



# test your function
print(generate_password())