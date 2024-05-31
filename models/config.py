import tensorflow as tf
from tf.keras.models import Sequential
from tf.keras.layers import Embedding, LSTM, Dense

def create_model(vocab_size, embedding_dim, max_length):
    model = Sequential()
    model.add(Embedding(vocab_size, embedding_dim, input_length=max_length))
    model.add(LSTM(128))
    model.add(Dense(1, activation='sigmoid'))
    return model

def train_model(model, X_train, y_train, epochs, batch_size):
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

def save_model(model, model_path):
    model.save(model_path)

def load_model(model_path):
    model = tf.keras.models.load_model(model_path)
    return model

# Example usage
vocab_size = 10000
embedding_dim = 100
max_length = 100
epochs = 10
batch_size = 32

model = create_model(vocab_size, embedding_dim, max_length)
train_model(model, X_train, y_train, epochs, batch_size)
save_model(model, 'feedback_model.h5')