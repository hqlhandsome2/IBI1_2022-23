import matplotlib.pyplot as plt

# Define dictionary data and choose colors for each data
movie = {
    'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction': 22,
    'Horror': 19, 'Crime': 18, 'Documentary': 12, 'History': 8, 'War': 7
}

print(movie)
# Extract a list of labels and numeric values
labels = list(movie.keys())
values = list(movie.values())

# Set the requested genre; you can choose any type of movie in the dictionary, e.g., "Horror"
movie_genre = "Horror"

# Create a list of colors, highlighting the requested genre
colors = ['red' if label == movie_genre else 'lightgray' for label in labels]

# Create a bar plot
plt.bar(labels, values, color=colors)

# Add labels and titles
plt.xlabel('Movie Genre')
plt.ylabel('Number of Movies')
plt.title('Distribution of Movie Genres')

# Set the font size of x-axis tick labels
plt.xticks(fontsize=6)

# Show the bar plot
plt.show()

# Print the number of movies in the requested genre
print(f"Number of movies in the '{movie_genre}' genre: {movie[movie_genre]}")
