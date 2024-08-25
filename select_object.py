import cv2

# image_path
image_path = 'image.jpg'
extension = image_path.split('.')[-1]

# load image
img = cv2.imread(image_path, cv2.IMREAD_COLOR)
canvas = img.copy()
H, W, _ = canvas.shape

# set window
cv2.namedWindow('Draw', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Draw', 800, 600)

# display the canvas
cv2.imshow('Draw', canvas)

# global coordinates and drawing state
x = 0
y = 0
drawing = False
x_coordinates = []
y_coordinates = []

# mouse callback function
def draw(event, current_x, current_y, flags, params):
    # hook up global variables
    global x, y, drawing, x_coordinates, y_coordinates, H, W

    # handle mouse down event
    if event == cv2.EVENT_LBUTTONDOWN:
        # update coordinates
        x = current_x
        y = current_y

        # enable drawing flag
        drawing = True

    # handle mouse move event
    elif event == cv2.EVENT_MOUSEMOVE:
        # draw only if mouse is down
        if drawing:

            # draw the line
            cv2.line(canvas, (current_x, current_y), (x, y), (0,0,255), thickness=5)

            # update coordinates
            x, y = current_x, current_y
            x_coordinates.append(current_x)
            y_coordinates.append(current_y)

    # handle mouse up event
    elif event == cv2.EVENT_LBUTTONUP:
        # disable drawing flag
        drawing = False

# bind mouse events
cv2.setMouseCallback('Draw', draw)

# infinite drawing loop
while True:
    # update canvas
    cv2.imshow('Draw', canvas)

    # break out of a program on 'Esc' button hit
    if cv2.waitKey(1) & 0xFF == 27: break

    # break out of a program on 'X' close button
    if cv2.getWindowProperty('Draw', cv2.WND_PROP_VISIBLE) < 1: break

x_min = max(min(x_coordinates), 0)
y_min = max(min(y_coordinates), 0)
x_max = min(max(x_coordinates), W-1)
y_max = min(max(y_coordinates), H-1)

cropped = img[y_min:y_max+1, x_min:x_max+1]

# cv2.imwrite(f'image_with_selection.{extension}', canvas)
cv2.imwrite(f'selected.{extension}', cropped)

# clean up windows
cv2.destroyAllWindows()