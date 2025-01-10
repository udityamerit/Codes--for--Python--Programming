def searcher():
    import time
    book = "this is a book on harray and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
next(search)
search.send("harry")
input("press any key")
search.send("harry and")

search.close()