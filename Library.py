#This program allows to make the basic library functionalities, 
 #like search a title, borrow and return a book.

import datetime
import json
import os

class Library:
    def __init__(self):
        # Lists
        self.books = []
        self.borrowBooks =[]
        # Dupla
        self.categorys = ("Ficción", "No ficción", "Ciencia", "Historia", "Biografía", 
                           "Poesía", "Infantil", "Técnico", "Cocina", "Viajes")
        # Set
        self.authors = set()
        self.titles = set()

    def addBook (self, title, author, category, year, unitCode):
        if category not in self.categorys:
            print(f"Invalid category. The available categorys are: {self.categorys}")
            return False
        # Create a dictionary for the book.
        book = {
            "id": len(self.books) + 1,
            "title": title,
            "author": author,
            "category": category,
            "year": year,
            "unitCode": unitCode,
            "available": True
        }
        # Updated sets and the list.
        self.authors.add(author)
        self.titles.add(title)
        self.books.append(book)
        print(f"the book '{title}' was update successfully.")
        return True
    
    
