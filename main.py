import cv2
import pytesseract

PATH_TO_TESSERACT_EXE = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = PATH_TO_TESSERACT_EXE
PATH_TO_IMG = 'itc_f.jpeg'


def read_chars(path_to_img = PATH_TO_IMG):
    img = cv2.imread(path_to_img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h_img, w_img, c_img = img.shape
    text = []
    bounding_boxes = pytesseract.image_to_boxes(img)
    for b in bounding_boxes.splitlines():
        s = b.split()[0]
        x, y, w, h, z = [int(c) for c in b.split()[1:]]
        cv2.rectangle(img, (x, h_img - y), (w, h_img - h), (200,200,0), 2)
        cv2.putText(img, s, (x, h_img-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (200, 200, 0))
        text.append(s)
    cv2.imshow('img', img)
    cv2.waitKey(0)


def read_words(path_to_img = PATH_TO_IMG):
    img = cv2.imread(path_to_img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h_img, w_img, c_img = img.shape
    text = []
    bounding_boxes = pytesseract.image_to_data(img)
    for en, b in enumerate(bounding_boxes.splitlines()):
        if en > 0:  # ignore first header line
            s = b.split()
            if len(s) == 12:  # has word
                x, y, w, h = [int(c) for c in b.split()[6:10]]
                cv2.rectangle(img, (x, y), (w+x, h+y), (250,0,100), 1)
                cv2.putText(img, s[11], (x, y+h+22), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (250,0,100))
                text.append(s[11])

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.imwrite('itc_detected.jpeg', img)
    return text


if __name__ == '__main__':
    # read_chars()
    read_words()