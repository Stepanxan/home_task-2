import nltk
from collections import Counter

nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer


#Зчитуємо файл який дали в завданні
filename = "data.csv"
with open(filename, 'r') as f:
    reviews = f.readlines()

# ініціалізуємо SentimentIntensityAnalyzer (бібліотека для визначення настроїв)
sia = SentimentIntensityAnalyzer()

# рахуємо загальний настрій відгуків
compound_scores = [sia.polarity_scores(review)['compound'] for review in reviews]
overall_sentiment = sum(compound_scores) / len(compound_scores)

# класифікуємо відгуки на позитивні, негативні та нейтральні (рахує всі відгуки пропускаючи ті де немає числового значення в колонці "Stars"
positive_reviews = [review for review in reviews if sia.polarity_scores(review)['compound'] > 0]
negative_reviews = [review for review in reviews if sia.polarity_scores(review)['compound'] < 0]
neutral_reviews = [review for review in reviews if sia.polarity_scores(review)['compound'] == 0]


#positive_reviews = [review for review in reviews if review.strip() and int(review.split('Stars \n')[0]) >= 4]
#negative_reviews = [review for review in reviews if review.strip() and int(review.split('Stars \n')[0]) <= 2]
#neutral_reviews = [review for review in reviews if review.strip() and int(review.split('Stars \n')[0]) == 3]


# рахуємо кількість повторюваних слів
word_count = Counter(word for review in reviews for word in review.split())
most_common_words = word_count.most_common(5)


num_positive = len(positive_reviews)
num_negative = len(negative_reviews)
num_neutral = len(neutral_reviews)


with open('report.txt', 'w') as file:
    file.write('\n Аналіз відгуків:\n')
    file.write(f"Загальний настрій відгуків: ({overall_sentiment}):\n")
    file.write(f"Позитивні: ({len(positive_reviews)}):\n")
    file.write(f"Негативні: ({len(negative_reviews)}):\n")
    file.write(f"Нейтральні: ({len(neutral_reviews)}):\n")


with open('repeating words.txt', 'w') as file:
    file.write("\n П'ять найбільш вживаних слів: \n")
    for word, count in most_common_words:
        file.write(f"{word}: {count}\n")

    file.write("Кількість повторюваних слів: \n")
    for word, count in word_count.items():
        file.write(f"{word}: {count}\n")




# Для перевірки
print("Аналіз настроїв:")
print("Загальний настрій відгуків: {:.2f}".format(overall_sentiment))
print("")

print("Аналіз негативних, позитивних і природних відгуків:")
print("Кількість позитивних відгуків: {}".format(num_positive))
print("Кількість негативних відгуків: {}".format(num_negative))
print("Кількість нейтральних відгуків: {}".format(num_neutral))
print("")