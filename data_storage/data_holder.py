import json
import os
import books
from sorting import SortingMixin


class DataHolder(SortingMixin):
    def __init__(self):
        """
        Class constructor. Takes no arguments, but it creates an instances of
        class Book and SortingMixin, which are used to store book data and sort
        the list data struct, containing class instances for every book scraped.
        """
        self.book_cls = books.Book
        self.__data_struct = []
        self.sort = SortingMixin

    def add_entity(
        self,
        upc,
        title,
        genre,
        pr_type,
        price_it,
        price_et,
        tax,
        qty,
        rating,
        description,
    ):
        """
        Function to add a new book to the current collection.

        The collection is a list of class instances from type Book.

        @param upc: UPC of current book
        @param title: Title of current book
        @param genre: Genre of the current book
        @param pr_type: Product type of the current book
        @param price_it: Price including tax of the current book
        @param price_et: Price excluding tax of the current book
        @param tax: Tax amount of the current book
        @param qty: Quantity of the current book
        @param rating: Rating of the current book
        @param description: Description of the current book
        @return:
        """
        price_incl = float(price_it)
        price_excl = float(price_et)
        price_tax = float(tax)
        quantity = int(qty)

        self.__data_struct.append(
            books.Book(
                upc,
                title,
                genre,
                pr_type,
                price_incl,
                price_excl,
                price_tax,
                quantity,
                rating,
                description,
            )
        )

    def print_all_data(self, sorting, gui=None):
        """
        Prints all items in the stored data collection. The function creates a JSON file
        and saves it ${PROJECT_DIRECTORY}/output/${fileName}

        The function works with the current instance of class DataHolder
        @return: None
        """
        if not self.__data_struct:
            if gui:
                return None
            print("Collection is empty!")

        else:
            final_collection = {}

            for book in range(len(self.__data_struct)):
                final_collection[self.__data_struct[book].upc] = {
                    "Title": self.__data_struct[book].title,
                    "Genre": self.__data_struct[book].genre,
                    "Quantity": self.__data_struct[book].qty,
                    "Product_type": self.__data_struct[book].product_type,
                    "Price_excl_tax": self.__data_struct[book].price_excl_tax,
                    "Price_incl_tax": self.__data_struct[book].price_with_tax,
                    "Tax": self.__data_struct[book].tax,
                    "Rating": self.__data_struct[book].rating,
                    "Description": self.__data_struct[book].description,
                }

            if sorting:
                final_collection = SortingMixin.any_sort(final_collection, sorting)

            cwd = os.getcwd()
            path = os.path.join(cwd, "output")

            try:
                os.mkdir(path)
            except OSError:
                path = "output/"

            with open(os.path.join(path, "Book collection"), "w") as collection:
                collection.write(
                    json.dumps(final_collection, indent=2, encoding="latin-1")
                )
            if gui:
                return True
            print("JSON created successfully!")
            print("Collection JSON saved in output/Book collection.txt")
