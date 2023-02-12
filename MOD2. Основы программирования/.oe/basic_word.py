class BasicWord:
    """
    A basic word class. Initializes a source word and its valid subwords.
    It has methods: checking the entered word in the list of valid subwords,
    counting the number of subwords.
    """
    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words

    def __repr__(self):
        return f"BasicWord(word={self.word}, sub_words={self.sub_words})"

    def is_correct(self, input_word):
        return input_word in self.sub_words

    def counting_sub_words(self):
        return len(self.sub_words)
