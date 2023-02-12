class Player:
    """
    Player class:
    Initiates a username, a list of the user's entered words.
    Methods for counting words entered by the user, adding words
    to the list, checking words.
    """

    def __init__(self, user_name):
        self.user_name = user_name
        self.used_words = []

    def __repr__(self):
        return f"Player: (user_name: {self.user_name}, used_word: {self.used_words})"

    def count_words(self):
        return len(self.used_words)

    def append_used_word(self, word):
        self.used_words.append(word)

    def word_check(self, word):
        return word in self.used_words
