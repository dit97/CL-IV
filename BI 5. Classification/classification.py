from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load built-in Iris dataset
iris = load_iris()

# Features and target
X = iris.data
y = iris.target

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Logistic Regression model
model = LogisticRegression(max_iter=200)

# Train the model
model.fit(X_train, y_train)

# Prediction on training data
train_pred = model.predict(X_train)

# Prediction on testing data
test_pred = model.predict(X_test)

# Training Accuracy
train_accuracy = accuracy_score(y_train, train_pred)

# Testing Accuracy
test_accuracy = accuracy_score(y_test, test_pred)

print("Training Accuracy:", train_accuracy)
print("Testing Accuracy:", test_accuracy)

# Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, test_pred))

# Confusion Matrix
print("Confusion Matrix:\n")
print(confusion_matrix(y_test, test_pred))