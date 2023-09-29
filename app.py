from tkinter import *
import sqlite3

root = Tk()
root.title("Registration Window")
conn = sqlite3.connect('my_database.db')
root.geometry("400x300")
cursor = conn.cursor()

'''cursor.execute("""
    CREATE TABLE users (
        f_name  text,
        s_name text,
        city text,
        country text,
        u_number integer)
    """)
'''


# Button Functions

def submit():
    conn = sqlite3.connect('my_database.db')
    insert = conn.cursor()

    # insert your data
    insert.execute("INSERT INTO users VALUES(:f_name, :s_name,:city,:country,:u_number",
                   {'f_name': f_name.get(), 's_name': s_name.get(), 'city': city.get(), 'country': country.get(),
                    'u_number': u_number.get()})
    conn.commit()
    conn.close()
    # clear the screen entries
    f_name.delete(0, END)
    s_name.delete(0, END)
    city.delete(0, END)
    country.delete(0, END)
    u_number.delete(0, END)


def display():
    users = Tk()
    users.title("Records")
    users.geometry("400x400")
    conn = sqlite3.connect('my_database.db')
    show = conn.cursor()
    show.execute("SELECT *, oid FROM users")
    data = show.fetchall()
    records = ''
    for record in data:
        records += str(record[0]) + ' ' + str(record[1]) + 'Tel:' + record[5] + "/n"

    u_title = Label(users, text="Current Users")
    u_title.grid(row=1, column=2)

    info = Label(users, text='yoongi')
    info.grid(row=2, column=2, columnspan=3)

    conn.commit()
    conn.close()
    users.mainloop()


def delete():
    conn = sqlite3.connect('my_database.db')
    delete = conn.cursor()

    conn.commit()
    conn.close()


def update():
    update_win = Tk()
    update_win.title("Update User")
    update_win.geometry("400x300")
    conn = sqlite3.connect('my_database.db')

    # Entries

    f_name_upt = Entry(update_win, width=30)
    s_name_upt = Entry(update_win, width=30)
    city_upt = Entry(update_win, width=30)
    country_upt = Entry(update_win, width=30)
    u_number_upt = Entry(update_win, width=30)

    f_name_upt.grid(row=1, column=1)
    s_name_upt.grid(row=2, column=1)
    city_upt.grid(row=3, column=1)
    country_upt.grid(row=4, column=1)
    u_number_upt.grid(row=5, column=1)

    # Labels

    f_name_lb_upt = Label(update_win, text="First Name:")
    s_name_lb_upt = Label(update_win, text="Second Name:")
    city_lb_upt = Label(update_win, text="Your City:")
    country_lb_upt = Label(update_win, text="Your Country:")
    u_number_lb_upt = Label(update_win, text="Mobile No.:")

    f_name_lb_upt.grid(row=1, column=0)
    s_name_lb_upt.grid(row=2, column=0)
    city_lb_upt.grid(row=3, column=0)
    country_lb_upt.grid(row=4, column=0)
    u_number_lb_upt.grid(row=5, column=0)

    # Buttons
    submit_btn_upt = Button(update_win, text="Submit", command=submit)
    submit_btn_upt.grid(row=6, column=0, columnspan=2, ipadx=10)

    conn.commit()
    conn.close()

    # clear the screeen
    f_name_upt.delete(0, END)
    s_name_upt.delete(0, END)
    city_upt.delete(0, END)
    country_upt.delete(0, END)
    u_number_upt.delete(0, END)
    update_win.mainloop()
    pass


def clear():
    conn = sqlite3.connect('my_database.db')

    clear = conn.cursor()

    clear.execute("""DELETE FROM users""")
    conn.commit()
    conn.close()
    pass


# end functions


# Entries

f_name = Entry(root, width=30)
s_name = Entry(root, width=30)
city = Entry(root, width=30)
country = Entry(root, width=30)
u_number = Entry(root, width=30)

f_name.grid(row=1, column=1)
s_name.grid(row=2, column=1)
city.grid(row=3, column=1)
country.grid(row=4, column=1)
u_number.grid(row=5, column=1)

# Labels

f_name_lb = Label(root, text="First Name:")
s_name_lb = Label(root, text="Second Name:")
city_lb = Label(root, text="Your City:")
country_lb = Label(root, text="Your Country:")
u_number_lb = Label(root, text="Mobile No.:")

f_name_lb.grid(row=1, column=0)
s_name_lb.grid(row=2, column=0)
city_lb.grid(row=3, column=0)
country_lb.grid(row=4, column=0)
u_number_lb.grid(row=5, column=0)

# Buttons

# submit
submit_btn = Button(root, text="Submit", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, ipadx=10)

# show data
show_data = Button(root, text="Show Data", command=display)
show_data.grid(row=7, column=0, columnspan=2, ipadx=10)

"""
# clear database 
clear_btn  = Button(root, text="Clear Data", command=clear)
clear_btn.grid(row=8, column=0, columnspan=2, ipadx=10)

# delete user 
delete_btn  = Button(root, text="Delete Data", command=delete)
delete_btn.grid(row=9, column=0, columnspan=2, ipadx=10)

# update user 
update_btn = Button(root, text="Update Data", command=update)
update_btn.grid(row=10, column=0, columnspan=2, ipadx=10)
"""

conn.commit()
conn.close()

root.mainloop()
