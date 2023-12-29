from pydantic import BaseModel

class Config(BaseModel):
    first_period_path = 'data/agg_stat_first_period.xlsx'
    second_period_path = 'data/agg_stat_second_period.xlsx'

    first_period_label = '1948-1949'
    second_period_label = '1954-1955'
    first_period_period = 1948
    second_period_period = 1954

    columns_genres = ['Adventure', 'Biography',
       'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History',
       'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Short', 'Sport',
       'Thriller', 'War', 'Western', 'Action', 'Adult', 'Animation',
       'Documentary']

    columns_countries = ['Austria', 'China', 'Czechoslovakia', 'East Germany',
       'France', 'Germany', 'Hungary', 'Italy', 'Kazakhstan', 'Mongolia',
       'Netherlands', 'Norway', 'Soviet Union', 'United Kingdom',
       'United States', 'Albania', 'Argentina', 'Australia', 'Bulgaria',
       'Finland', 'India', 'Japan', 'Mexico', 'North Korea', 'Poland',
       'Romania', 'Russia', 'Spain', 'Sweden', 'West Germany', 'Yugoslavia']