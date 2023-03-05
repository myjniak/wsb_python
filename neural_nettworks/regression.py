import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf

print(tf.config.list_physical_devices())

x = tf.range(-50, 120, 2, dtype=tf.float32)
noise = tf.keras.layers.GaussianNoise(15)
y = noise(-0.01 * x ** 3 + x ** 2 - 5 * x + 6, training=True)
x_train = tf.expand_dims(x, axis=-1)
y_train = y

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation="sigmoid"),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(1)
])

model.compile(loss=tf.keras.losses.mae,
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.002),
              metrics=["mae"])


def scheduler(epoch, lr):
    if epoch < 100:
        lr = 0.01
    elif epoch < 200:
        lr = 0.005
    elif epoch < 300:
        lr = 0.001
    elif epoch < 500:
        lr = 0.0005
    elif epoch < 700:
        lr = 0.0002
    else:
        lr = 0.0001
    return lr


fit = model.fit(x_train,
                y_train,
                callbacks=[tf.keras.callbacks.LearningRateScheduler(scheduler)],
                epochs=1000)

pd.DataFrame(fit.history).plot()
plt.ylabel("loss")
plt.xlabel("epoch")
plt.savefig("loss.png")
plt.clf()

x_pred = tf.range(-60, 130, dtype=tf.float32)
y_pred = model.predict(x_pred)

plt.scatter(x_train, y_train, c="green", label="Training data")
plt.plot(x_pred, y_pred, c="red", label="Predicted (learned) data")
plt.legend()
plt.savefig("regression.png")
plt.clf()
