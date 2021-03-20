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

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(jokes=1, word_repeat=True):
    """
    @param jokes: number of jokes from 1 to infinite
    @type jokes: int
    @param word_repeat: True(default) for repeat words in jokes, False to prevent it
    @type word_repeat: bool
    @return: list of jokes
    @rtype: list
    """
    if type(word_repeat) != bool:
        raise Exception(f'parameter word_repeat must be empty or bool')

    nouns_copy = nouns.copy()
    adverbs_copy = adverbs.copy()
    adjectives_copy = adjectives.copy()
    jokes_result = []

    for i in range(jokes):
        try:
            noun = random.choice(nouns_copy)
            adverb = random.choice(adverbs_copy)
            adjective = random.choice(adjectives_copy)
            joke = f'{noun} {adverb} {adjective}'
            jokes_result.append(joke)

            if word_repeat is False:
                nouns_copy.pop(nouns_copy.index(noun))
                adverbs_copy.pop(adverbs_copy.index(adverb))
                adjectives_copy.pop(adjectives_copy.index(adjective))
        except IndexError:
            print('Были использованы все слова для составления загадок')
            break

    return jokes_result


print('Вызов функции без аргументов:')
print(get_jokes())

print('\nВызов функции с первым аргументом:')
print(get_jokes(5))

print('\nВызов функции с обоими аргументами, без повтора слов'
      '\nи с превышением лимита слов:')
print(get_jokes(7, word_repeat=False))

# закоментил, чтобы лишний раз не стреляло
# print('\nВызов функции с обоими аргументами, без повтора слов'
#       '\nи с превышением лимита слов:')
# get_jokes(7, word_repeat='qqq')
