class Book(object):
    def __init__(
        self,
        upc,
        title,
        genre,
        product_type,
        price_with_tax,
        price_excl_tax,
        tax,
        qty,
        rating,
        description,
    ):
        self.upc = upc
        self.title = title
        self.genre = genre
        self.product_type = product_type
        self.price_with_tax = price_with_tax
        self.price_excl_tax = price_excl_tax
        self.tax = tax
        self.qty = qty
        self.rating = rating
        self.description = description

    @property
    def upc(self):
        return self.__upc

    @upc.setter
    def upc(self, value):
        if len(value) < 16:
            raise ValueError("Incorrect UPC length!")
        self.__upc = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Book title cannot be None!")
        self.__title = value

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        if not value:
            raise ValueError("Genre cannot be None!")
        self.__genre = value

    @property
    def product_type(self):
        return self.__product_type

    @product_type.setter
    def product_type(self, value):
        if value.lower() != "books":
            raise ValueError("Product type must be a book!")
        self.__product_type = value

    @property
    def price_with_tax(self):
        return self.__price_with_tax

    @price_with_tax.setter
    def price_with_tax(self, value):
        if value == 0 or not value:
            self.__price_with_tax = "N\A"
            return
        self.__price_with_tax = value

    @property
    def price_excl_tax(self):
        return self.__price_excl_tax

    @price_excl_tax.setter
    def price_excl_tax(self, value):
        if value == 0 or not value:
            self.__price_excl_tax = "N\A"
            return
        self.__price_excl_tax = value

    @property
    def tax(self):
        return self.__tax

    @tax.setter
    def tax(self, value):
        if value < 0:
            raise ValueError("Tax cannot be a negative number!")
        self.__tax = value

    @property
    def qty(self):
        return self.__qty

    @qty.setter
    def qty(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be a negative number!")
        self.__qty = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError("Rating cannot be a negative number!")
        self.__rating = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if not value or str(value).isdigit():
            self.__description = "N\A"
            return
        self.__description = value
