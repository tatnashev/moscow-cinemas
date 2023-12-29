import plotly.express as px

class Vizualizer:
    '''
    Vizualizer: utility class for different visualisations.
    All methods are under the @staticmethod decorator
    '''

    @staticmethod
    def plot_boxplot(data, x, y, color=None, title='') -> None:
        fig = px.box(data, x=x, y=y, color=color, title=title)
        fig.show()

    # @staticmethod
    # def plot_barplot(data, x, y, color=None, title='') -> None:
    #     fig = px.bar(data, x=x, y=y, color=color, title=title)
    #     fig.show()

    @staticmethod
    def plot_hist(data, x, color=None, title='') -> None:
        fig = px.histogram(data, x=x, color=color, title=title)
        fig.update_layout(bargap=0.2)
        fig.show()

    @staticmethod
    def plot_scatter(data, x, y, color=None, title='') -> None:
        fig = px.scatter(data, x=x, y=y, color=color, title=title)
        fig.show()


