import os
from flask import Flask, render_template, request
from tmdb_api import get_popular_movies, search_movies, get_movie_details

app = Flask(__name__)

@app.route('/')
def home():
    movies = get_popular_movies()
    return render_template('index.html', movies=movies)

@app.route('/movies')
def movies():
    movies = get_popular_movies()
    return render_template('movies.html', movies=movies)

@app.route('/tv-shows')
def tv_shows():
    return render_template('tv_shows.html')

@app.route('/my-list')
def my_list():
    return render_template('my_list.html')

@app.route('/search')
def search():
    query = request.args.get('query', '')
    movies = search_movies(query)
    return render_template('search_results.html', movies=movies, query=query)

@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    movie = get_movie_details(movie_id)
    return render_template('movie_detail.html', movie=movie)

@app.route('/new-popular')
def new_popular():
    movies = get_popular_movies()
    return render_template('new_popular.html', movies=movies)

if __name__ == '__main__':
    # Get the port from environment variable, default to 5000 for local testing
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
