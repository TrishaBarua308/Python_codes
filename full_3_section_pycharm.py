import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

# ==========================
# SECTION 1 — DATA LOADING
# ==========================

dataset_path = r"D:\Desktop\Thesis\Fish_dataset"
valid_classes = ['Tengra', 'Taki', 'Sorputi', 'Sol', 'Sing', 'Byen']

images = []
labels = []

# Load images
for cls in valid_classes:
    folder = os.path.join(dataset_path, cls)
    if not os.path.isdir(folder):
        continue

    for file in os.listdir(folder):
        if file.lower().endswith(".jpg"):
            img_path = os.path.join(folder, file)
            img = cv2.imread(img_path)
            if img is None:
                continue

            img = cv2.resize(img, (224, 224))
            img = img[..., ::-1]  # BGR → RGB

            images.append(img)
            labels.append(cls)

X = np.array(images) / 255.0
labels = np.array(labels)

print("Total images:", len(X))

# Encode labels
le = LabelEncoder()
y = le.fit_transform(labels)
y = to_categorical(y)

print("Classes:", le.classes_)
print("Label shape:", y.shape)

# Split dataset
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, shuffle=True, stratify=y, random_state=42)

X_val, X_test, y_val, y_test = train_test_split( X_temp, y_temp, test_size=0.66, shuffle=True, stratify=y_temp, random_state=42)

print("Train:", X_train.shape)
print("Val:", X_val.shape)
print("Test:", X_test.shape)

# ==========================
# SECTION 2 — CUSTOM VGG19
# ==========================

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, CSVLogger

model = Sequential()

# Block 1
model.add(Conv2D(64, (3,3), activation='relu', padding='same', input_shape=(224,224,3)))
model.add(Conv2D(64, (3,3), activation='relu', padding='same'))
model.add(MaxPooling2D())

# Block 2
model.add(Conv2D(128, (3,3), activation='relu', padding='same'))
model.add(Conv2D(128, (3,3), activation='relu', padding='same'))
model.add(MaxPooling2D())

# Block 3
model.add(Conv2D(256, (3,3), activation='relu', padding='same'))
model.add(Conv2D(256, (3,3), activation='relu', padding='same'))
model.add(Conv2D(256, (3,3), activation='relu', padding='same'))
model.add(MaxPooling2D())

# Block 4
model.add(Conv2D(512, (3,3), activation='relu', padding='same'))
model.add(Conv2D(512, (3,3), activation='relu', padding='same'))
model.add(Conv2D(512, (3,3), activation='relu', padding='same'))
model.add(MaxPooling2D())

# Block 5
model.add(Conv2D(512, (3,3), activation='relu', padding='same'))
model.add(Conv2D(512, (3,3), activation='relu', padding='same'))
model.add(Conv2D(512, (3,3), activation='relu', padding='same'))
model.add(MaxPooling2D())

# Fully Connected Layers
model.add(Flatten())
model.add(Dense(4096, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(4096, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(valid_classes), activation='softmax'))

model.summary()

# Compile
model.compile(optimizer=Adam(0.0001), loss="categorical_crossentropy", metrics=["accuracy"])

# Callbacks
es = EarlyStopping(patience=2, restore_best_weights=True)
logger = CSVLogger("training_log.csv")

# Train (ONLY 2 epochs)
history = model.fit( X_train, y_train,validation_data=(X_val, y_val),epochs=2, batch_size=4,callbacks=[es, logger] )

# Save model
model.save("custom_vgg19_model.h5")

# Evaluate
train_loss, train_acc = model.evaluate(X_train, y_train)
test_loss, test_acc = model.evaluate(X_test, y_test)

print("Train Accuracy:", train_acc)
print("Test Accuracy:", test_acc)

# ==========================
# SECTION 3 — PLOTS
# ==========================

plt.plot(history.history['accuracy'], label='Train Acc')
plt.plot(history.history['val_accuracy'], label='Val Acc')
plt.legend()
plt.title("Accuracy")
plt.show()

plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.legend()
plt.title("Loss")
plt.show()

# ==========================
# SECTION 4 — CONFUSION MATRIX
# ==========================

from sklearn.metrics import confusion_matrix, classification_report

y_pred = model.predict(X_test)
y_pred = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)

print(classification_report(y_true, y_pred, target_names=le.classes_))

cm = confusion_matrix(y_true, y_pred)
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.colorbar()
plt.show()
