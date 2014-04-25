from os import system

def joReplace(song):
    #you = re.compile('you', re.IGNORECASE)
    you = re.compile('you|(baby)|honey|babe|she|woman|girl|lady', re.IGNORECASE)

    your = re.compile('your|You\\\\\'re|her', re.IGNORECASE)
    for line in song:
        for index in range(len(line)):
            if your.match(line[index]):
                line[index] = 'Joanna\\\'s'
            if you.match(line[index]):
                line[index] = 'The Joannas'
    return song

def txtToSpeech(song):
    for line in song:
        for word in line:
            system('say ' + word)



import sys, re
if __name__ == "__main__":
    inputFile = sys.argv[1]
    songFile = open(inputFile, 'r')
    song = []
    allChars = re.compile('^[a-zA-Z0-9\'\"()\-,.!?]+$')
    someChars = re.compile('[a-zA-Z0-9!?]$')
    quotes = re.compile('[\'\"]')
    for line in songFile:
        words = line.split(' ')
        newWordsList = []
        for word in words:
            word = allChars.match(word)
            if word:
                newWord = ''
                for char in word.group(0):
                    if someChars.match(char):
                        newWord += char
                    elif quotes.match(char):
                        newWord += '\\'
                        newWord += char
                newWordsList.append(newWord)
        if newWordsList:
            song.append(newWordsList)
    songFile.close()
    song = joReplace(song)
    txtToSpeech(song)
