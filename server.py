import socket
#import socket
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os 
from keras.preprocessing import image
model = tf.keras.models.load_model('model.h5')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 1234
address = (ip,port)
server.bind(address)
server.listen(1)

#making prediction and store them inside the array.
def prediction(results):
    if(results[0][0]) == 1:
        return "Paper"
    elif results[0][1] == 1:
        return "Rock"
    elif results[0][2] == 1:
        return "Scissors"
    else:
        return "Unknown"
    
def predict_image():
    #preprocessing and loading 
    img = image.load_img('rock.png', target_size=(150,150))
    x = image.ing_to_array(img)
    x = np.expand_dims(x, axis=0)
    
    #model 
    images = np.vstack([x])
    classes = model.predict(images, batch_size= 10)
    return classes

print("[*] Started listening on ", ip, ":", port)
client,addr = server.accept()
print("[*] Got a connection from ", addr[0], " :", addr[1])
while True:
    data = client.recv(1024).decode()
    print("[*] Received ", data, " from the client.\n")
    print(" Processing data.\n")
    if(data=="client"):
        
        client.send(("Rock, Paper and Scissors image classification server, Vinh Pham,'[%s] %s %(ctime().data\n)").encode())
    
        print(" Processing done. \n [*] Reply sent")
    elif(data=="client rock.jpg"):
        #result returning
        predictionDATA = predict_image()
        predict = prediction(predictionDATA).encode()
                             
        client.sendall(predict)
        break
    else:
        client.send(("Invalid data").encode())
        print(" Processing done because Invalid data \n")
client.close()
