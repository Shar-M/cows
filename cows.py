from random import randrange

COWS_TXT = "cows.txt"


class Cows:
    def __init__(self):
        global cows
        cows = self.get_all_cows()

    @staticmethod
    def get_all_cows():
        cows_file = open("%s" % COWS_TXT, 'r', encoding="utf-8")
        cow_string = cows_file.read()
        cows_file.close()
        return cow_string.split('\n\n\n')

    def random_cow(self):
        random_offset = randrange(cows.__len__())
        return self.get_cow_by_number(random_offset)

    @staticmethod
    def get_cow_by_number(number):
        try:
            return cows[number]
        except Exception as e:
            return "Moo, we don't have so many cows. Try with a smaller number. " + str(e)
