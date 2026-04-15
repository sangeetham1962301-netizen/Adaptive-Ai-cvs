import pandas as pd
import random
import csv

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB



# Load datasetw
data = pd.read_csv("college_faqnew.csv")

# Input & Output
X = data["question"]
y = data["tag"]

# Convert text to numbers
vectorizer = TfidfVectorizer()
X_vector = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vector, y)

print("✅ Adaptive AI Ready!\n")

# Function to store unknown questions
def save_unanswered(question):
    with open("unanswered_questions.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([question])

# Chat loop
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("AI: Goodbye!")
        break

    # Convert input
    user_vector = vectorizer.transform([user_input])

    # Get probability (confidence)
    probabilities = model.predict_proba(user_vector)
    confidence = max(probabilities[0])

    # If confidence is low → unknown question
    if confidence < 0.2:
        print("AI: Sorry, I don't know that yet. Your question has been recorded.")
        save_unanswered(user_input)
        continue

    # Predict tag
    predicted_tag = model.predict(user_vector)[0]

    # Get all answers for that tag
    answer = data[data["tag"] == predicted_tag]["answer"].values

    # Random answer selection
    answer = random.choice(answer)
    if "," in answer:
        items = answer.split(",")
        print("AI:")
        for item in items:
            print("•", item.strip())
    else:
        print("AI:", answer)