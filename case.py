import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('IMDB-Movie-Data.csv')
# print(df.info())
# df['Revenue (Millions)'].fillna(-1,inplace = True)
# print(df.info())
# michael_film = 0
# michael_ratings = 0
# emma_film = 0
# emma_ratings = 0

# print('?')

s = df['Actors'].value_counts().plot(kind = 'pie')
s.plot()
plt.show()
# fantasy_genre = 0
# fantasy_runtime = 0
# drama_genre = 0
# drama_runtime = 0
# def genre_apply(row):
#     global fantasy_genre,fantasy_runtime,drama_genre,drama_runtime
#     if row['Genre'].find('Fantasy') != 1:
#         fantasy_runtime += row['Revenue (Millions)']
#         fantasy_genre += 1
#     if row['Genre'].find('Drama') != 1:
#         drama_runtime += row['Revenue (Millions)']
#         drama_genre += 1
# df.apply(genre_apply,axis = 1)
# print('Среднеий доход у Fantasy',round(fantasy_runtime/fantasy_genre,2))
# print('Среднеий доход у Drama',round(drama_runtime/drama_genre,2))

# def ratings_apply(row):
#     global michael_film,michael_ratings,emma_film,emma_ratings
#     if row['Actors'].find('Michael Fassbender') != -1:
#         michael_ratings += row['Rating']
#         michael_film += 1
#     if row['Actors'].find('Emma Watson') != -1:
#         emma_ratings += row['Rating']
#         emma_film += 1

# df.apply(ratings_apply,axis = 1)
# print('Среднее у Michael Fassbender',round(michael_ratings/michael_film,2))
# print('Среднее у Emma Watson',round(emma_ratings/emma_film,2))
# print(df['Genre'].value_counts())



