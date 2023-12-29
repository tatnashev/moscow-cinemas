import pandas as pd
from resources.config import Config
from sklearn.model_selection import train_test_split

class Data:
    '''
    Data: class for storing one concated and
    distinct by period dataframes.
    '''

    def __init__(self):
        self.config = Config()

        self.df_first_period = pd.read_excel(self.config.first_period_path)
        self.df_second_period = pd.read_excel(self.config.second_period_path)

        self.df_concat = None
        self.concat_periods()

        self.df_concat['rank'] = pd.Categorical(self.df_concat['rank'])
        self.df_first_period['rank'] = pd.Categorical(self.df_first_period['rank'])
        self.df_second_period['rank'] = pd.Categorical(self.df_second_period['rank'])

    def concat_periods(self):
        self.df_first_period['label'] = self.config.first_period_label
        self.df_first_period['period'] = self.config.first_period_period

        self.df_second_period['label'] = self.config.second_period_label
        self.df_second_period['period'] = self.config.second_period_period

        self.df_concat = pd.concat([self.df_first_period, self.df_second_period], axis=0)

    def calc_stat(self):
        '''
        here we adding some important for analysis
        new features (kind of feature engineering):
            -foreign_movies_percentage
            -new_movies_percentage
            -is_awarded_percentage
            -is_censure_percentage
        '''

        self.df_concat['foreign_movies_percentage'] = (self.df_concat['is_foreign'] / self.df_concat['count_movies']) * 100
        self.df_concat['new_movies_percentage'] = (self.df_concat['new_movies'] / self.df_concat['count_movies']) * 100
        self.df_concat['is_award_percentage'] = (self.df_concat['is_award'] / self.df_concat['count_movies']) * 100
        self.df_concat['is_censure_percentage'] = (self.df_concat['is_censure'] / self.df_concat['count_movies']) * 100

        self.df_first_period['foreign_movies_percentage'] = (self.df_first_period['is_foreign'] / self.df_first_period['count_movies']) * 100
        self.df_first_period['new_movies_percentage'] = (self.df_first_period['new_movies'] / self.df_first_period['count_movies']) * 100
        self.df_first_period['is_award_percentage'] = (self.df_first_period['is_award'] / self.df_first_period['count_movies']) * 100
        self.df_first_period['is_censure_percentage'] = (self.df_first_period['is_censure'] / self.df_first_period['count_movies']) * 100

        self.df_second_period['foreign_movies_percentage'] = (self.df_second_period['is_foreign'] / self.df_second_period['count_movies']) * 100
        self.df_second_period['new_movies_percentage'] = (self.df_second_period['new_movies'] / self.df_second_period['count_movies']) * 100
        self.df_second_period['is_award_percentage'] = (self.df_second_period['is_award'] / self.df_second_period['count_movies']) * 100
        self.df_second_period['is_censure_percentage'] = (self.df_second_period['is_censure'] / self.df_second_period['count_movies']) * 100

    def prepare_data(self, df_period='first', y_column='rank',
                     columns_to_drop = ['rank', 'Screening Days', 'Cinema', 'label']
                     ):
        if df_period == 'first':
            df = self.df_first_period
        elif df_period == 'second':
            df = self.df_second_period
        else:
            df = self.df_concat

        df_train, df_test = train_test_split(df,
                                             test_size=0.2,
                                             stratify=df[['label', 'rank']],
                                             random_state=42
                                             )


        X_train = df_train.drop(columns=columns_to_drop)
        X_test = df_test.drop(columns=columns_to_drop)

        y_train = df_train[y_column]
        y_test = df_test[y_column]

        return X_train, X_test, y_train, y_test

