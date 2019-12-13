import os,cv2, sys
import numpy as np
from keras import backend as K
from keras.models import model_from_json, load_model

K.clear_session() # Clear previous models from memory.

json_file = open('bacteria_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("bacteria-classifier.h5")
#loaded_model=load_model('bacteria-classifier.h5')
loaded_model.summary()

labels_name={'Candida_albicans':0,'Clostridium_perfringens':1,'Lactobacillus_paracasei':2,'Staphylococcus_saprophiticus':3}

image_path = sys.argv[1]
img = cv2.imread(image_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
image = np.array(img)
image = image.reshape(1,244,244)
print(image.shape)

testPred = loaded_model.predict_classes(image.reshape(image.shape[0], 1, 244, 244))
prediction = testPred[0]
print("Class: ", prediction)


