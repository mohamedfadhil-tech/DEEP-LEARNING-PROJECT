import random

classes = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer',
           'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

print("Simulating image classification model training...")

for epoch in range(1, 4):
    train_acc = random.uniform(0.6, 0.9)
    val_acc = train_acc - random.uniform(0.01, 0.1)
    print(f"Epoch {epoch}/3 - Train Accuracy: {train_acc:.2f} - Val Accuracy: {val_acc:.2f}")

print("\n✅ Model 'trained' successfully!")
print(f"Final Simulated Test Accuracy: {val_acc:.2f}")
