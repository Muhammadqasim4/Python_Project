import json
import os

# 📁 File for saving/loading data
FILE_NAME = "library.txt"

# 📚 Load library from file
def load_library():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# 💾 Save library to file
def save_library(library):
    with open(FILE_NAME, "w") as file:
        json.dump(library, file)

# 📘 Add a book
def add_book(library):
    print("\n📘 Add a Book")
    try:
        book = {
            'title': input("Title: "),
            'author': input("Author: "),
            'year': int(input("Publication Year: ")),
            'genre': input("Genre: "),
            'read': input("Read? (yes/no): ").strip().lower().startswith("y")
        }
        library.append(book)
        print("✅ Book added!")
    except ValueError:
        print("⚠️ Invalid year! Please enter a number.")

# ❌ Remove a book
def remove_book(library):
    print("\n❌ Remove a Book")
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print("✅ Book removed.")
            return
    print("⚠️ Book not found.")

# 🔍 Search for a book
def search_book(library):
    print("\n🔍 Search Book")
    keyword = input("Enter title or author to search: ").lower()
    results = [
        book for book in library
        if keyword in book['title'].lower() or keyword in book['author'].lower()
    ]
    if results:
        print("🔎 Matching Books:")
        for idx, book in enumerate(results, start=1):
            status = 'Yes' if book['read'] else 'No'
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) | Genre: {book['genre']} | Read: {status}")
    else:
        print("⚠️ No matching books found.")

# 📚 Display all books
def display_books(library):
    print("\n📚 All Books in Library:")
    if not library:
        print("Library is empty.")
        return
    for idx, book in enumerate(library, start=1):
        status = 'Yes' if book['read'] else 'No'
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) | Genre: {book['genre']} | Read: {status}")

# 📊 Display statistics
def display_stats(library):
    print("\n📊 Library Statistics")
    total = len(library)
    if total == 0:
        print("No books in the library yet.")
        return
    read_books = sum(1 for book in library if book['read'])
    percent = (read_books / total) * 100
    print(f"📚 Total books: {total}")
    print(f"📖 Books read: {read_books} ({percent:.2f}%)")

# 🚀 Main function
def main():
    library = load_library()

    print("📖 Welcome to Personal Library Manager")
    print("Your digital book collection starts here!")

    while True:
        print("\n=== MENU ===")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            save_library(library)
            print("💾 Library saved to file. 👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
