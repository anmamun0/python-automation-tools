def searcher():
    import time
    # Some 4 seconds time consuming tast
    book = "This is a book on mamun and code with mamun and good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print ('Your text is in the Book')

        else:
            print("Tex is not in the Book")

search = searcher()
next(search)
search.send('mamun')
input()
search.send('an')



# import random

# fast = ['this ', 'for', 'sec']
# var = random.choice(fast)
# print(var)