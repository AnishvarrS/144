import csv
all_movies = []
with open('E:\\Whitehatjunior\\Module3\\movie_recommendation_142\\movie_recommendation_142_fixed_errors-main\\c-142-main\\c-142-main\\final.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []