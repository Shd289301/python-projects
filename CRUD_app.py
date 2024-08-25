import mysql.connector
from tkinter import*
from tkinter import messagebox

window = Tk()
window.geometry('600x270')
window.title('Employee Crud App')
empID = Label(window, text='Emp ID', font=('serif', 12))
empID.place(x=20, y=30)
empName = Label(window, text='Emp Name', font=('serif', 12))
empName.place(x=20, y=60)
empDept = Label(window, text='Emp Name', font=('serif', 12))
empDept.place(x=20, y=90)
enterID = Entry(window)
enterID.place(x=170, y=30)
enterName = Entry(window)
enterName.place(x=170, y=60)
enterDept = Entry(window)
enterDept.place(x=170, y=90)
showData = Listbox(window)
showData.place(x=330, y=30)


def ShowData():
    myDB = mysql.connector.connect(host='localhost', user='root', passwd='Sib_Sql@x64!', database='Employee')
    myCur =myDB.cursor()
    myCur.execute("select * from EmpDetail")
    rows = myCur.fetchall()
    showData.delete(0, showData.size())
    for row in rows:
        add_value = str(row[0])+''+row[1]+''+row[2]
        showData.insert(showData.size()+1, add_value)
    myDB.close()


def ResetFields():
    enterID.delete(0, "end")
    enterName.delete(0, "end")
    enterDept.delete(0, "end")


def InsertData():
    id = enterID.get()
    name = enterName.get()
    dept = enterDept.get()
    if id == "" or name == "" or dept == "":
        messagebox.showwarning("cannot insert", "all fields are required!")
    else:
        myDB = mysql.connector.connect(host='localhost', user='root', passwd='Sib_Sql@x64!', database='Employee')
        myCur = myDB.cursor()
        myCur.execute("insert into EmpDetail values("+id+", "+name+", "+dept+")")
        myDB.commit()
        ShowData()
        enterID.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")
        messagebox.showinfo("insert status", "data inserted successfully")
        myDB.close()


def UpdateData():
    id = enterID.get()
    name = enterName.get()
    dept = enterDept.get()
    if id == "" or name == "" or dept == "":
        messagebox.showwarning("cannot insert", "required all fields!")
    else:
        myDB = mysql.connector.connect(host='localhost', user='root', passwd='Sib_Sql@x64!', database='Employee')
        myCur = myDB.cursor()
        myCur.execute("update EmpDetail set empname = "+name+", empdept = "+dept+" where empID = "+id+"")
        myDB.commit()
        ShowData()
        enterID.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")
        messagebox.showinfo("update status", "data updated successfully")
        myDB.close()


def GetData():
    if enterID.get() == "":
        messagebox.showwarning("fetch status", "insert empID!")
    else:
        myDB = mysql.connector.connect(host='localhost', user='root', passwd='Sib_Sql@x64!', database='Employee')
        myCur = myDB.cursor()
        myCur.execute("select * from EmpDetail where empID = "+enterID.get()+"")
        rows = myCur.fetchall()
        for row in rows:
            enterName.insert(0, row[1])
            enterDept.insert(0, row[2])
        myDB.close()


def DeleteData():
    if enterID.get() == "":
        messagebox.showwarning("delete status", "insert empID!")
    else:
        myDB = mysql.connector.connect(host='localhost', user='root', passwd='Sib_Sql@x64!', database='Employee')
        myCur = myDB.cursor()
        myCur.execute("delete from EmpDetail where empID = "+enterID.get()+"")
        myDB.commit()
        ShowData()
        enterID.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")
        myDB.close()


insertBtn = Button(window, text='Insert', font=('Sans', 16), bg='white', command=InsertData)
insertBtn.place(x=20, y=160)
updateBtn = Button(window, text='Update', font=('Sans', 16), bg='white', command=UpdateData)
updateBtn.place(x=97, y=160)
deleteBtn = Button(window, text='Delete', font=('Sans', 16), bg='white', command=DeleteData)
deleteBtn.place(x=190, y=160)
resetBtn = Button(window, text='Reset', font=('Sans', 16), bg='white', command=ResetFields)
resetBtn.place(x=20, y=210)
ShowData()
window.mainloop()






