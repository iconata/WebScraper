class SortingMixin:
    @staticmethod
    def any_sort(dict_to_sort, sorting):
        """
        Collection of sorting according to a different user entered parameter.
        The collection is a static method and sorts the list given as a parameter.

        The keys must be passed as a string. Possible sorting keys are:
        - genre:
            sorts by genre, can be ascending or descending

        - rating:
            sorts by rating, can be ascending or descending

        - price:
            sorts by price, can be ascending or descending

        - quantity:
            sorts by book quantity, can be ascending or descending

        - default:
            sorts by upc if entered, else sorts by title, can be ascending or descending

        @param sorting: receives a list of arguments about type and direction of the sort
        @param dict_to_sort: dict to be sorted
        @return: None
        """
        sort_by = "default"
        sort_direction = "ascending"
        extract_args_from_list = sorting[0]

        possible_dict_keys = ["Rating", "Genre", "Price_incl_tax", "Quantity", "Title"]
        key_index = None

        if sorting:
            sort_type = extract_args_from_list[0]
            direction = extract_args_from_list[1]

            sort_by = sort_type
            sort_direction = direction

        if sort_by == "default":
            sort_by = "title"
        elif sort_by == "price":
            sort_by = "price_incl_tax"

        for index, value in enumerate(possible_dict_keys):
            if sort_by in value.lower():
                key_index = index
                break
            elif sort_by.capitalize() not in possible_dict_keys and sort_by != 'upc':
                return None

        if sort_by == "upc":
            if sort_direction.lower() == "ascending":
                return sorted(dict_to_sort.items(), key=lambda item: item[0])
            else:
                return sorted(
                    dict_to_sort.items(),
                    key=lambda item: item[0],
                    reverse=True,
                )

        elif sort_direction == "ascending":
            return sorted(
                dict_to_sort.items(),
                key=lambda item: item[1][possible_dict_keys[key_index]],
            )
        else:
            return sorted(
                dict_to_sort.items(),
                key=lambda item: item[1][possible_dict_keys[key_index]],
                reverse=True,
            )
