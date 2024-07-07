import cv2
from pyzbar.pyzbar import decode
def scan_qr_code():
    # Initialize camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the frame
        cv2.imshow('QR Code Scanner', frame)

        # Attempt to decode QR code
        decoded_objs = decode(frame)
        for obj in decoded_objs:
            print(f"QR Code data: {obj.data.decode('utf-8')}")

            # Open a web browser or perform an action based on the decoded data
            # For example, open a web link if the data starts with 'http'
            data = obj.data.decode('utf-8')
            if data.startswith('http'):
                import webbrowser
                webbrowser.open(data)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    scan_qr_code()
