
#create dictionary
movie_ratings = {'The Godfather':  9,
                 'Back to The Future': 8.5,
                 'Batman Begins': 7.4,
                 'The Hunger games': 7.2,
                 'Forest Gump': 8.8}


def main():


    movie_title = input('Enter movie title: ')

    recommend_movie(movie_ratings, movie_title)





    





def recommend_movie(movie_ratings, movie_title ):

    
    if movie_title in movie_ratings and movie_ratings[movie_title] >= 8:
        print(f'I recomend {movie_title} with a rating of {movie_ratings[movie_title]} / 10')
    
    elif movie_title in movie_ratings and movie_ratings[movie_title] < 8:
        print(f'I reccomend the following movies:')
        for movies, rating in movie_ratings.items():
            if rating >= 8:
                print(f'{movies}, {rating} / 10')
    else:
        print(f'Your movie was not found, here are some movies I reccomend:')
        for movies, rating in movie_ratings.items():
            if rating >= 8:
                print(f'{movies}, {rating} / 10')





main()
