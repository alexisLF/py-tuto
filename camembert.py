import matplotlib.pyplot as plt

labels = 'Brie', 'Comté', 'Camembert', 'Bleu'
sizes = [15, 30, 45, 10]
explode = (0.2, 0, 0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode= explode, labels=labels, autopct='%1.1f%%', startangle=90)

plt.show()