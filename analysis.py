import re
from algorithms import *


class Analysis():
    def __init__(self, debug=False):
        self.articles = {
            "citylink": [
                "citylink-article-1.txt",
                "citylink-article-2.txt",
                "citylink-article-3.txt"],

            "poslaju": ["poslaju-article-1.txt",
                        "poslaju-article-2.txt",
                        "poslaju-article-3.txt"],

            "dhl": ["dhl-article-1.txt",
                    "dhl-article-2.txt",
                    "dhl-article-3.txt"],

            "jnt": ["jnt-article-1.txt",
                    "jnt-article-2.txt",
                    "jnt-article-3.txt"]
        }

        self.debug = debug

    def run_analysis(self):
        self.articles_len = 0
        self.pos = 0
        self.neg = 0
        self.neutral = 0

        pos_neg = dict()
        sentimental_data = dict()
        for courier in self.articles:
            text = ""
            for art in self.articles[courier]:
                with open("articles/" + art, encoding="utf8") as data:
                    text += data.read()
            self.articles_len = len(text.split())
            neutral, pos, neg = self.article_sentiment(text)
            sentimental_data[courier] = (neg / self.articles_len)
            pos_neg[courier] = [pos, neg]
            # print(f"COURIER {courier}:  ",
            #       sentimental_data[courier], " Length: ", self.articles_len, " Positive: ", pos, " Negative: ", neg, " Neutral: ", neutral)
        sentimental_data['gdex'] = 0.01
        print(sentimental_data)
        print(pos_neg)
        return pos_neg
    # count article's positive , negative words and neutral words

    def article_sentiment(self, text):
        with open('articles/negative_words.txt', encoding='utf-8') as File1:
            negativeFile = File1.read().lower()
        negativeText = re.sub('[,-]', '', negativeFile).split()

        with open('articles/positive_words.txt', encoding='utf-8') as File2:
            positiveFile = File2.read().lower()
        positiveText = re.sub('[,-]', '', positiveFile).split()

        self.neg = 0
        for n in negativeText:
            result = Boyer_Moore_Matcher(text, n)
            self.neg += len(result)

        self.pos = 0
        lst = []
        for p in positiveText:
            result1 = Boyer_Moore_Matcher(text, p)
            lst = [*lst, *result1]

        self.pos = len(set(lst))

        self.neutral = self.articles_len - (self.pos + self.neg)
        return self.neutral, self.pos, self.neg


if __name__ == '__main__':
    analysis = Analysis(debug=True)
    analysis.run_analysis()
