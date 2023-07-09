from keras.datasets import mnist
from keras import models
from keras import layers
#models se utiliza para definir y construir modelos de redes neuronales,
#mientras que la biblioteca layers se utiliza para crear las diferentes capas que componen la arquitectura de la red neuronal.
from keras.utils import to_categorical

#se importan los vectores de caracteristicas del data set
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
#las "imagenes" son vectores con numeros del 0 al 255 (blanco y negro), que cada pixel se representa con un numero y se recorre horizontalmente
#los labels son vectores de etiquetas que se asocian uno a uno con los vectores de caracteristicas, y son el valor numerico de la imagen asociada a la etiqueta

network = models.Sequential()
#n modelo secuencial es aquel en el que las capas se apilan una encima de la otra en secuencia.

network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255
#En este paso se normalizó el vector desde 0 hasta 1 y se pasó a la forma de una matriz de 60000 por 28 por 28

#También necesitamos codificar categóricamente las etiquetas, se usa hot encoding para asociar cada numero a un vector
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

#se entrena la red neuronal, con un tamaño de lote de datos de 128
network.fit(train_images, train_labels, epochs=6, batch_size=128)

test_loss, test_acc = network.evaluate(test_images, test_labels)  #se testea la NN con nuevos datos

print('test_acc:', test_acc)  #porcentaje de acierto
