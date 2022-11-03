class CountVectorizer:
    """Returns matrix of counts of words in texts
    and all distinct words from all texts """
    def __init__(self):
        self.voc = []

    def fit_transform(self, text: list) -> list:
        """Returns the word frequency list"""
        text_new = []
        for element in text:
            element = element.lower().split()
            text_new.append(element)
            for e in element:
                if e not in self.voc:
                    self.voc.append(e)
        counts = []
        for element in text_new:
            single_text_count = []
            for e in self.voc:
                single_text_count.append(element.count(e))
            counts.append(single_text_count)
        return counts

    def get_feature_names(self) -> list:
        """Returns a list of unique words for all texts in the list"""
        return self.voc


if __name__ == '__main__':
    corpus = [
     'Crock Pot Pasta Never boil pasta again',
     'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(count_matrix)
    print(vectorizer.get_feature_names())
