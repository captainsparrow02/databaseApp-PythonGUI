#!/usr/bin/env python3

from tkinter import *
import sqlite3

# Creating tkinter root window
root = Tk()

# Giving a title and default size to our root window.
root.title("Database Entry App")
root.geometry("400x400")

# Connecting to our database.
conn = sqlite3.connect('address_book.db') #passing the name of the database that needs to connected.

#Create a cursor which will help us interract with our database.
c = conn.cursor()

# Commit changes made in database.
conn.commit()


#Creating a submit function
def submit():
    ''' This function enters a new record into the database. '''

    # Connecting to our database.
    conn = sqlite3.connect('address_book.db')
    # Create a cursor which will help us interract with our database.
    c = conn.cursor()

    # Inserting new values in our database.
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # Commit changes made in database.
    conn.commit()
    # Closing connection.
    conn.close()

    #Clearing all the fields.
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Making the delete function.
def delete():
    ''' This function delete's a record present in the database. '''

    # Connecting to our database.
    conn = sqlite3.connect('address_book.db')
    # Create a cursor which will help us interract with our database.
    c = conn.cursor()

    # Deleting all the data for the entered id.
    c.execute("DELETE from addresses WHERE oid= "+select_entry.get())

    # Commit changes made in database.
    conn.commit()
    # Closing connection.
    conn.close()


#Making Update Button
def update():
    ''' This function updates the data/values of a particular record. '''

    # Connecting to our database.
    conn = sqlite3.connect('address_book.db')
    # Create a cursor which will help us interract with our database.
    c = conn.cursor()

    # Recieving the ID for the record which needs to be updated.
    record_id = select_entry.get()

    # Updating the values of the selected record.
    c.execute("""
        UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = oid""",
              {
                 'first': f_name_editor.get(),
                 'last': l_name_editor.get(),
                 'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),
                  'oid': record_id
              })

    # Committing the changes to the database.
    conn.commit()
    # Closing the connection to the database.
    conn.close()

    # Closing the editor window.
    editor.destroy()


#Editing Record
def edit():
    ''' This function creates a new window which renders the whole record of the selected record which needs to be updated.'''

    global editor

    # Creating a new window and giving it a title.
    editor = Tk()
    editor.title("Update Records Window")

    # Connecting to the database.
    conn = sqlite3.connect('address_book.db')
    # Create a cursor which will help us interract with our database.
    c = conn.cursor()

    # Recording the ID of the record which needs to be updated.
    record_id = select_entry.get()

    # Fetching all the data associated with the record.
    c.execute("SELECT * FROM addresses WHERE oid="+record_id)
    records = c.fetchall()

    #Making Entry fields global
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Creating Entry fields
    f_name_editor = Entry(editor, text="First Name")
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))  # pady is given a tupple (upper, lower)
    l_name_editor = Entry(editor, text="Last Name")
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, text="Address")
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, text="City")
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, text="State")
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, text="Zipcode")
    zipcode_editor.grid(row=5, column=1, padx=20)

    # Creating Labels for entry fields.
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0,pady=(10,0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    # Iterating through the fetched record and rendering the fetched data in the respective fields.
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    update_btn = Button(editor, text="Update", command=update)
    update_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=130)

    # Committing changes in the database.
    conn.commit()
    # Closing the database.
    conn.close()

# Making Query function.
def query():
    '''This functions renders the full name and ID of each record in the database.'''

    # Connecting to our database.
    conn = sqlite3.connect('address_book.db')
    # Create a cursor which will help us interract with our database.
    c = conn.cursor()

    # Fetching all the records.
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    #Looping through records
    print_record=''
    for record in records:
        print_record+= record[0]+' '+record[1]+' '+str(record[6])+'\n'

    query_label = Label(root, text = print_record)
    query_label.grid(row=11, column =0 , columnspan =2, padx=10, pady=10)

    # Committing changes in the database.
    conn.commit()
    # Closing the database.
    conn.close()



# Creating Entry fields
f_name = Entry(root, text="First Name")
f_name.grid(row=0, column=1, padx =20, pady=(10,0)) #pady is given a tupple (upper, lower)

l_name = Entry(root, text="Last Name")
l_name.grid(row=1, column=1, padx =20)

address = Entry(root, text="Address")
address.grid(row=2, column=1, padx =20)

city = Entry(root, text="City")
city.grid(row=3, column=1, padx =20)

state = Entry(root, text="State")
state.grid(row=4, column=1, padx =20)

zipcode = Entry(root, text="Zipcode")
zipcode.grid(row=5, column=1, padx =20)

select_entry = Entry(root, text="Select Record")
select_entry.grid(row=8, column=1, padx =20, pady=10)

# Creating Labels for entry fields.

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0,pady=(10,0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

select_entry_label = Label(root, text="Select ID")
select_entry_label.grid(row=8, column=0, pady=10)

# Creating a submit button.

btn_submit = Button(root, text='Enter data in Database', command= submit)
btn_submit.grid(row = 6, column =0, columnspan = 2, padx=10, pady=10, ipadx=100)

# Create a query button.

btn_query = Button(root, text="Show data", command = query)
btn_query.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=130)

# Creating delete button.

delete_btn = Button(root, text="Delete Record", command = delete)
delete_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=121)

# Creating Update button.

update_btn = Button(root, text="Update Record", command = edit)
update_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=119)

# Closing connection.
conn.close()

# Running the root window.
root.mainloop()
