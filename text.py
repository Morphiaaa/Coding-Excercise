class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type of words: string
        :type of maxWidth: int
        :retur type: List[string]
        """
        if len(words) == 0 or maxWidth == 0:
            return words
        
        cur, res, total_letters = [], [], 0
        
        words = collections.deque(words.split())
        # I use a deque to store all the words that splited from the input 'words'
        
        while words:
            if len(words[0]) + len(cur) + total_letters > maxWidth:  
            # if the current word can not be add into our current word list

                if len(cur) == 0:
                # this is the case that the first word in word list is a very long word whose length exceed the max length
                    rest = maxWidth - 1
                    cur.append(words[0][:rest] + '-')
                    temp = words.popleft()
                    words.appendleft(temp[rest:])
                    

                if len(cur) == 1:
                # this is the case that there is only one word in our cur word list and we can not put the curren word into it
                    if cur[-1][-1] != '-':
                        res.append(cur[0] + ' '*(maxWidth-total_letters))
                    else:
                    # if the current word is the rest part that the last word is splited.
                        res.append(cur[0])
                    
                if len(cur) > 1:
                # this is the case that there are more than one word in our current word list.
                    rest = maxWidth - total_letters - len(cur) - 1
                    cur.append(words[0][:rest] + '-')
                    temp = words.popleft()
                    words.appendleft(temp[rest:])

                    # put the spaces evenly into the slot of our current word list
                    for i in range(maxWidth - total_letters):
                        cur [i % (len(cur) - 1)] += ' '
                    
                    res.append(''.join(cur))
                
                # finished the current line
                cur = []
                total_letters = 0
            

            if len(words[0]) <= maxWidth:
                cur.append(words[0])
                total_letters += len(words[0])
                words.popleft()
            else:
                cur.append(words[0][:maxWidth-1] + '-')
                print 1
                total_letters += maxWidth
                temp = words.popleft()
                words.appendleft(temp[maxWidth-1:])
            
        # append the last line and fill the rest part of last line with spaces.
        res += [' '.join(cur).ljust(maxWidth)]
        
        return res
''''
test case 1
input: ('justification.', 6)
output: ["justi-","ficat-","ion   "]    

test case 2
input: ('This is my best friend in highshool', 10)
output: ["This is m-", "y best fr-", "iend in h-", "ighschool."]

test case 3
input: ('highschool', 20)
output: ["highschool.         "]


''''







