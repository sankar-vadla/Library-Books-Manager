from tkinter import *               # Import all modules from tkinter library for GUI
from PIL import ImageTk, Image       # Import ImageTk and Image from PIL for handling images
from tkinter import messagebox       # Import messagebox from tkinter to display message boxes
import firebase                      # Import firebase for handling backend tasks like borrowing and lending

# Create the root window (main login page)
root = Tk()                          
root.title("LOGIN PAGE")             
root.geometry("850x478")            

# Load and display a background image for the login window
img = ImageTk.PhotoImage(Image.open("login.jpg"))
img_label = Label(image=img)
img_label.place(x=0, y=0)

# Create input fields for username and password
e1 = Entry(root, width=40)           
e1.grid(column=1, row=0, padx=10, pady=10)  
e1.place(x=470, y=150, height=20)    
e2 = Entry(root, width=40)           
e2.grid(column=1, row=1, padx=10, pady=10)
e2.place(x=470, y=210, height=20)

# Labels for username and password fields
name = Label(root, text="Username", bg="#001133", fg="#85e0e0")  
name.grid(column=0, row=0, padx=10, pady=10)
name.place(x=380, y=150)
pas = Label(root, text="Password", bg="#001133", fg="#85e0e0")   
pas.grid(column=0, row=1, padx=10, pady=10)
pas.place(x=380, y=210)

# Function to handle borrowing and lending operations based on user's selection
def do(det):
    if det == 1:   # If borrowing
        answer = messagebox.askyesno("Confirmation Page", "name                   : " + ee1.get() +
                                     "\n" + "roll number        : " + ee2.get() + "\n" +
                                     "branch                : " + var.get() +
                                     "\n" + "mobile number  : " + ee3.get() +
                                     "\n" + "book name         : " + ee4.get() + "\n" + "\n" +
                                     "Are provided details correct?" + "\n")
        if answer:  # If user confirms details
            firebase.borrow(ee2.get(), ee4.get())  # Call firebase's borrow method
            messagebox.showinfo("status", "Details updated successfully")
            bone.destroy()  # Close the form window after success

    else:   # If lending
        answer = messagebox.askyesno("Confirmation Page", "name                   : " + ee1.get() +
                                     "\n" + "roll number        : " + ee2.get() + "\n" +
                                     "branch                : " + var.get() +
                                     "\n" + "mobile number  : " + ee3.get() +
                                     "\n" + "book name         : " + ee4.get() + "\n" + "\n" +
                                     "Are provided details correct?" + "\n")
        if answer:  # If user confirms details
            firebase.lend(ee1.get(), ee2.get(), var.get(), ee3.get(), ee4.get())  # Call firebase's lend method
            messagebox.showinfo("status", "Details updated successfully")
            bone.destroy()  # Close the form window after success

# Function to close the given window
def close(window):
    window.destroy()

# Function to open the form window for lending/borrowing details submission
def openform(value):
    global bone
    bone = Toplevel()  # Create a new top-level window (form)
    bone.title("Details Submission")
    bone.configure(bg="#666633")
    bone.geometry("600x500")
    
    # Labels and Entry fields to capture details like name, roll number, branch, phone, and book name
    head = Label(bone, text="STUDENT DETAILS", background="#666633", foreground="white")
    head.grid(pady=20, padx=250)
    nam = Label(bone, text="Name", foreground="black", background="#666633")
    nam.place(x=200, y=70)
    roll = Label(bone, text="Roll no.", foreground="black", background="#666633")
    roll.place(x=200, y=110)
    global ee1, ee2, ee3, ee4, var
    ee1 = Entry(bone, width=30)  # Name field
    ee1.place(x=270, y=70)
    ee2 = Entry(bone, width=30)  # Roll no. field
    ee2.place(x=270, y=110)
    bran = Label(bone, text="Branch", foreground="black", background="#666633")
    bran.place(x=200, y=150)
    var = StringVar()  # Drop-down menu for selecting branch
    drop = OptionMenu(bone, var, "computer engineering", "electronics and communication engineering",
                      "electrical engineering", "mechanical engineering", "civil engineering",
                      "industrial internet of things")
    drop.place(x=270, y=150)
    phno = Label(bone, text="Phone no.", foreground="black", background="#666633")
    phno.place(x=200, y=190)
    ee3 = Entry(bone, width=30)  # Phone number field
    ee3.place(x=270, y=190)
    b_nam = Label(bone, text="Book name", foreground="black", background="#666633")
    b_nam.place(x=200, y=230)
    ee4 = Entry(bone, width=30)  # Book name field
    ee4.place(x=270, y=230)
    
    # Submit and Close buttons
    c1 = Button(bone, text="Close", bg="#2e2e1f", fg="white", command=lambda: close(bone))
    c1.place(x=210, y=270)
    s1 = Button(bone, text="Submit", bg="#2e2e1f", fg="white", command=lambda: do(value))
    s1.place(x=310, y=270)

# Function to search book availability using firebase
def search(inp):
    firebase.lib_search(inp)

# Function to open the home page after login
def newwindow():
    global naya
    naya = Toplevel()  # Create a new top-level window for home page
    naya.title("HOME PAGE")
    naya.geometry("1000x495")
    
    # Load and display the background image for the home page
    global img2
    img2 = ImageTk.PhotoImage(Image.open("home.jpg"))
    i_label = Label(naya, image=img2)
    i_label.place(x=0, y=0)
    
    # Create buttons for lending, borrowing, and book search
    bor = Button(naya, text="Lend", command=lambda: openform(0))  # Open form for lending
    bor.place(x=250, y=290)
    subm = Button(naya, text="Borrow", command=lambda: openform(1))  # Open form for borrowing
    subm.place(x=250, y=390)
    sea = Button(naya, text="Search Availability", command=lambda: search(ent.get()))  # Book search
    sea.place(x=150, y=190)
    
    global ent
    ent = Entry(naya, width=30)  # Entry field for book search
    ent.place(x=285, y=190)

# Function to show the entered password (for testing purposes)
def show():
    word = e2.get()  
    print(word)      

# Button to show the entered password
sho = Button(root, text="show", command=show, fg="white", bg="black")
sho.place(x=730, y=210)

# Function to handle login submission
def submitted():
    str1 = e1.get()  
    str2 = e2.get()  
    if str1 == "00" and str2 == "00":  # Check for valid credentials
        newwindow()  # Open home page if credentials are valid
        root.withdraw()  # Hide the login page (root window)
    else:
        messagebox.showerror("Error", "Entered wrong username or password")  # Display error message

# Submit button for login
sub = Button(root, text="Submit", command=submitted, fg="white", bg="black")
sub.place(x=500, y=300)

# Run the main event loop
root.mainloop()
