from tkinter import messagebox, Toplevel, Label, Entry, Button
import psycopg2
import adminusercreatepage
# from ADMIN.adminusercreatepage import adminuserpage
import inventoryfeed   
def openadminpage():
   def logout_clicked():
        new_window.destroy()
        messagebox.showinfo("Logout", "You have been logged out.")
   new_window=Toplevel()
   # new_window.geometry("200X200")
   new_window.title('ADMIN PAGE')  
   ENGGACCOUNT=Button(new_window,text="ENGINEER ACCOUNT")
   ENGGACCOUNT.pack()
   
   USERACCOUNT=Button(new_window,text="USER ACCOUNT",command=adminusercreatepage.adminuserpage)
   USERACCOUNT.pack()
   
   Inventory=Button(new_window,text="INVENTORY",command=inventoryfeed.inventorywindow)
   Inventory.pack()
   
   logout_button = Button(new_window, text="Logout", command=lambda:logout_clicked())
   logout_button.pack()
   

def login_clicked(username_entry, password_entry):
    # Get the entered username and password
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    try:
        conn = psycopg2.connect(database="Asset_management", user="postgres", password="Lob@89763", host="localhost", port="5432")
        cursor = conn.cursor()
        query = f"SELECT * FROM admin WHERE username = '{entered_username}' AND password= '{entered_password}'"
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            messagebox.showinfo("Login Successful", "Admin login successful.")
            openadminpage()

            
            # Add code to open the next page or perform further actions
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

        conn.close()
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
def admin_button_clicked():
    login_window = Toplevel()
    login_window.title("Admin Login")

    label_username = Label(login_window, text="Username:")
    label_username.pack()
    username_entry = Entry(login_window)
    username_entry.pack()

    label_password = Label(login_window, text="Password:")
    label_password.pack()
    password_entry = Entry(login_window, show="*")
    password_entry.pack()

    login_button = Button(login_window, text="Login", command=lambda: login_clicked(username_entry, password_entry))
    login_button.pack()
    