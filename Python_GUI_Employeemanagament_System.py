import tkinter as tk


from tkinter import messagebox, END

def login():

    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "0000":

        login_screen.destroy()
        main_menu_screen()

    else:

        messagebox.showerror("Error", "Username or password is incorrect!!")
        username_entry.delete(0,tk.END)
        password_entry.delete(0, tk.END)

def add_worker():
    name = name_entry.get()
    number = number_entry.get()
    salary = salary_entry.get()

    if name != "" and number != "" and salary != "":
        with open("workers.txt", "a") as file:
            file.write(f"{name}, {number}, {salary}\n")
        messagebox.showinfo("Successful", "Employee added successfully")
        name_entry.delete(0,tk.END)
        number_entry.delete(0, tk.END)
        salary_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter all information!!")
        name_entry.delete(0,tk.END)
        number_entry.delete(0, tk.END)
        salary_entry.delete(0, tk.END)

def list_workers():
    with open("workers.txt", "r") as f:
        workers = f.readlines()

    list_screen = tk.Toplevel(main_menu_screen)
    list_screen.title("ALL EMPLOYEE")
    for worker in workers:
        tk.Label(list_screen, text=worker.strip()).pack()


def delete_worker():
    name = delete_entry.get()

    if name != "":
        with open("workers.txt", "r") as f:
            lines = f.readlines()

        found = False
        with open("workers.txt", "w") as f:
            for line in lines:
                if not line.startswith(name + ","):
                    f.write(line)
                else:
                    found = True
                    messagebox.showinfo("Information", "Employee Deleted Successfully!",icon="info")

        if not found:
            messagebox.showerror("Error", "Employee not found!",icon="error")

    else:
        messagebox.showerror("Error", "Please enter a name!", icon="error")

    delete_entry.delete(0, tk.END)


def main_menu_screen():
    global main_menu_screen
    main_menu_screen = tk.Tk()
    main_menu_screen.geometry("300x250")
    main_menu_screen.title("Employee Management Panel")


    tk.Label(main_menu_screen, text="****Welcome****",font=('times new roman', 20, "bold")).pack()
    tk.Button(main_menu_screen, text="ADD EMPLOYEE", command=add_worker_screen,font=('times new roman', 18, "bold")).pack(pady=10)
    tk.Button(main_menu_screen, text="LIST EMPLOYEE", command=list_workers,font=('times new roman', 18, "bold")).pack(pady=10)
    tk.Button(main_menu_screen, text="DELETE EMPLOYEE", command=delete_worker_screen,font=('times new roman', 18, "bold")).pack(pady=10)


def add_worker_screen():
    global add_worker_screen
    add_worker_screen = tk.Toplevel(main_menu_screen)
    add_worker_screen.title("ADD EMPLOYEE")
    add_worker_screen.geometry("300x250")

    global name_entry, number_entry, salary_entry
    tk.Label(add_worker_screen, text="Name-Surname").pack()
    name_entry = tk.Entry(add_worker_screen)
    name_entry.configure(foreground="white", font=('times new roman', 15, "bold"))
    name_entry.pack()


    tk.Label(add_worker_screen, text="Number").pack()
    number_entry = tk.Entry(add_worker_screen)
    number_entry.configure(foreground="white", font=('times new roman', 15, "bold"))
    number_entry.pack()


    tk.Label(add_worker_screen, text="Salary").pack()
    salary_entry = tk.Entry(add_worker_screen)
    salary_entry.configure(foreground="white",font=('times new roman', 15,"bold"))
    salary_entry.pack()


    tk.Button(add_worker_screen, text="ADD EMPLOYEE", command=add_worker,font=('times new roman', 18,"bold")).pack(pady=10)



def delete_worker_screen():
    global delete_worker_screen
    delete_worker_screen = tk.Toplevel(main_menu_screen)
    delete_worker_screen.title("DELETE EMPLOYEE")
    delete_worker_screen.geometry("300x250")
    global delete_entry
    tk.Label(delete_worker_screen, text="Name").pack()
    delete_entry = tk.Entry(delete_worker_screen)
    delete_entry.configure(foreground="white", font=('times new roman', 18, "bold"))
    delete_entry.pack()

    tk.Button(delete_worker_screen, text="DELETE EMPLOYEE", command=delete_worker,font=('times new roman', 18, "bold")).pack(pady=10)
def login_screen():
    global login_screen
    login_screen = tk.Tk()
    login_screen.geometry("300x270")
    login_screen.title("Login Screen")
    tk.Label(login_screen, text="Please Login",font=('times new roman', 20,"bold")).pack(pady=10)


    global username_entry, password_entry

    tk.Label(login_screen, text="Username",font=('times new roman', 18,"bold")).pack(pady=5)
    username_entry = tk.Entry(login_screen)
    username_entry.configure(foreground="white",font=('times new roman', 18,"bold"))
    username_entry.pack()

    tk.Label(login_screen, text="Password",font=('times new roman', 18,"bold")).pack(pady=5)
    password_entry = tk.Entry(login_screen, show="*")
    password_entry.configure(foreground="white", font=('times new roman', 18, "bold"))
    password_entry.pack()

    tk.Label(login_screen, text="").pack()
    tk.Button(login_screen, text="LOGIN", width=10, height=1, command=login,font=('times new roman', 20, "bold")).pack(pady=10)

    login_screen.mainloop()

login_screen()