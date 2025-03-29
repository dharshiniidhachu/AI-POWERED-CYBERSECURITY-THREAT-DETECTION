import customtkinter as ctk
import subprocess
import tkinter as tk
import time

def open_xss_detection():
    subprocess.Popen(["python", "Project codes/xss_test.py"])

def open_url_detection():
    subprocess.Popen(["python", "Project codes/demo.py"])

def open_email_attack_functionality():
    subprocess.Popen(["python", "Project codes/Email_Attack.py"])

def open_about_page():
    subprocess.Popen(["python", "Project codes/About.py"])

def quit_application():
    root.destroy()

button_configs = [
    ("XSS Detection", open_xss_detection),
    ("URL Detection", open_url_detection),
    ("Email Attack", open_email_attack_functionality),
    ("About", open_about_page)
]

root = ctk.CTk()
root.geometry("800x700")

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

main_label = ctk.CTkLabel(master=root, text="CyberLock ...!", font=("Arial", 18), text_color="skyblue")
main_label.pack(pady=20)

frame_width = root.winfo_screenwidth() // 2

left_frame = ctk.CTkFrame(master=root, width=frame_width, fg_color="black")
left_frame.pack(side="left", fill="both", expand=True)

right_frame = ctk.CTkFrame(master=root, width=frame_width, fg_color="black")
right_frame.pack(side="right", fill="both", expand=True)

def handle_app_click(function):
    function()

button_frame = ctk.CTkFrame(master=left_frame, fg_color="black")
button_frame.pack(pady=20)
for label_text, command in button_configs:
    button = ctk.CTkButton(
        master=button_frame,
        text=label_text,
        width=200,
        height=100,
        command=lambda f=command: handle_app_click(f),
        corner_radius=8,
        fg_color="skyblue",
        text_color="black"
    )
    button.pack(side="top", padx=20, pady=10)

description_frame = ctk.CTkFrame(master=right_frame, fg_color="black")
description_frame.pack(pady=20)

app_description = """
This application provides various security functionalities:

1. XSS Detection: Protects against cross-site scripting attacks.

2. URL Detection: Detects suspicious URLs.

3. Email Attack: Simulates email attacks for testing purposes.

4. About: Information about the application.
"""

description_label = ctk.CTkLabel(master=description_frame, text=app_description, font=("Arial", 15), justify=ctk.LEFT,
                                 text_color="skyblue")
description_label.pack(pady=20, padx=20)

# Team details
team_details = """
Team Name: WhyNot
Team Members:
- Dharshini S
- Shobana S
- Swathi S
"""

team_label = ctk.CTkLabel(master=description_frame, text=team_details, font=("Arial", 15), justify=ctk.LEFT,
                           text_color="skyblue")
team_label.pack(pady=20, padx=10)

def open_help_page():
    phone_label = ctk.CTkLabel(master=description_frame, text="Phone Number: +91 9448977671", font=("Arial", 15),
                               justify=ctk.LEFT, text_color="skyblue")
    phone_label.pack(side="top", pady=10)



exit_button = ctk.CTkButton(
    master=description_frame,
    text="Exit",
    command=quit_application,
    corner_radius=8,
    fg_color="skyblue",
    text_color="black"
)
exit_button.pack(side="bottom", pady=20)

# Animation
def animate_label(label, text, delay=100):
    def update_text(i=0):
        if i < len(text):
            current_text = text[:i + 1]
            label.configure(text=current_text)  # Use configure instead of config
            label.after(delay, update_text, i + 1)
    update_text()

animate_label(main_label, "CyberLock ...!", delay=150)

root.mainloop()