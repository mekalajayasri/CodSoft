
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Creating a sample user-item ratings matrix
new_data = {
    'Book A': [4, 3, 2, 5, 0],
    'Book B': [0, 5, 1, 2, 4],
    'Book C': [3, 0, 5, 4, 1],
    'Book D': [1, 4, 0, 2, 3],
    'Book E': [2, 1, 4, 0, 5]
}
item_ratings = pd.DataFrame(new_data, index=['Reader 1', 'Reader 2', 'Reader 3', 'Reader 4', 'Reader 5'])

# Compute cosine similarity between users
reader_similarity = cosine_similarity(item_ratings)

# Create a DataFrame from the similarity matrix for easier reading
reader_similarity_df = pd.DataFrame(reader_similarity, index=item_ratings.index, columns=item_ratings.index)

# Function to recommend books to a reader based on similar readers' preferences
def recommend_books(reader, item_ratings, reader_similarity_df, n_recommendations=3):
    similar_readers = reader_similarity_df[reader].sort_values(ascending=False)[1:]  # Exclude the reader themselves
    weighted_ratings = pd.Series(np.zeros(item_ratings.shape[1]), index=item_ratings.columns)
    
    for other_reader, similarity in similar_readers.items():
        weighted_ratings += item_ratings.loc[other_reader] * similarity
    
    reader_unrated = item_ratings.loc[reader][item_ratings.loc[reader] == 0]  # Books the reader hasn't rated
    recommendations = weighted_ratings[reader_unrated.index].sort_values(ascending=False)[:n_recommendations]
 
    return recommendations.index.tolist()

# Example: Recommend books for 'Reader 1'
reader = 'Reader 1'
recommended_books = recommend_books(reader, item_ratings, reader_similarity_df, n_recommendations=3)

print(f"Books recommended for {reader}: {recommended_books}")

