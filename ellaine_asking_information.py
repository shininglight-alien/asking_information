import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def confirm_data(
    first_name,
    middle_name,
    last_name,
    age,
    barangay,
    municipality,
    province,
    region,
    country,
):
    confirmation_window = tk.Toplevel()
    confirmation_window.title("Confirmation")
    fg = ("#000000",)
    bg = ("#FFC0CB",)
    confirmation_window.geometry("500x300")

    confirmation_label = tk.Label(
        confirmation_window,
        text=f"Please confirm the following information:\n\n"
        f"Your name is {first_name} {middle_name} {last_name}.\n"
        f"You are {age} years old.\n"
        f"You live in {barangay}, {municipality}, {province}, Region {region}, {country}.",
        font=("Courier New", 12),
        bg="#FFC0CB",
        fg="#000000",
    )
    confirmation_label.pack()

    confirm_button = tk.Button(
        confirmation_window,
        text="Confirm",
        font=("Courier New", 14),
        command=lambda: print_and_exit(
            first_name,
            middle_name,
            last_name,
            age,
            barangay,
            municipality,
            province,
            region,
            country,
            confirmation_window,
        ),
        bg="#FF1493",
        fg="#000000",
    )
    confirm_button.pack()


def print_and_exit(
    first_name,
    middle_name,
    last_name,
    age,
    barangay,
    municipality,
    province,
    region,
    country,
    window,
):
    print(f"Full Name: {first_name} {middle_name} {last_name}")
    print(f"Age: {age} years old")
    print(
        f"Address: {barangay}, {municipality}, {province}, Region {region}, {country}"
    )
    print("---------------------------------")
    window.destroy()
    tk.messagebox.showinfo(
        title="Success",
        message="Congratulations, your information was submitted.",
    )


def submit_data():
    agreement = agreement_var.get()

    if agreement == "Agree":
        first_name = first_name_entry.get()
        middle_name = middle_name_entry.get()
        last_name = last_name_entry.get()
        if first_name and last_name:
            age = age_spinbox.get()
            barangay = barangay_entry.get()
            municipality = municipality_entry.get()
            province = province_entry.get()
            region = region_entry.get()
            country = country_entry.get()

            confirm_data(
                first_name,
                middle_name,
                last_name,
                age,
                barangay,
                municipality,
                province,
                region,
                country,
            )

        else:
            tk.messagebox.showwarning(
                title="Error", message="No first name and last name entered."
            )
    elif agreement == "Disagree":
        tk.messagebox.showinfo(
            title="Information",
            message="Thank you, but your information was not submitted.",
        )


window = tk.Tk()
window.title("Ellaine's Background")
window.configure(bg="#FFC0CB")
window.geometry("3000x1000")

text = tk.Label(
    window,
    text="Ellaine's Background",
    font=("Courier New", 30),
    fg="#000000",
    bg="#FFC0CB",
)
text.pack()

frame = tk.Frame(window)
frame.pack()

# name_and_age
user_info_frame = tk.LabelFrame(
    frame,
    text="Ellaine's Information",
    font=("Courier New", 14),
    fg="#000000",
    bg="#FFC0CB",
)
user_info_frame.grid(row=0, column=0, sticky="news", pady=15, padx=15)

first_name_label = tk.Label(
    user_info_frame, text="First Name", font=("Courier New", 12), fg="#000000", bg="#FFC0CB"
)
first_name_label.grid(row=0, column=0)
middle_name_label = tk.Label(
    user_info_frame,
    text="Middle Name",
    font=("Courier New", 12),
    fg="#000000",
    bg="#FFC0CB",
)
middle_name_label.grid(row=0, column=1)
last_name_label = tk.Label(
    user_info_frame, text="Last Name", font=("Courier New", 12), fg="#000000", bg="#FFC0CB"
)
last_name_label.grid(row=0, column=2)

first_name_entry = tk.Entry(user_info_frame, bg="#FFB6C1", fg="#000000")
middle_name_entry = tk.Entry(user_info_frame, bg="#FFB6C1", fg="#000000")
last_name_entry = tk.Entry(user_info_frame, bg="#FFB6C1", fg="#000000")
first_name_entry.grid(row=1, column=0)
middle_name_entry.grid(row=1, column=1)
last_name_entry.grid(row=1, column=2)

age_label = tk.Label(
    user_info_frame, text="Age", font=("Courier New", 12), fg="#000000", bg="#FFC0CB"
)
age_spinbox = tk.Spinbox(user_info_frame, from_=1, to=100, bg="#FFB6C1", fg="#000000")
age_label.grid(row=2, column=1)
age_spinbox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# address
address_frame = tk.LabelFrame(
    frame, text="Ellaine's Address", font=("Courier New", 14), fg="#000000", bg="#FFC0CB"
)
address_frame.grid(row=1, column=0, sticky="news", pady=15, padx=15)

barangay_label = tk.Label(
    address_frame, text="Barangay", font=("Courier New", 12), fg="#000000", bg="#FFC0CB"
)
barangay_label.grid(row=1, column=0)
municipality_label = tk.Label(
    address_frame, text="Municipality", font=("Courier New", 12), fg="#000000", bg="#FFC0CB"
)
municipality_label.grid(row=1, column=1)
province_label = tk.Label(
    address_frame, text="Province", font=("Courier New", 12), fg="#000000", bg="#FFC0CB"
)
province_label.grid(row=1, column=2)
region_label = tk.Label(
    address_frame, text="Region", font=("Courier New", 12), fg="#000000", bg="#FFC0CB"
)
region_label.grid(row=3, column=0)
country_label = tk.Label(
    address_frame, text="Country", font=("Courier New", 12), fg="#000000", bg="#FFC0CB"
)
country_label.grid(row=3, column=1)

barangay_entry = tk.Entry(address_frame, bg="#FFB6C1", fg="#000000")
municipality_entry = tk.Entry(address_frame, bg="#FFB6C1", fg="#000000")
province_entry = tk.Entry(address_frame, bg="#FFB6C1", fg="#000000")
region_entry = tk.Entry(address_frame, bg="#FFB6C1", fg="#000000")
country_entry = tk.Entry(address_frame, bg="#FFB6C1", fg="#000000")

barangay_entry.grid(row=2, column=0)
municipality_entry.grid(row=2, column=1)
province_entry.grid(row=2, column=2)
region_entry.grid(row=4, column=0)
country_entry.grid(row=4, column=1)

for widget in address_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# agreement
agreement_frame = tk.LabelFrame(
    frame, text="Agreement", font=("Courier New", 14), fg="#000000", bg="#FFC0CB"
)
agreement_frame.grid(row=2, column=0, sticky="news", pady=15, padx=10)

agreement_var = tk.StringVar(value="Disagree")
agreement_check = tk.Checkbutton(
    agreement_frame,
    text="I agree to submit my information.",
    font=("Courier New", 12),
    variable=agreement_var,
    onvalue="Agree",
    offvalue="Disagree",
    bg="#FFC0CB",
    fg="#000000",
)
agreement_check.grid(row=1, column=0)

disagree_pass_check = tk.Checkbutton(
    agreement_frame,
    text="I disagree to submit my information.",
    font=("Courier New", 12),
    variable=agreement_var,
    onvalue="Disagree",
    offvalue="Agree",
    bg="#FFC0CB",
    fg="#000000",
)
disagree_pass_check.grid(row=2, column=0)

for widget in agreement_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# submit_button
submit_button = tk.Button(
    frame,
    text="Submit",
    font=("Courier New", 14),
    command=submit_data,
    bg="#FF1493",
    fg="#000000",
)
submit_button.grid(row=3, column=0, sticky="news", pady=15, padx=10)

window.mainloop()
