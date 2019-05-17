#This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode(): ##selects the function the program will be used for
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']: ##testing for word or letter
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".') ##reprompts user for valid input

def getMessage(): ##gets message from user
    print('Enter your message: ')
    return input()

def getKey():
    key = 0 #initializes data point
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())#forces input to be integer format
        if (key >= 1 and key <= MAX_KEY_SIZE):#makes sure key is not greater than cipher alphabet
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS):#the shift starts happening here depending on the length of the SYMBOL list and the key the student provides
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode() #calling functioons
message = getMessage()
key = getKey()
print('Your translated text is: ') #print statements
print(getTranslatedMessage(mode, message, key))#print statements