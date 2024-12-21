import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

# Expanded Dataset (Correct and Incorrect Sentences)
data = [
    # Subject-verb agreement errors
    ("அவன் பாடுகிறேன்", "அவன் பாடுகிறான்"),
    ("அவள் பாடுகிறேன்", "அவள் பாடுகிறாள்"),
    ("நான் பாடுகிறான்", "நான் பாடுகிறேன்"),
    ("அவர்கள் பாடுகிறான்", "அவர்கள் பாடுகிறார்கள்"),
    ("நாங்கள் பாடுகிறேன்", "நாங்கள் பாடுகிறோம்"),
    ("அவன் கத்தறாள்", "அவன் கத்தறான்"),
    ("அவள் வேலை செய்கிறான்", "அவள் வேலை செய்கிறாள்"),
    ("நாங்கள் சிரிக்கிறேன்", "நாங்கள் சிரிக்கிறோம்"),
    ("அவர்கள் ஓடுகிறான்", "அவர்கள் ஓடுகிறார்கள்"),
    ("நான் நடக்கிறான்", "நான் நடக்கிறேன்"),

    # Subject-verb tense mismatches
    ("நான் நேற்று பாடுகிறேன்", "நான் நேற்று பாடினேன்"),
    ("அவள் நாளை பாடினாள்", "அவள் நாளை பாடுவாள்"),
    ("அவன் கடந்த ஆண்டு பாடுவான்", "அவன் கடந்த ஆண்டு பாடினான்"),
    ("அவர்கள் நேற்று பாடுகிறார்கள்", "அவர்கள் நேற்று பாடினார்கள்"),
    ("நாங்கள் நாளை பாடினோம்", "நாங்கள் நாளை பாடுவோம்"),
    ("அவன் அப்போது பேசினான்", "அவன் அப்போது பேசினான்"),
    ("அவள் அடுத்த மாதம் பாடினாள்", "அவள் அடுத்த மாதம் பாடுவாள்"),
    ("நாங்கள் கடந்த வாரம் வேலை செய்தோம்", "நாங்கள் கடந்த வாரம் வேலை செய்தோம்"),
    ("நான் நாளை நடப்பேன்", "நான் நாளை நடப்பேன்"),
    ("அவர்கள் நேற்று கற்றார்கள்", "அவர்கள் நேற்று கற்றார்கள்"),

    # Neutral examples (correct sentences)
    ("அவன் பந்து விளையாடுகிறான்", "அவன் பந்து விளையாடுகிறான்"),
    ("அவள் மிகவும் அழகாக நடக்கிறாள்", "அவள் மிகவும் அழகாக நடக்கிறாள்"),
    ("நாங்கள் சாப்பிட்டோம்", "நாங்கள் சாப்பிட்டோம்"),
    ("அவர்கள் ஓடினார்கள்", "அவர்கள் ஓடினார்கள்"),
    ("நான் பள்ளிக்கு சென்றேன்", "நான் பள்ளிக்கு சென்றேன்"),
    ("அவன் பாடசாலையில் இருக்கிறான்", "அவன் பாடசாலையில் இருக்கிறான்"),
    ("அவள் உணவை சமைக்கிறாள்", "அவள் உணவை சமைக்கிறாள்"),
    ("நாங்கள் புத்தகங்களை படித்தோம்", "நாங்கள் புத்தகங்களை படித்தோம்"),
    ("அவர்கள் விரைவாக சென்றார்கள்", "அவர்கள் விரைவாக சென்றார்கள்"),
    ("நான் நண்பர்களுடன் பேசினேன்", "நான் நண்பர்களுடன் பேசினேன்"),

    # Longer sentences with mixed errors
    ("நான் நேற்று காலை பாடசாலைக்கு சென்றோம்", "நான் நேற்று காலை பாடசாலைக்கு சென்றேன்"),
    ("அவர்கள் மிகவும் அழகாக பாட்டுப் பாடினாள்", "அவர்கள் மிகவும் அழகாக பாட்டுப் பாடினார்கள்"),
    ("நான் நாளை வீட்டுக்கு சென்றேன்", "நான் நாளை வீட்டுக்கு செல்வேன்"),
    ("நாங்கள் வேகமாக ஓடி வந்தேன்", "நாங்கள் வேகமாக ஓடி வந்தோம்"),
    ("அவன் கடந்த வருடம் பிறந்த நாள் கொண்டாடுவான்", "அவன் கடந்த வருடம் பிறந்த நாள் கொண்டாடினான்")
]

# Prepare Data
X = [x[0] for x in data]  # Incorrect sentences (input)
y = [x[1] for x in data]  # Correct sentences (output)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the sentences using CountVectorizer
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Initialize the model (Naive Bayes)
model = MultinomialNB()

# Train the model
model.fit(X_train_vec, y_train)

# Predict on the test data
y_pred = model.predict(X_test_vec)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%")

# Now test with specific sentences
test_sentences = [
    "நான் நேற்று காலை பாடசாலைக்கு சென்றோம்.",
    "அவர்கள் மிகவும் அழகாக பாட்டுப் பாடினாள்.",
    "நான் நாளை வீட்டுக்கு சென்றேன்.",
    "நாங்கள் வேகமாக ஓடி வந்தேன்.",
    "அவன் கடந்த வருடம் பிறந்த நாள் கொண்டாடுவான்."
]

# Vectorize the test sentences
test_vec = vectorizer.transform(test_sentences)

# Make predictions
predictions = model.predict(test_vec)

print("\nPredictions for test sentences:")
for i, sentence in enumerate(test_sentences):
    print(f"Input Sentence: {sentence}")
    print(f"Predicted Corrected Sentence: {predictions[i]}")
    print()
