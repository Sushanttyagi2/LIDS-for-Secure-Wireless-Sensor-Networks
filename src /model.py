import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def train_model(df):
    X = df[["packet_rate", "drop_rate", "energy"]]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    return model
