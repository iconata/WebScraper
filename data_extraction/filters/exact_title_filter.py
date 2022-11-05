class ExactTitleFilter(object):
    """
    Search title in given titles_dict
    and returns url of matching book
    """
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        title = " ".join(value)
        self.__title = title.lower()

    def search_book_by_exact_title(self, titles_dict):
        if self.title in titles_dict:
            return titles_dict[self.title]
