from os import system
#import pyttsx

def joReplace(song):
    #you = re.compile('you', re.IGNORECASE)
    you = re.compile('you|molly|bitch|(baby)|honey|babe|she|woman|girl|lady', re.IGNORECASE)

    your = re.compile('your|You\\\\\'re|her', re.IGNORECASE)
    for line in song:
        for index in range(len(line)):
            if your.match(line[index]):
                line[index] = 'Joanna\\\'s'
            if you.match(line[index]):
                line[index] = 'Joanna'
    return song

def txtToSpeech(song):
    #engine = pyttsx.init()
    #engine.setProperty('rate', 70)
    #voices = engine.getProperty('voices')
    #for voice in voices:
        #print "Using voice:", repr(voice)
        #engine.setProperty('voice', voice.id)
        #engine.say("Hi there, how's you ?")
        #engine.say("A B C D E F G H I J K L M")
        #engine.say("N O P Q R S T U V W X Y Z")
        #engine.say("0 1 2 3 4 5 6 7 8 9")
        #engine.say("Sunday Monday Tuesday Wednesday Thursday Friday Saturday")
        #engine.say("Violet Indigo Blue Green Yellow Orange Red")
        #engine.say("Apple Banana Cherry Date Guava")
    #engine.runAndWait()
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
