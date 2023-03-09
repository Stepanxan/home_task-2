import matplotlib.pyplot as plt
from app import *


#Кругла діаграма
labels = ['Positive', 'Negative', 'Neutral']
sizes = [num_positive, num_negative, num_neutral]


plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.legend(title = "Review: ")
plt.savefig("./graphs/mygraph.png")




