"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    incoming_list = [1, 2, 3, 4, 5, 6, 7]
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """

    return max(incoming_list)


def find_least_number(incoming_list):
    incoming_list = [1, 2, 3, 4, 5, 6, 7]
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """

    return min(incoming_list)


def add_list_numbers(incoming_list):
    incoming_list = [1, 2, 3, 4, 5, 6, 7]
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """

    return sum(incoming_list)


def longest_value_key(incoming_dict):
    incoming_dict = {"green": "perfect", "red": "good"}
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """

    return max(incoming_dict.keys(), key=len)
