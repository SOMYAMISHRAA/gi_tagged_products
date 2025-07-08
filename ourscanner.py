import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    decoded_objects = decode(frame)
    if decoded_objects:  # If at least one QR code is detected
        for obj in decoded_objects:
            print(obj.type)
            print(obj.data.decode('utf-8'))
        break  # Exit the while loop after scanning once

    cv2.imshow("Ourqr_code_scanner", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



