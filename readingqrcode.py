import qrcode
# example data
data = "https://www.thepythoncode.com"
# output file name
filename = "site.png"
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)

import cv2
# read the QRCODE image
img = cv2.imread("IDCard-Satya.png")

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)

# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
        cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)

# display the result
cv2.imshow("img", img)
cv2.imwrite("result.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()