
# coding: utf-8

# # Пример верификации человека на фотографии с помощью библиотеки dlib
# 
# **Верификация** - это задача определения, находится ли на изображении нужный нам человек, или нет. 
# 
# Мы будем решать задачу верификации человека на двух фотографиях. Нам нужно будет определить, один человек изображен на двух фотографиях, или нет.

# In[122]:

import urllib.request
import dlib
from skimage import io
from scipy.spatial import distance

# # Создаем модели для поиска и нахождения лиц в dlib
# 
# Предварительно обученные модели можно скачать по ссылкам:
# - http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
# - http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2
# 
# Файлы с моделями нужно разархивировать и положить в каталог с этим notebook

# In[123]:

sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()

# Загружаем первую фотографию

# In[124]:

img = io.imread('standard_Alex.jpg')


# Показываем фотографию средствами dlib

# In[125]:

win1 = dlib.image_window()
win1.clear_overlay()
win1.set_image(img)


# # Находим лицо на фотографии

# In[126]:

dets = detector(img, 1)


# In[127]:

for k, d in enumerate(dets):
    #print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(k, d.left(), d.top(), d.right(), d.bottom()))
    shape = sp(img, d)
    win1.clear_overlay()
    win1.add_overlay(d)
    win1.add_overlay(shape)


# # Извлекаем дескриптор из лица

# In[128]:

face_descriptor1 = facerec.compute_face_descriptor(img, shape)


# Печатаем дексриптор

# In[129]:

#print(face_descriptor1)


# # Загружаем и обрабатываем вторую фотографию

# In[130]:

img = io.imread('checkface.jpg')
win2 = dlib.image_window()
win2.clear_overlay()
win2.set_image(img)
dets_webcam = detector(img, 1)
for k, d in enumerate(dets_webcam):
    #print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(k, d.left(), d.top(), d.right(), d.bottom()))
    shape = sp(img, d)
    win2.clear_overlay()
    win2.add_overlay(d)
    win2.add_overlay(shape)


# In[131]:

face_descriptor2 = facerec.compute_face_descriptor(img, shape)


# # Рассчитываем Евклидово расстояние между двумя дексрипторами лиц
# 
# В dlib рекомендуется использовать граничное значение Евклидова расстояния между дескрипторами лиц равное 0.6. Если Евклидово расстояние меньше 0.6, значит фотографии принадлежат одному человеку. 
# 
# С использованием такой метрики dlib обеспечивает точность 99.38% на тесте распознавания лиц Labeled Faces in the Wild. Подробности можно посмотреть по ссылке - http://dlib.net/face_recognition.py.html

# In[132]:

a = distance.euclidean(face_descriptor1, face_descriptor2)
#print(a)
a=round(a, 2)
urllib.request.urlopen('http://127.0.0.1/objects/?object=admin&op=set&p=EuclidValue&v=%s' % a)
