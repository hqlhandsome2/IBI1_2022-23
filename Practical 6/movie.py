import matplotlib.pyplot as plt
# Define dictionary datas nd choose colors for each data
movie ={'Comedy':73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction':22,'Horror':19, 'Crime':18, 'Documentary':12, 'History':8, 'War':7}
colors= ['red', 'wheat', 'lightgray', 'green','grey','lightpink','teal','beige','lightcoral','gold']
# Extract a list of labels and numeric values
labels = list(movie.keys())
values = list(movie.values())

# Draw a pie chart
plt.pie(values, labels=labels, colors= colors , autopct='%1.1f%%',)
# show legend and adjust the size of it
plt.legend(bbox_to_anchor=(0.98, 1.10),fontsize='small')
# show the image
plt.show()

# set the requested genre, you can choose any tpye of movie in dictionary,like Action....
movie_genre = "Horror"

# print the number of students who like the requested genre
print(movie[movie_genre])
