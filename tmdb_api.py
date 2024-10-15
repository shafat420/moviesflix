import requests

TMDB_API_KEY = "61e2290429798c561450eb56b26de19b"
TMDB_BASE_URL = "https://api.themoviedb.org/3"

def get_popular_movies():
    url = f"{TMDB_BASE_URL}/movie/popular"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
        "page": 1
    }
    response = requests.get(url, params=params)
    return response.json()["results"]

def get_top_rated_movies():
    url = f"{TMDB_BASE_URL}/movie/top_rated"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
        "page": 1
    }
    response = requests.get(url, params=params)
    return response.json()["results"]

def get_upcoming_movies():
    url = f"{TMDB_BASE_URL}/movie/upcoming"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
        "page": 1
    }
    response = requests.get(url, params=params)
    return response.json()["results"]

def search_movies(query):
    url = f"{TMDB_BASE_URL}/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
        "query": query,
        "page": 1
    }
    response = requests.get(url, params=params)
    return response.json()["results"]

def get_movie_details(movie_id):
    url = f"{TMDB_BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US"
    }
    response = requests.get(url, params=params)
    return response.json()