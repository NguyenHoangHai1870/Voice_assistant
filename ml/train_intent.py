import pandas as pd
import joblib

from pathlib import Path

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import FunctionTransformer

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "data_R.csv"
MODEL_PATH = BASE_DIR / "models" / "intent_model.pkl"

def identity(x):
    return x

df = pd.read_csv(DATA_PATH, encoding="utf-8")

X = df["text"].astype(str)
y = df["label"]

word_vectorizer = Pipeline([
    (
        "selector",
        FunctionTransformer(identity, validate=False)
    ),
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            analyzer="word",
            ngram_range=(1, 2),
            max_features=5000,
            sublinear_tf=True
        )
    )
])

char_vectorizer = Pipeline([
    (
        "selector",
        FunctionTransformer(identity, validate=False)
    ),
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            analyzer="char_wb",
            ngram_range=(3, 5),
            max_features=10000,
            sublinear_tf=True
        )
    )
])

features = ColumnTransformer([
    ("word", word_vectorizer, 0),
    ("char", char_vectorizer, 0)
])

pipeline = Pipeline([
    (
        "features",
        features
    ),
    (
        "clf",
        LogisticRegression(
            max_iter=3000,
            class_weight="balanced",
            C=2.0
        )
    )
])

pipeline.fit(X.to_frame(), y)

joblib.dump(pipeline, MODEL_PATH)

print("Model saved to:", MODEL_PATH)