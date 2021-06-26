import requests
from bs4 import BeautifulSoup


class TopRatedMovies:

    def get_top_rated_movies_list(self):
        file = open("F:\\Projects\\IMDb_MovieSuggestion\\topRatedMovies.csv", 'w')
        file.write('S No.' + ';' + 'Movie Title' + ';' + 'Released Year' + ';' + 'IMDb Ratings' + ';' + 'Users rated' + '\n')
        data = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
        print(data)
        soup = BeautifulSoup(data.content, 'html.parser')
        movies_tables = soup.find('tbody', {'class':'lister-list'})
        movie_details = movies_tables.findAll('tr')
        count = 0
        for movie_info in movie_details:
            count += 1
            print(count)
            movie_title = movie_info.find('td', {'class':'titleColumn'})
            movie_Title= movie_title.a.text
            release_year= movie_title.span.text
            movie_ratings = movie_info.find('td', {'class': 'ratingColumn imdbRating'})
            rating = movie_ratings.strong.text
            user_ratings = movie_ratings.strong.attrs
            user_Rated = user_ratings["title"]
            print(user_Rated)
            file.write(str(count) + str(';') + movie_Title + str(';') + release_year +
                       str(';') + rating + str(';') + user_Rated + '\n')


holly = TopRatedMovies()
holly.get_top_rated_movies_list()