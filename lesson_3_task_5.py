"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или
запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
Сможете ли вы сделать аргументы именованными?

"""
import random


def get_jokes(jokes=1, word_repeat=True):
    """
    @param jokes: number of jokes from 1 to infinite
    @type jokes: int
    @param word_repeat: True(default) for repeat words in jokes, False to prevent it
    @type word_repeat: bool
    @return: string compiled from 3 arrays
    @rtype: str
    """
    if type(word_repeat) != bool:
        raise Exception(f'parameter word_repeat must be empty or bool')

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    for i in range(jokes):
        try:
            noun = random.choice(nouns)
            adverb = random.choice(adverbs)
            adjective = random.choice(adjectives)
            joke = f'{noun} {adverb} {adjective}'

            if word_repeat is False:
                nouns.pop(nouns.index(noun))
                adverbs.pop(adverbs.index(adverb))
                adjectives.pop(adjectives.index(adjective))

        except IndexError:
            print('Кончились слова для составления загадок')
            break

        print(joke)


print('Вызов функции без аргументов:')
get_jokes()

print('\nВызов функции с первым аргументом:')
get_jokes(5)

print('\nВызов функции с обоими аргументами, без повтора слов'
      '\nи с превышением лимита слов:')
get_jokes(7, word_repeat=False)

# коментил, чтобы лишний раз не стреляло
# print('\nВызов функции с обоими аргументами, без повтора слов'
#       '\nи с превышением лимита слов:')
# get_jokes(7, word_repeat='qqq')
