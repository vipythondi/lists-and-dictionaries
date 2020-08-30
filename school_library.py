books = input().split("&")
command = input()

while command != "Done":
    book = command.split(" | ")
    if book[0] == "Add Book":
        book_name = book[1]
        if book_name not in books:
            books.insert(0, book_name)
    elif book[0] == "Take Book":
        book_name = book[1]
        if book_name in books:
            books.remove(book_name)
    elif book[0] == "Swap Books":
        book1=book[1]
        book2=book[2]
        b1=books.index(book1)
        b2 = books.index(book2)
        if book1 in books and book2 in books:
            books[b1], books[b2] = books[b2], books[b1]
    elif book[0] == "Insert Book":
        book_name = book[1]
        books.append(book_name)
    elif book[0] == "Check Book":
        index = int(book[1])
        if 0 <= index < (len(books)):
            print(books[index])
    command = input()
print(", ".join(books))