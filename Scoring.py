import joblib
import pandas as pd
from sklearn.metrics import precision_score

# This would be the tested data hosted on ocean
test = pd.read_csv('test.csv')
X_test = test.drop('species', axis=1)
y_true = test['species']


def Cal_Score(y_pred):
    loaded_model = joblib.load('weights/model_weights.joblib')

    y_pred = loaded_model.predict(X_test)

    user_precision_score = precision_score(y_true, y_pred, average='macro')

    return user_precision_score
