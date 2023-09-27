import sqlite3
#con=sqlite3.connect('employees.db')
class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXITS employees(
        id integer Primary Key,
        name text,
        age text,
        doj text,
        email text,
        gender text,
        contact text,
        address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

#Insert Function
def insert(self,name,age,doj,email,gender,contact,address):
    self.cur.execute("insert into employees values(NULL,?,?,?,?,?,?,?)",
                     (name, age, doj, email, gender, contact, address))
    self.con.commit()

o=Database("Employee.db")
o.insert("Ran","25","12-10-2020","ram@gmail.com","Male","985786985","Chery Road, Salem")