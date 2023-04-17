import tkinter as tk

# Create the main window

window = tk.Tk()

# Create a label for the password field

password_label = tk.Label(text="Password:")

# Create a text box for the password

password_entry = tk.Entry()

# Create a button to check the password

check_password_button = tk.Button(text="Check Password")

# Create a label for the password strength

password_strength_label = tk.Label(text="Password Strength:")

# Create a text box for the password strength

password_strength_entry = tk.Entry()

# Create a label for the compromised password status

compromised_password_status_label = tk.Label(text="Compromised Password Status:")

# Create a text box for the compromised password status

compromised_password_status_entry = tk.Entry()

# Add the label and text box for the password to the main window

password_label.pack()

password_entry.pack()

# Add the button to check the password to the main window

check_password_button.pack()

# Add the label and text box for the password strength to the main window

password_strength_label.pack()

password_strength_entry.pack()

# Add the label and text box for the compromised password status to the main window

compromised_password_status_label.pack()

compromised_password_status_entry.pack()

# Define a function to check the password

def check_password():

    # Get the password from the user

    password = password_entry.get()
# Generate the hash of the password

    hashed_password = generate_password_hash(password)

    # Check if the password is strong enough

    if is_password_strong_enough(password):

        password_strength_entry.delete(0, tk.END)

        password_strength_entry.insert(0, "Strong")

    else:

        password_strength_entry.delete(0, tk.END)

        password_strength_entry.insert(0, "Weak")

    # Check if the password is compromised

    if is_password_compromised(hashed_password):

        compromised_password_status_entry.delete(0, tk.END)

        compromised_password_status_entry.insert(0, "Compromised")

    else:

        compromised_password_status_entry.delete(0, tk.END)

        compromised_password_status_entry.insert(0, "Not compromised")

# Bind the check_password function to the click event of the check_password_button

check_password_button.config(command=check_password)

# Run the main loop

window.mainloop()
