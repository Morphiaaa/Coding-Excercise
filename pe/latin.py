# if start letter is vowel, add 'ma' on the end of word
# if start letter is consonant, move this consonant to the end
# for the first word, append 'a' to it, for the second word, append 'aa' to it. repeat this for every word in the list.

def convert(sentence):
	if not sentence:
		return None

	word_list = sentence.split()

	res = []
	suffix = 'a'

	for word in word_list:
		temp = word
		if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
			temp = word + 'ma' + suffix
		else:
			temp = word[1:] + word[0] + suffix
		suffix += 'a'
		res.append(temp)

	return ' '.join(res)


print convert('I speak Goat Latin')