import firebase_admin                      # Import firebase_admin for Firebase functionalities
from firebase_admin import credentials, db  # Import credentials and database functionalities from firebase_admin
from datetime import datetime              # Import datetime for time tracking
from tkinter import messagebox             # Import messagebox to show pop-up messages

# Initialize Firebase Admin SDK with a service account JSON file and connect to the database URL
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://book-manager-c42ff-default-rtdb.firebaseio.com/"})

# Create references to the "students" and "library" sections of the Firebase database
ref = db.reference("students") 
ref2 = db.reference("library")  

# Function to handle lending of a book
def lend(_name, _roll, _branch, _phno, _bname):
    bookdict = {}  # Dictionary to store book name and lending time
    now = datetime.now()  # Get the current date and time
    current_time = now.strftime("%y/%m/%d %H:%M:%S")  # Format the time to a readable string
    print(current_time)  # Print the current time for debugging purposes
    bookdict.update({_bname: current_time})  # Add book name and lending time to the dictionary

    # Create a data dictionary for the student, containing their details and the borrowed book
    data = {
        "name": _name,
        "roll number": _roll,
        "branch": _branch,
        "mobile number": _phno,
        "books": bookdict
    }

    # Store the student data in the Firebase database under their roll number
    ref.child(_roll).set(data)

    # Remove the book from the library's available books in the Firebase database after it has been lent out
    ref2.child(_bname).delete()

# Function to handle returning (borrowing) of a book
def borrow(roll, bname):
    now = datetime.now()  # Get the current date and time
    current_time = now.strftime("%y/%m/%d %H:%M:%S")  # Format the time to a readable string

    # Update the library database by adding the returned book along with the current time
    ref2.update({bname: current_time})

    # Remove the returned book from the student's borrowed books in the Firebase database
    ref.child(roll).child("books").child(bname).delete()

# Function to search for a book's availability in the library
def lib_search(input):
    new_dict = ref2.get()  # Get all the available books from the library reference
    sum = 0  # Variable to track if the book is found

    # Loop through the available books and check if the searched book matches any in the library
    for i in new_dict:
        if input == i:  # If the input matches a book name
            sum += 1
        else:
            pass

    # If the book is found in the library, show a pop-up message confirming its availability
    if sum > 0:
        messagebox.showinfo("information", "PRESENT" + "\n" + "\n" +
                            "Your required book exists in our library.")
    # If the book is not found, show an error pop-up indicating its absence
    else:
        messagebox.showerror("information", "ABSENT" + "\n" + "\n" +
                             "Your required book doesn't exist in our library.")
