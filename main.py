import cv2
import qrcode
from flask import Flask, render_template, request
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('qr.html')

@app.route('/', methods=['POST'])
def generateQR():
    memory = BytesIO()
    data = request.url
    img = qrcode.make(data)
    img.save(memory)
    memory.seek(0)

    base64_img = "data:image/png;base64," + \
                 b64encode(memory.getvalue()).decode('ascii')
    return render_template('qr.html', data=base64_img)
"""
    img_qrcode = cv2.imread("DT.jpg")
    detector = cv2.QRCodeDetector()

    data, bbox, clear_qrcode = detector.detectAndDecode(img_qrcode)

    print(data)
    print(bbox)

    cv2.imshow("rez", clear_qrcode)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
"""


if __name__ == "__main__":
    app.run(debug=True)


