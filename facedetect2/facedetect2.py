import dlib
import cv2
from skimage import io
from scipy.spatial import distance

#iii=0
fn_haar = 'haarcascade_frontalface_default.xml'
haar_cascade = cv2.CascadeClassifier(fn_haar)

sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()

webcam = cv2.VideoCapture(0) #для использования ип камеры вместо 0 вставить ип адрес камеры
size = 4
(im_width, im_height) = (300, 300)

img = io.imread('standard_Alex.jpg')
# win1 = dlib.image_window()
# win1.clear_overlay()
# win1.set_image(img)
dets = detector(img)

for k, d in enumerate(dets):
    shape = sp(img, d)
    # win1.clear_overlay()
    # win1.add_overlay(d)
    # win1.add_overlay(shape)
#
face_descriptor1 = facerec.compute_face_descriptor(img, shape)

while True:
    # Цикл, пока камера не работает
    rval = False
    while (not rval):

        # Поместите изображение с веб-камеры в 'frame'
        (rval, frame) = webcam.read()
        if (not rval):
            print("Failed to open webcam. Trying again...")

    # frame = cv2.resize(frame, (int(frame_width/2), int(frame_height/2)))
    frame = cv2.flip(frame, 1, 0)  # Flip, чтобы действовать как зеркало

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(8, 8))
    clahe_image = clahe.apply(gray, 0)



    mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))

    # Обнаруживать лица
    faces = haar_cascade.detectMultiScale(mini)

    faces = sorted(faces, key=lambda x: x[3])
    if faces:
        face_i = faces[0]
        (x, y, w, h) = [v * size for v in face_i]

        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (im_width, im_height))

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # cv2.putText(frame, "Sasha", (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,
        #             1, (0, 255, 0))

    dets = detector(clahe_image)
    for d in dets:
        # cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 2)
        shape = sp(frame, d)

    # face_resize=cv2.cvtColor(face_resize, cv2.COLOR_GRAY2RGB)

    face_descriptor2 = facerec.compute_face_descriptor(frame, shape)

    a = distance.euclidean(face_descriptor1, face_descriptor2)
    print(a)


    # Покажите изображение и проверьте нажатие ESC.
    cv2.imshow('OpenCV', frame)
    key = cv2.waitKey(10)
    #if key == 27:
        #break
