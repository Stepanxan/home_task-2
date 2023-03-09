import matplotlib.pyplot as plt
from app import *


#Стовпчиковий графік
most_common = word_count.most_common(5)
words, counts = zip(*most_common)
plt.bar(words, counts)
plt.title("Top 5 Most Common Words")
plt.xlabel("Words")
plt.ylabel("Counts")
plt.savefig("./chart/mygraph1.png")
