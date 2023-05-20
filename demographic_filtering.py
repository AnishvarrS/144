import pandas as pd

df = pd.read_csv("E:\\Whitehatjunior\\Module3\\movie_recommendation_142\\movie_recommendation_142_fixed_errors-main\\c-142-main\\c-142-main\\final.csv")

C = df["vote_average"].mean()
m = df["vote_count"].quantile(0.9)
q_movies = df.copy().loc[df["vote_count"] >= m]


def weighted_rating(x, m=m, C=C):
    v = x["vote_count"]
    R = x["vote_average"]
    return (v / (v + m) * R) + (m / (m + v) * C)


q_movies["score"] = q_movies.apply(weighted_rating, axis=1)

q_movies = q_movies.sort_values("score", ascending=False)

output = (
    q_movies[
        ["title", "poster_link", "release_date", "runtime", "vote_average", "overview"]
    ]
    .head(20)
    .values.tolist()
)
