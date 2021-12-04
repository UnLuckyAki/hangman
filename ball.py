import random
HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
 =========''','''
    +---+
    |   |
    O   |
        |
        |
        |
 =========''','''
    +---+
    |   |
    O   |
    |   |
        |
        |
 =========''','''
    +---+
    |   |
    O   |
   /|   |
        |
        |
 =========''','''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
 =========''','''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
 =========''','''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
 =========''']
words = 'муравей бабуин барсук медведь бобр верблюд кошка моллюск кобра пума койот ворона олень собака осел утка орел хорек лиса лягушка коза гусь ястреб ящерица лама моль обезьяна лось мышь мул тритон выдра сова панда попугай голубь питон кролик баран крыса носорог лосось акула змея паук аист лебедь тигр жаба форель индейка черепаха ласка кит волк вомбат зебра'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters,secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    print('Неправильные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks = "*"*len(secretWord)
    #Заменяем звездочки на правильно угаданные буквы
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    # Показываем загаданное слово с пробелами между букв
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        guess = input('Введите букву: ').lower()
        if len(guess) != 1:
            print('Неверное количество')
        elif guess in alreadyGuessed:
            print('Вы уже пробовали угадать'
                  'эту букву. Выберите другую.')
        elif guess not in 'ёйцукенгшщзхъфывапролджэячсмитьбю':
            print('Пожалуйста, введите букву кириллицы')
        else:
            return guess

def playAgain():
    print('Хотите попробовать еще раз? ("Да" или "Нет")')
    return input().lower().startswith('д')

missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters,secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Проверка условия победы игрока
        foundAllLetters =True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Вы победили и отгадали: '+ secretWord)
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, secretWord)
            print(f'Ты приограл!\nПосле '+str(len(missedLetters))+' ошибок и '+ str(len(correctLetters))+ ' угаданных букв.\nЗагаданное слово: '+ secretWord)
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)
            gameIsDone = False
    else:
        break
