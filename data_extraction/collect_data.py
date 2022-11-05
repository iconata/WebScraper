from data_extraction.extractors.book_data_extractor import BookDataExtractor
from data_extraction.filters.exact_title_filter import ExactTitleFilter
from data_extraction.filters.titles_filter import TitlesFilter
from data_extraction.filters.books_filter import BooksFilter
from data_extraction.request_handler import RequestHandler
from data_extraction.url_collector import UrlCollector
from data_storage.data_holder import DataHolder


BASE_URL = "https://books.toscrape.com/"


class CollectData(object):
    """
    The Collect Data class collects book data according to given criteria and filters
    """
    def __init__(self, books_count, genres, filters, keywords, title, file_path):
        self.__collection = DataHolder()
        self.__url_collector = UrlCollector(BASE_URL)
        self.__request_handler = self.__init_request_handler(BASE_URL)
        self.__content_extractor = None
        self.__books_count = books_count
        self.__genres = genres
        self.__filters = filters
        self.__keywords = keywords
        self.__title = title
        self.__file_path = file_path

    @property
    def collection(self):
        return self.__collection

    def __set_content_extractor(self, value):
        """
        Set content_extractor. If content_extractor is None, creates an instance.
        If content_extractor is all ready created, sets new value.
        :param value:
        :return:
        """
        if self.__content_extractor:
            self.__content_extractor.html_text = value
        else:
            self.__content_extractor = BookDataExtractor(value)

    @staticmethod
    def __init_request_handler(url):
        """
        Try to create request handler instance.
        If success return request handler with input url.
        If fails print error message and return None.
        :param url:
        :return:
        """
        try:
            page_handler = RequestHandler.create_request_handler(url)
        except ValueError as ve:
            print(ve)
            return None
        else:
            return page_handler

    def __add_book_to_collection(self):
        self.__collection.add_entity(
            self.__content_extractor.get_upc(),
            self.__content_extractor.get_title(),
            self.__content_extractor.get_genre(),
            self.__content_extractor.get_product_type(),
            self.__content_extractor.get_price_incl_tax(),
            self.__content_extractor.get_price_excl_tax(),
            self.__content_extractor.get_tax(),
            self.__content_extractor.get_quantity(),
            self.__content_extractor.get_rating(),
            self.__content_extractor.get_description()
        )

    def __collect_books_by_titles(self):
        """
        Filters books by list of titles.
        If there are matching books returns a list of book soups
        :return list:
        """
        books_filter = TitlesFilter(self.__file_path)
        if not books_filter.titles_list:
            return
        titles_dict = self.__url_collector.collect_books_urls()
        filtered_urls = books_filter.filter_books_by_titles(titles_dict)
        if filtered_urls:
            return self.__request_handler.get_pages_text_async(filtered_urls)

    def __collect_book_by_exact_title(self):
        """
        Search current book by title.
        If match returns list with book soup
        :return:
        """
        books_filter = ExactTitleFilter(self.__title)
        titles_dict = self.__url_collector.collect_books_urls(self.__books_count, self.__genres)
        book_url = books_filter.search_book_by_exact_title(titles_dict)
        if book_url:
            return [self.__request_handler.get_page(book_url)]

    def __collect_filtered_books(self):
        """
        Collect soups of all books in titles_dict and filters them by a given filters, if any.
        returns list of filtered soups
        :return:
        """
        books_filter = BooksFilter(self.__filters, self.__keywords)
        titles_dict = self.__url_collector.collect_books_urls(self.__books_count, self.__genres)
        soup_list = self.__request_handler.get_pages_text_async(titles_dict.values())
        if soup_list:
            return books_filter.filter_books(soup_list)

    def __get_books_soups(self):
        """
        Select the type of filter to apply
        :return:
        """
        if not self.__request_handler:
            return
        if self.__file_path:
            return self.__collect_books_by_titles()
        if self.__title:
            return self.__collect_book_by_exact_title()
        return self.__collect_filtered_books()

    def collect_books_data(self):
        """
        Collect a list of soups according to set criteria and filters.
        Collect data for all books in the soup list.
        :return:
        """
        print("Scraping books data...")
        soup_list = self.__get_books_soups()
        if not soup_list:
            return
        for soup in soup_list:
            self.__set_content_extractor(soup)
            self.__add_book_to_collection()
