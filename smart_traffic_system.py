import cv2
import numpy as np
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from threading import Timer

text_color = (0, 73, 255 )



# Function to perform object detection and counting
def detect_and_count_objects(frame, text_location):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Perform background subtraction
    fgmask = bg_subtractor.apply(blur)
    # Apply morphological operations to remove noise
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    # Find contours in the foreground mask
    contours, _ = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Initialize object count
    object_count = 0
    # Iterate through detected contours
    for contour in contours:
        # Compute the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)
        # Filter contours based on area
        if cv2.contourArea(contour) > min_contour_area:
            # Draw bounding box around detected object
            cv2.rectangle(frame, (x, y), (x + w, y + h), (46, 255, 0 ), 2)
            # Increment object count
            object_count += 1
    # Display object count on the frame
    cv2.putText(frame, f'Object Count: {object_count}', text_location, cv2.FONT_HERSHEY_SIMPLEX, 3.0, text_color, 6)
    
    return frame, object_count



move_labels = True

def menu_command():
    print("Menu item clicked")

# Create the default root window as a global variable
mtraffic_dashboard_v1 = Tk()
mtraffic_dashboard_v1.title("Mtraffic Monitoring Dasboard v1.1")
mtraffic_dashboard_v1.geometry("1500x750+10+10")  # Increase window size
mtraffic_dashboard_v1.resizable(False, False)
mtraffic_dashboard_v1.config(bg="black")


# Create a menu bar
menu_bar = Menu(mtraffic_dashboard_v1)

def open_map_window():
    map_window = Toplevel(mtraffic_dashboard_v1)
    map_window.title("Map")
    map_window.geometry("1500x750+10+10")
    map_window.resizable(False, False)
    map_window.config(bg="#4ea6a1")
    label_map = Label(map_window, text="Map Window Content", font=("Arial", 18))
    label_map.grid(row=0, column=0, padx=10, pady=10)
    
    image_path = "C:/Users/sahil/projects/traffic_management_system/map1.jpg" 
    image = Image.open(image_path)

    # Convert the Image object to a Tkinter-compatible image
    tk_image = ImageTk.PhotoImage(image)

    # Create a Label widget to display the image
    image_label = tk.Label(map_window, image=tk_image)
    image_label.grid(row=1, column=0, padx=10, pady=10)  # Use grid instead of pack


# intersection info Window
def open_intersection_info_window():
    intersection_info_window = Toplevel(mtraffic_dashboard_v1)
    intersection_info_window.title("Intersection Info")
    intersection_info_window.geometry("1500x750+10+10")
    intersection_info_window.resizable(False, False)
    intersection_info_window.config(bg="#4ea6a1")
    label_map = Label(intersection_info_window, text="Map Window Content", font=("Arial", 18))
    label_map.grid(row=0, column=0, padx=10, pady=10)
    

# version information window
def open_version_info_window():
    version_info_window = Toplevel(mtraffic_dashboard_v1)
    version_info_window.title("Version Information")
    version_info_window.geometry("1500x750+10+10")
    version_info_window.resizable(False, False)
    version_info_window.config(bg="#4ea6a1")
    label_map = Label(version_info_window, text="Map Window", font=("Arial", 18))
    label_map.grid(row=0, column=0, padx=10, pady=10)

    label_map1 = Label(version_info_window, text="M-Traffic Version 1.1", font=("Arial", 15))
    label_map1.grid(row=1, column=1, padx=10, pady=10)



# window for help
def open_help_window():
    help_window = Toplevel(mtraffic_dashboard_v1)
    help_window.title("Help")
    help_window.geometry("1500x750+10+10")
    help_window.resizable(False, False)
    help_window.config(bg="#4ea6a1")
    label_map = Label(help_window, text="Help Window", font=("Arial", 18))
    label_map.grid(row=0, column=0, padx=10, pady=10)

    label_map2 = Label(help_window, text="helpline 7039708212", font=("Arial", 15))
    label_map2.grid(row=1, column=0, padx=10, pady=10)

# Create a file menu 
home_menu = Menu(menu_bar, tearoff=0)
home_menu.add_command(label="Map", command=open_map_window)
home_menu.add_command(label="intersection info", command=open_intersection_info_window)
home_menu.add_separator()
home_menu.add_command(label="shutdown", command=mtraffic_dashboard_v1.quit)
menu_bar.add_cascade(label="Home", menu=home_menu)

# about menu
about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label="Sahil Ghodvinde", command=menu_command)
about_menu.add_command(label="Version information", command=open_version_info_window)
menu_bar.add_cascade(label="About", menu=about_menu)

# Create a help menu and 
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help", command=open_help_window)
menu_bar.add_cascade(label="Help", menu=help_menu)




# Add the menu bar to the root window
mtraffic_dashboard_v1.config(menu=menu_bar)



# Function to toggle label movement

# Define the function to toggle label movement
def toggle_label_movement():
    global move_labels
    move_labels = not move_labels

    if move_labels:
        toggle_button.config(bg="white", fg="green")
    else:
        toggle_button.config(bg="blue", fg="white")


# Create a button for automation
toggle_button = Button(mtraffic_dashboard_v1, text="Automation", command=toggle_label_movement, bg="blue", fg="white")
toggle_button.grid(row=1, column=6, padx=10, pady=5,sticky=W)
 
toggle_label_movement()

# Function to update the video feed in the Tkinter window
def update_video_feed():
    # Read frames from each video file
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()
    ret4, frame4 = cap4.read()

    # Break the loop if frames are not read successfully
    if not (ret1 and ret2 and ret3 and ret4):
        return

    # Perform object detection and counting for each video feed
    frame1_processed, count1 = detect_and_count_objects(frame1.copy(), text_location)
    frame2_processed, count2 = detect_and_count_objects(frame2.copy(), text_location)
    frame3_processed, count3 = detect_and_count_objects(frame3.copy(), text_location)
    frame4_processed, count4 = detect_and_count_objects(frame4.copy(), text_location)

    # Resize frames to fit into the window
    frame1_processed = cv2.resize(frame1_processed, (400, 300))
    frame2_processed = cv2.resize(frame2_processed, (400, 300))
    frame3_processed = cv2.resize(frame3_processed, (400, 300))
    frame4_processed = cv2.resize(frame4_processed, (400, 300))

    # Convert OpenCV frames to PIL format
    img1 = Image.fromarray(cv2.cvtColor(frame1_processed, cv2.COLOR_BGR2RGB))
    img2 = Image.fromarray(cv2.cvtColor(frame2_processed, cv2.COLOR_BGR2RGB))
    img3 = Image.fromarray(cv2.cvtColor(frame3_processed, cv2.COLOR_BGR2RGB))
    img4 = Image.fromarray(cv2.cvtColor(frame4_processed, cv2.COLOR_BGR2RGB))

    # Convert PIL images to Tkinter-compatible format
    img_tk1 = ImageTk.PhotoImage(image=img1)
    img_tk2 = ImageTk.PhotoImage(image=img2)
    img_tk3 = ImageTk.PhotoImage(image=img3)
    img_tk4 = ImageTk.PhotoImage(image=img4)

    # Update the positions of the labels based on the move_labels variable
    if move_labels:
        # Calculate label positions as before
        pass
    else:
        # Hide the labels
        count_label1.grid_forget()
        count_label2.grid_forget()
        count_label3.grid_forget()
        count_label4.grid_forget()
        green_light.grid_forget()
        red_light1.grid_forget()
        red_light2.grid_forget()
        red_light3.grid_forget()

    # Update the video feed labels
    label1.config(image=img_tk1)
    label1.image = img_tk1
    label2.config(image=img_tk2)
    label2.image = img_tk2
    label3.config(image=img_tk3)
    label3.image = img_tk3
    label4.config(image=img_tk4)
    label4.image = img_tk4

    # Update individual counter labels
    count_label1.config(text=f'Video 1: {count1}')
    count_label2.config(text=f'Video 2: {count2}')
    count_label3.config(text=f'Video 3: {count3}')
    count_label4.config(text=f'Video 4: {count4}')

    # Update counts in descending order
    counts = [(count_label1, count1), (count_label2, count2), (count_label3, count3), (count_label4, count4)]
    counts.sort(key=lambda x: x[1], reverse=True)
    for i, (label, count) in enumerate(counts):
        if move_labels:
            label.grid(row=i, column=2, padx=10, pady=1, sticky=W)
        else:
            label.grid_forget()

    # Schedule the next update after a delay
    mtraffic_dashboard_v1.after(10, update_video_feed)
    


# Initialize video captures for four video files
cap1 = cv2.VideoCapture('C:/Users/sahil/projects/traffic_management_system/Video2.mp4')
cap2 = cv2.VideoCapture('C:/Users/sahil/projects/traffic_management_system/Video3.mp4')
cap3 = cv2.VideoCapture('C:/Users/sahil/projects/traffic_management_system/Video4.mp4')
cap4 = cv2.VideoCapture('C:/Users/sahil/projects/traffic_management_system/Video5.mp4')


# Initialize background subtractor and kernel
bg_subtractor = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((5, 5), np.uint8)

# Minimum contour area for object detection
min_contour_area = 500


# Define text location for displaying object count
text_location = (5, 100)



# Create labels to display video feeds
label1 = Label(mtraffic_dashboard_v1)
label1.grid(row=0, column=0, padx=10, pady=10)
label2 = Label(mtraffic_dashboard_v1)
label2.grid(row=0, column=1, padx=10, pady=10)
label3 = Label(mtraffic_dashboard_v1)
label3.grid(row=1, column=0, padx=10, pady=10)
label4 = Label(mtraffic_dashboard_v1)
label4.grid(row=1, column=1, padx=10, pady=10)

# Create label variables for displaying counts
count_label1 = Label(mtraffic_dashboard_v1, text="Video 1: Count", fg="blue", font=("Arial", 12))
count_label2 = Label(mtraffic_dashboard_v1, text="Video 2: Count", fg="blue", font=("Arial", 12))
count_label3 = Label(mtraffic_dashboard_v1, text="Video 3: Count", fg="blue", font=("Arial", 12))
count_label4 = Label(mtraffic_dashboard_v1, text="Video 4: Count", fg="blue", font=("Arial", 12))




# Create labels to display video feeds
label1 = Label(mtraffic_dashboard_v1)
label1.grid(row=0, column=0, padx=10, pady=10)
label2 = Label(mtraffic_dashboard_v1)
label2.grid(row=0, column=1, padx=10, pady=10)
label3 = Label(mtraffic_dashboard_v1)
label3.grid(row=1, column=0, padx=10, pady=10)
label4 = Label(mtraffic_dashboard_v1)
label4.grid(row=1, column=1, padx=10, pady=10)

# Set background color for column 6
column_bg_color = "#ABB2B9 " 

# Create labels for lights
green_light = Label(mtraffic_dashboard_v1, text="Green", fg="green", font=("Arial", 12))
red_light1 = Label(mtraffic_dashboard_v1, text="Red", fg="red", font=("Arial", 12))
red_light2 = Label(mtraffic_dashboard_v1, text="Red", fg="red", font=("Arial", 12))
red_light3 = Label(mtraffic_dashboard_v1, text="Red", fg="red", font=("Arial", 12))

# Position the lights
green_light.grid(row=0, column=2, padx=100, pady=1, sticky=W)
red_light1.grid(row=1, column=2, padx=100, pady=1, sticky=W)
red_light2.grid(row=2, column=2, padx=100, pady=1, sticky=W)
red_light3.grid(row=3, column=2, padx=100, pady=1, sticky=W)



# Create a Label widget with text, font color, and font size
label = Label(mtraffic_dashboard_v1, text="M-traffic Monitoring Dashboard-v1.1", fg="blue", font=("Arial", 25))

# Position the Label widget using the grid method
label.grid(row=3, column=0,sticky=E)

# Create labels to display video feeds
label1 = Label(mtraffic_dashboard_v1)
label1.grid(row=0, column=0, padx=10, pady=10)
label2 = Label(mtraffic_dashboard_v1)
label2.grid(row=0, column=1, padx=10, pady=10)
label3 = Label(mtraffic_dashboard_v1)
label3.grid(row=1, column=0, padx=10, pady=10)
label4 = Label(mtraffic_dashboard_v1)
label4.grid(row=1, column=1, padx=10, pady=10)

# Create labels for lights
green_light = Label(mtraffic_dashboard_v1, text="Green", fg="green", font=("Arial", 12))
red_light1 = Label(mtraffic_dashboard_v1, text="Red", fg="red", font=("Arial", 12))
red_light2 = Label(mtraffic_dashboard_v1, text="Red", fg="red", font=("Arial", 12))
red_light3 = Label(mtraffic_dashboard_v1, text="Red", fg="red", font=("Arial", 12))

# Position the lights
green_light.grid(row=0, column=2, padx=100, pady=1, sticky=W)
red_light1.grid(row=1, column=2, padx=100, pady=1, sticky=W)
red_light2.grid(row=2, column=2, padx=100, pady=1, sticky=W)
red_light3.grid(row=3, column=2, padx=100, pady=1, sticky=W)

# Add buttons and signal indicators
button1 = Button(mtraffic_dashboard_v1, text="Signal 1", command=lambda: update_signal(1))
button1.grid(row=0, column=3, padx=10, pady=10)

button2 = Button(mtraffic_dashboard_v1, text="Signal 2", command=lambda: update_signal(2))
button2.grid(row=1, column=3, padx=10, pady=10)

button3 = Button(mtraffic_dashboard_v1, text="Signal 3", command=lambda: update_signal(3))
button3.grid(row=2, column=3, padx=10, pady=10)

button4 = Button(mtraffic_dashboard_v1, text="Signal 4", command=lambda: update_signal(4))
button4.grid(row=3, column=3, padx=10, pady=10)

circle1 = Canvas(mtraffic_dashboard_v1, width=20, height=20, bg="red", highlightthickness=0)
circle1.grid(row=0, column=4, padx=10, pady=10)

circle2 = Canvas(mtraffic_dashboard_v1, width=20, height=20, bg="red", highlightthickness=0)
circle2.grid(row=1, column=4, padx=10, pady=10)

circle3 = Canvas(mtraffic_dashboard_v1, width=20, height=20, bg="red", highlightthickness=0)
circle3.grid(row=2, column=4, padx=10, pady=10)

circle4 = Canvas(mtraffic_dashboard_v1, width=20, height=20, bg="red", highlightthickness=0)
circle4.grid(row=3, column=4, padx=10, pady=10)


# Function to update signal indicators
def update_signal(signal):
    # Reset all circles to red
    circle1.config(bg="red")
    circle2.config(bg="red")
    circle3.config(bg="red")
    circle4.config(bg="red")
    
    # Set the selected circle to green
    if signal == 1:
        circle1.config(bg="green")
    elif signal == 2:
        circle2.config(bg="green")
    elif signal == 3:
        circle3.config(bg="green")
    elif signal == 4:
        circle4.config(bg="green")




# Entry widget for the user to input the time interval
timer_entry = Entry(mtraffic_dashboard_v1)
timer_entry.grid(row=3, column=6, padx=10, pady=5)
timer_entry.insert(0, "10")  # Default value 10


automatic_signal_mode = False
# Function to set a specific circle to red
def set_circle_red(circle):
    circle.config(bg="red")

# Function to toggle automatic signal mode
def toggle_automatic_signal_mode():
    global automatic_signal_mode
    automatic_signal_mode = not automatic_signal_mode
    if automatic_signal_mode:
        toggle_automatic_button.config(bg="green") 
        # Start automatic signal timer
        time_interval = float(timer_entry.get())  # Read the time interval from the entry widget
        automatic_signal_timer(time_interval)
    else:
        toggle_automatic_button.config(bg="red")    

# Function to automatically switch signal after the specified time interval
def automatic_signal_timer(time_interval):
    if automatic_signal_mode:
        # Reset all circles to red
        circle1.config(bg="red")
        circle2.config(bg="red")
        circle3.config(bg="red")
        circle4.config(bg="red")

        # Set the first circle to green
        circle1.config(bg="green")

        # Set a timer to switch to the next circle after the specified time interval
        timer = Timer(time_interval, rotate_signals)
        timer.start()

# Function to rotate signals automatically
def rotate_signals():
    if automatic_signal_mode:
        # Get the current color of the first circle
        current_color = circle1.cget('bg')

        # Rotate the signals by changing the color
        if current_color == "green":
            circle1.config(bg="red")
            circle2.config(bg="green")
        elif current_color == "red":
            circle2.config(bg="red")
            circle3.config(bg="green")
        elif current_color == "green":
            circle3.config(bg="red")
            circle4.config(bg="green")
        elif current_color == "green":
            circle4.config(bg="red")
            circle1.config(bg="green")

        # Schedule the next rotation
        time_interval = float(timer_entry.get())  
        timer = Timer(time_interval, rotate_signals)
        timer.start()


# Create a button to toggle automatic signal mode
toggle_automatic_button = Button(mtraffic_dashboard_v1, text="Frequency Mode", command=toggle_automatic_signal_mode, fg="white",bg="red")
toggle_automatic_button.grid(row=2, column=6, padx=10, pady=5, sticky=W)

toggle_automatic_button = Button(mtraffic_dashboard_v1, text="Distress Button", fg="white",bg="red")
toggle_automatic_button.grid(row=0, column=6, padx=10, pady=5, sticky=W)

# Update signal function to handle automatic mode
def update_signal(signal):
    if not automatic_signal_mode:
        # Reset all circles to red
        circle1.config(bg="red")
        circle2.config(bg="red")
        circle3.config(bg="red")
        circle4.config(bg="red")
        
        # Set the selected circle to green
        if signal == 1:
            circle1.config(bg="green")
        elif signal == 2:
            circle2.config(bg="green")
        elif signal == 3:
            circle3.config(bg="green")
        elif signal == 4:
            circle4.config(bg="green")





# Start updating the video feeds
update_video_feed()


# Run the Tkinter event loop
mtraffic_dashboard_v1.mainloop()

# Release video captures and close all OpenCV windows
cap1.release()
cap2.release()
cap3.release()
cap4.release()
cv2.destroyAllWindows()