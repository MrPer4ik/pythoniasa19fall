import cv2
import logging
import time
import path
from imutils.object_detection import non_max_suppression

CASCADESFILE = 'data/haarcascades/haarcascade_frontalface_default.xml'
SMILEFILE = 'data/haarcascades/haarcascade_smile.xml'
LOGFILE = 'build/faces.log'

#path.Path('build').mkdir()
logging.basicConfig(filename=LOGFILE, level='DEBUG')
def main():

    model = cv2.CascadeClassifier(CASCADESFILE)
    modelesmile = cv2.CascadeClassifier(SMILEFILE)

    webcam = cv2.VideoCapture(0)

    # infinite image processing loop
    while True:

        if not webcam.isOpened():
            logging.warning('Unable to connect to camera.')
            time.sleep(5)
            continue

        # get image from camera
        ret, frame = webcam.read()

        # convert image to grayscale
        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # add blur
        grayframe = cv2.GaussianBlur(grayframe, (21, 21), 0)

        # detect faces
        faces = model.detectMultiScale(grayframe, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        smile = modelesmile.detectMultiScale(grayframe, scaleFactor=1.1, minNeighbors=5, minSize=(10, 10))
        
        # adding non_max_suppression to avoid overlapping
        faces = non_max_suppression(faces, probs=None, overlapThresh=0.65)
        smile = non_max_suppression(smile, probs=None, overlapThresh=0.65)

        logging.info(f'Detected faces: {len(faces)}')

        # add boxes
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        for (x, y, w, h) in smile:
            if bool(list(faces)):
                if all( (x1 <= x <= x + w <= x1 + w1 ) and (y1 <= y <= y + h <= y1 + h1) for (x1,y1,h1,w1) in faces):
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # show image
        cv2.imshow('Video', frame)

        # stop if user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # close everything
    webcam.release()
    cv2.destroyWindows()


if __name__ == '__main__':
    main()