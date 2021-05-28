from tkinter import *
import sqlite3
root=Tk()
root.title("Database address book")
root.iconbitmap('contact1.ico')

#Database
#Create a database or connectr to one
conn=sqlite3.connect("address_book.db")

#create cursor
#cursor class is an instance using which you can evoke
# methods that execute SQlite, fetch data from the result sets of the queries

c=conn.cursor()
'''
#create Table
c.execute(""" CREATE TABLE addresses(
       first_name,
       last_name,
       address text,
       city text,
       state text,
       zipcode integer
)        
""")
print("Table created successfully")
'''
#create a submit button for data base
def submit():
    #clear the text boxes
    first_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)


#Create text boxes
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20)

last_name = Entry(root, width=30)
last_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

first_name_label = Label(root, text="First Name")
first_name_label.grid(row=0,column=0)

last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=1,column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2,column=0)

city_label = Label(root, text="City")
city_label.grid(row=3,column=0)

state_label = Label(root, text="State")
state_label.grid(row=4,column=0)


zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

#create submit button
submit_btn = Button(root, text="Add records", command=submit)
submit_btn.grid(row=6, column=0, pady=10, padx=10, ipadx=100)


def query():
    #create a database or connect to one
    conn = sqlite3.connect('adress_book.db')

    #create cursor
    c = conn.cursor()

    #query of the database
    c.execute("SELECT *, old FROM addresses")

    records = c.fetchall()
    print(records)

    # loop through th results
    print_records=''
    for record in records:
        print_record += str(record + "\n")
    query_label = Label(root, text=print_record)
    query_label,grid(row=8, column=0, columnspan=2)


# commit change
conn.commit()

# close connection
conn.close()
mainloop()