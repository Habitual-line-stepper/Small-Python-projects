# Import the sqlite3 module
import sqlite3


# Create a function to check if an integer is entered
def check_integer(user_input):
    # check if user input is an integer
    try:
        return int(input(user_input))
    # if not, recursively ask the user to enter an integer
    except ValueError:
        print("Please enter an integer\n")
        return check_integer(user_input)


def menu():
    # Create a menu for the user to select from
    user_menu = int(input("\n--MAIN MENU--\n"
                          "1. Enter book\n"
                          "2. Update book\n"
                          "3. Delete book\n"
                          "4. Search books\n"
                          "5. Show all books\n"
                          "0. Exit\n"))
    if user_menu == 1:
        enter_book()
    elif user_menu == 2:
        update_book()
    elif user_menu == 3:
        delete_book()
    elif user_menu == 4:
        search_books()
    elif user_menu == 5:
        show_all()
    elif user_menu == 0:
        print("Now exiting...")
        quit()
    else:
        print("Please enter a valid option from the menu.\n"
              "(1,2,3,4 or 0\n")
        menu()


# Connect to/create a database called ebookstore
db = sqlite3.connect('ebookstore')
# Create the cursor
cursor = db.cursor()
# Create the table
cursor.execute('''CREATE TABLE IF NOT EXISTS
books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, QTY INTEGER)''')
db.commit()
# Populate the table
books_list = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
              (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40),
              (3003, 'The Lion, the Witch and the Wardrobe', 'C.S.Lewis', 25),
              (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
              (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)]
# Use executemany to insert multiple rows
cursor.executemany(''' INSERT or IGNORE INTO books(id, Title, Author, QTY) 
VALUES(?,?,?,?)''', books_list)
db.commit()


def enter_book():
    # Get user input
    # Use the function check() to check input where an integer is required
    book_identification = check_integer("Please enter an ID number for the book:\n")
    book_title = input("Please enter the book title:\n")
    book_author = input("Please enter the books author:\n")
    book_qty = check_integer("Please enter the quantity of the book currently in stock:\n")

    # Combine the input into a single variable
    new_book = (book_identification, book_title, book_author, book_qty)
    # Insert the input into the table
    cursor.execute(''' INSERT INTO books(id, Title, Author, QTY) 
    VALUES(?,?,?,?)''', new_book)
    db.commit()
    print("New book added successfully!")
    menu()


def update_book():
    # Ask the user to enter the book ID
    book_identification = check_integer("Please enter the book ID number:\n")
    # Ask the user what they would like to update
    user_selection = int(input("What would you like to update?\n"
                               "1. ID\n"
                               "2. Title\n"
                               "3. Author\n"
                               "4. Quantity\n"
                               "5. Return to the main menu\n"))
    # If the user selects option 1
    if user_selection == 1:
        # ask them to enter the new ID
        change_identification = check_integer("Please enter a new ID number for the book:\n")
        id = (change_identification, book_identification,)
        # update the ID and save
        cursor.execute('''UPDATE books SET id = ? WHERE id = ?''', id)
        db.commit()
    # If the user selects option 2
    elif user_selection == 2:
        # ask the user to enter the new book title
        book_title = input("Please enter the new book title:\n")
        id = (book_title, book_identification,)
        # update and save
        cursor.execute('''UPDATE books SET Title = ? WHERE id = ?''', id)
        db.commit()
    # If the user selects option 3
    elif user_selection == 3:
        # ask the user to enter the new book author
        book_author = input("Please enter the books author:\n")
        id = (book_author, book_identification,)
        # update and save
        cursor.execute('''UPDATE books SET Author = ? WHERE id = ?''', id)
        db.commit()
    # If the user selects option 4
    elif user_selection == 4:
        # ask the user to enter the new quantity
        book_qty = check_integer("Please enter the quantity of the book currently in stock:\n")
        id = (book_qty, book_identification)
        cursor.execute('''UPDATE books SET QTY = ? WHERE id = ?''', id)
        db.commit()
    # return to the menu if user inputs 5
    elif user_selection == 5:
        menu()
    # else tell the user to enter a valid option
    else:
        print("Please select a valid option\n")
        update_book()
    print("Changes saved")
    menu()


def delete_book():
    # ask for the book ID
    book_identification = check_integer("Please enter the book ID number:\n")
    # use DELETE FROM and where to delete the row
    cursor.execute('''DELETE FROM books where id = ?''', (book_identification,))
    db.commit()
    print("Book deleted")
    menu()


def search_books():
    # Ask for the book ID
    book_identification = check_integer("Please enter the book ID number:\n")
    # Select the row where id = id entered by the user
    cursor.execute('''SELECT * FROM books WHERE id = ?''', (str(book_identification),))
    # employ fetchone to retrieve the row and save it in a variable
    search = cursor.fetchone()
    # if search is None (empty/nothing found/does not exist)
    if search is None:
        # tell the user nothing is found
        print("Book not found! Please enter a valid ID:\n")
        search_books()
    # else print the data using map and convert the tuple list into a string
    else:
        print("\n")
        print(f"{', '.join(map(str, search))}")
        menu()


def show_all():
    # select every row in books
    with db:
        cursor.execute("SELECT * FROM BOOKS")
        # use fetch all to fetch all the data from the table
        fetching_all = cursor.fetchall()
        # for each row in fetching all
        for book in fetching_all:
            # print the row out and join on the ','
            print(f"{', '.join(map(str, book))}")
    menu()


menu()
