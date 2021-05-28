def dataUpdate(id, StdID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StdID=?, Firstname=?, DoB=?,Age=?,Address=?Mobile=?,WHERE id=?",
                (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, id))
    con.commit()
    con.close()


studentData()