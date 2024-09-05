import tkinter as tk
from main import start

def start_action():
    # Get text from the input fields
    text1 = entry1.get()
    text2 = entry2.get()
    text3 = entry3.get()
    text4 = entry4.get()
    text5 = entry5.get()
    text6 = entry6.get()

    # Print the text
    print("Text Field 1:", text1)
    print("Text Field 2:", text2)
    print("Text Field 3:", text3)
    print("Text Field 4:", text4)

    start(text1, text2, text3, text4, text5, text6)

def restart_action():
    # Clear the text fields
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)
    entry6.delete(0, tk.END)
    print("Text fields cleared!")

# Create the main window
root = tk.Tk()
root.title("Basic UI")

# Set the size of the window
root.geometry("400x400")

# Create a frame to center the text fields
frame = tk.Frame(root)
frame.pack(expand=True)

# Create and place the labels and text fields in the center

tk.Label(frame, text="Your CID:").pack(pady=2)
entry1 = tk.Entry(frame, width=30)
entry1.pack(pady=2)

tk.Label(frame, text="Password:").pack(pady=2)
entry2 = tk.Entry(frame, width=30)
entry2.pack(pady=2)

tk.Label(frame, text="code1:").pack(pady=2)
entry3 = tk.Entry(frame, width=30)
entry3.pack(pady=2)

tk.Label(frame, text="code2:").pack(pady=2)
entry4 = tk.Entry(frame, width=30)
entry4.pack(pady=2)

tk.Label(frame, text="code3:").pack(pady=2)
entry5 = tk.Entry(frame, width=30)
entry5.pack(pady=2)

tk.Label(frame, text="code4:").pack(pady=2)
entry6 = tk.Entry(frame, width=30)
entry6.pack(pady=2)

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create and place the Start and Restart buttons
start_button = tk.Button(button_frame, text="Start", command=start_action, width=10)
start_button.pack(side="left", padx=10, pady=10)

restart_button = tk.Button(button_frame, text="Clear", command=restart_action, width=10)
restart_button.pack(side="right", padx=10, pady=10)

# Run the application
root.mainloop()
