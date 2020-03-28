import random
import time
a = 'а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я'
alphabet = a.split(', ')


def main(word):
    ch = 0
    monkey_word = ''
    while True:
        monkey_word += random.choice(alphabet)
        ch += 1
        if len(monkey_word) >= len(word):
            if word in monkey_word:
                return [monkey_word, ch]
            monkey_word = monkey_word[1:]

start=time.time()
answ = main('короная')
end=time.time()-start
print(answ, end)
