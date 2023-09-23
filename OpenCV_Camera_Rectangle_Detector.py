import cv2

# Create a VideoCapture object to access the webcam
cap = cv2.VideoCapture(0)  # 0 represents the default webcam index

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Failed to open the webcam")
    exit()

# Initialize the desired width and height of the frame
frame_width = 1080
frame_height = 720

# Initialize the rectangle width and height
rectangle_width = 75
rectangle_height = 75

# Initialize the initial gap between rectangles (height and width)
initial_gap_between_rectangles_height = 5
initial_gap_between_rectangles_width = 10
gap_to_frame_sides_height = 30
gap_to_frame_sides_width = 30

# Function to calculate the number of rectangles that can fit in a row and column
def calculate_num_rectangles():
    # Get the current size of the frame
    actual_frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    actual_frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # Calculate the number of rectangles that can fit in a row and column based on the actual frame size
    num_rectangles_row = int((actual_frame_width - 2 * gap_to_frame_sides_width) / (rectangle_width + gap_between_rectangles_width))
    num_rectangles_col = int((actual_frame_height - 2 * gap_to_frame_sides_height) / (rectangle_height + gap_between_rectangles_height))

    return num_rectangles_row, num_rectangles_col

# Set the initial gap values
gap_between_rectangles_height = initial_gap_between_rectangles_height
gap_between_rectangles_width = initial_gap_between_rectangles_width

# Initialize the number of rectangles
num_rectangles_row, num_rectangles_col = calculate_num_rectangles()

# Initialize the list to store the rectangles
rectangles = []

# Function to draw a rectangle on the frame
def draw_rectangle(frame, x, y, width, height):
    cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 255), 2)

# Function to add a rectangle
def add_rectangle():
    # Calculate the row and column index for the new rectangle based on the number of existing rectangles
    num_rectangles = len(rectangles)
    row_index = num_rectangles // num_rectangles_row
    col_index = num_rectangles % num_rectangles_row

    # Calculate the x and y coordinates for the new rectangle
    x = gap_to_frame_sides_width + col_index * (rectangle_width + gap_between_rectangles_width)
    y = gap_to_frame_sides_height + row_index * (rectangle_height + gap_between_rectangles_height)

    # Append the new rectangle parameters to the rectangle list
    rectangles.append([x, y, rectangle_width, rectangle_height])
    
#Initialize the actual_frame variable
actual_frame = None

# Read and display frames from the webcam
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        print("Failed to capture frame")
        break
    
    # Draw all the rectangles in the frame
    for rect in rectangles:
        draw_rectangle(frame, rect[0], rect[1], rect[2], rect[3])
    
    # Resize the frame to the desired width and height
    frame = cv2.resize(frame, (frame_width, frame_height))
    
    # Display the frame
    cv2.imshow("Webcam", frame)

    # Check for key press events
    key = cv2.waitKey(1)
    if key == ord('a') or key == ord('A'):
        if len(rectangles) < num_rectangles_row * num_rectangles_col:
            add_rectangle()

    # Wait for the 'q' key to be pressed to exit
    if key == ord('q') or key == ord('Q'):
        break

# Release the VideoCapture object and close the windows
cap.release()
cv2.destroyAllWindows()

# Gather all rectangles in a list
rectangle_list = []
for rect in rectangles:
    rectangle_list.append(rect[:])

# Print the rectangle list
print(rectangle_list)
    
if actual_frame is not None:
    cv2.imshow("Original Frame", actual_frame)
    cv2.destroyAllWindows()