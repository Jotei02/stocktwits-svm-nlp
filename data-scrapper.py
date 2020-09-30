import requests
import json
import sys


def parse_json(json_data):
    # return the list of variables in the json data with body, in strings
    # should parse the json file into format like below
    # {variable name} : {body}
    # example: "label : this is a message"
    # some docs: https://docs.python.org/3/library/json.html
    return 0


def make_dict_from_list(message_list):
    # return a dict of the string list
    # the string list will follow the format of parse_json()
    # the dict should be like {label} : {array of messages}
    return 0


class DataScrapper:

    def __init__(self, auth_username, auth_passwd):
        self.auth_username = auth_username
        self.auth_passwd = auth_passwd
        self.data = None

    @staticmethod
    def _get_auth_token():  # can be used to add auth stuff but ignore for now
        # returns the auth token, -1 when failed
        # Some helpful articles and docs:
        # https://api.stocktwits.com/developers/docs/api#oauth-token-docs
        return 0

    @staticmethod
    def _get_trending_symbols():
        # returns a list of symbols, in string formats
        # make a get request and get the list of trending symbols
        # some docs: https://realpython.com/python-requests/#the-get-request
        # https://api.stocktwits.com/developers/docs/api#trending-symbols-docs
        return 0

    @staticmethod
    def _get_posts_from_symbol(symbol):
        # return a list of posts, in string format {sentiment label} : {body}
        # should removes everything except body and the sentiment label
        # some docs: https://realpython.com/python-requests/#the-get-request
        # https://api.stocktwits.com/developers/docs/api#streams-symbol-docs
        return 0

    def _read_from_csv(self):
        # read the csv file from local machine
        # then populate the self.data variable
        # the csv file will follow the format {label} , {message}
        # https://realpython.com/python-csv/
        self.data = []

    def _write_to_csv(self):
        # write the data in self to a local csv file
        # the csv file should follow the format {label} , {message}
        # https://realpython.com/python-csv/
        self.data = []  # remove this line

    def _populate_data(self, message_list):
        # populate the data var in self
        # the data should be a dictionary of entries, and you should use
        # make_dict_from_list(post_list) function to get the dict
        # the dict should be like {label} : {array of messages}
        # Note: this should not add duplicate messages
        self.data = []  # remove this line

    def _data_cleaning(self):
        # TO DO, clean the data in self
        # only return status code, 0 = failed, 1 = success
        self.data = []
        return 0


def main():
    auth_username = "cs490a"  # default username
    auth_passwd = "fZ?TCqik92x9pE3"  # default passwd
    args = sys.argv
    if len(args) > 1:
        auth_username = args[1]
        auth_passwd = args[2]

    scrapper = DataScrapper(auth_username, auth_passwd)


if __name__ == "__main__":
    # execute only if run as a script
    main()