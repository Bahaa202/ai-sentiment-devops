"""
train_model.py
موديل بسيط جدًا لتصنيف المشاعر (Positive / Negative)
باستخدام Logistic Regression + TF-IDF
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# ----------------------------
# 1. بيانات تدريب بسيطة جدًا (Demo dataset)
# لاحقًا ممكن نستبدلها بـ dataset حقيقي أكبر (IMDB مثلاً)
# ----------------------------
texts = [
    "I love this product, it's amazing",
    "This is the best experience ever",
    "Absolutely wonderful, highly recommend",
    "Great quality and fast delivery",
    "I am very happy with this purchase",
    "Excellent service and friendly staff",
    "This made my day, fantastic!",
    "I really enjoy using this app",
    "Superb quality, will buy again",
    "Amazing value for money",

    "I hate this product, it's terrible",
    "Worst experience of my life",
    "Absolutely awful, do not buy",
    "Poor quality and slow delivery",
    "I am very disappointed with this purchase",
    "Terrible service and rude staff",
    "This ruined my day, horrible",
    "I really dislike using this app",
    "Bad quality, will not buy again",
    "Waste of money",
]

labels = [
    "positive", "positive", "positive", "positive", "positive",
    "positive", "positive", "positive", "positive", "positive",
    "negative", "negative", "negative", "negative", "negative",
    "negative", "negative", "negative", "negative", "negative",
]

# ----------------------------
# 2. بناء الـ Pipeline: TF-IDF + Logistic Regression
# ----------------------------
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression()),
])

# ----------------------------
# 3. التدريب
# ----------------------------
model.fit(texts, labels)

# ----------------------------
# 4. اختبار سريع
# ----------------------------
test_samples = ["I love it so much", "This is really bad"]
predictions = model.predict(test_samples)
for text, pred in zip(test_samples, predictions):
    print(f"'{text}' -> {pred}")

# ----------------------------
# 5. حفظ الموديل
# ----------------------------
joblib.dump(model, "app/model.pkl")
print("\nModel saved to app/model.pkl")
