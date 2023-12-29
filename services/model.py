from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report

from resources.config import Config

class Model:
    def __init__(self, model_type):
        self.model_type = model_type

        if model_type == 'logreg':
            self.model = LogisticRegression(random_state=42)
        elif model_type == 'rf':
            self.model = RandomForestClassifier(random_state=42)
        elif model_type == 'boosting':
            self.model = GradientBoostingClassifier(random_state=42)
        else:
            print('ooops, there is not such model')

        self.metrics = None

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def fit_predict(self, X_train, y_train, X_test):
        self.fit(X_train, y_train)

        return self.predict(X_test)

    def eval_metrics(self, y_true, y_pred):
        self.metrics = classification_report(y_true, y_pred)
        print(self.metrics)

    def __ne__(self, other: object) -> bool:
        return self.model_type != other.model_type


