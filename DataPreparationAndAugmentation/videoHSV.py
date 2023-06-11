import cv2 as cv2

cap = cv2.VideoCapture('test6.mp4')

img_array = []

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    img_array.append(hsv)
    # Display the resulting frame
    cv2.imshow('frame',hsv)
    height, width, layers = hsv.shape
    size = (width, height)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()

cv2.destroyAllWindows()

out = cv2.VideoWriter('test6HSV.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
