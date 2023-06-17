import matplotlib.pyplot as plt

# Set Labels
labels = 'Schweiz', 'Europa', 'USA', 'Sonstige', 'ohne Eintrag'
sizes = [21, 18, 14, 1, 47]

# Expand a slice
explode = (0.1, 0, 0, 0, 0)

# Create pie chart
plt.pie(sizes, labels=labels, autopct='%.1f%%', startangle=90, explode=explode)

# Set legend for chart
plt.legend(labels, loc='upper right')

# Set title
plt.title("Credit Suisse Aktien Verteilung gemäss Aktienregister in %")

plt.show()
