#!/usr/bin/python3
"""this module puts into practice the concept of inheritance"""


class MyList(list):
    """this is a subclass of the class "list"""


    def print_sorted(self):
        """prints the list object in a sorted format"""


        return(sorted(self))


