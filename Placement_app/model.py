import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def train_model():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Senthil@7578",
        database="placement_system"
    )

    query = "SELECT * FROM students"
    df = pd.read_sql(query, conn)
    conn.close()

    df = df.drop(columns=["student_id"])

    X = df[["attendance","avg_marks","python","sql_skill","aptitude","communication"]]
    y = df["placement_readiness"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    return model

# Train model once
model = train_model()

def predict_student(data):
    return model.predict([data])[0]
