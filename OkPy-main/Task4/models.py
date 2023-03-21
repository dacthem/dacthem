class Student:

    def __init__(self, id, code, firstName, lastName, dob, math, physics, chemistry):
        self.id = id
        self.code = code
        self.fistName = firstName
        self.lastName = lastName
        self.dob = dob
        self.math = math
        self.physics = physics
        self.chemistry = chemistry

    def getStudentInfor(self):
        print('Id: ' + self.id)
        print('Name: ' + self.fistName + " " + self.lastName)
        print('Dob: ' + self.dob)
        print('Math: ' + str(self.math))
        print('Physics: ' + str(self.physics))
        print('Chemistry: ' + str(self.chemistry))
        print('-------------')


def createTableStudents(mydb, cursor):
    mySql_Create_Table_Query = """CREATE TABLE IF NOT EXISTS Students ( 
                                 id int(11) NOT NULL AUTO_INCREMENT,
                                 code varchar(250) NULL ,
                                 first_name varchar(250) NULL,
                                 last_name varchar(250) NULL,
                                 dob varchar(250) NULL,
                                 math float NULL,
                                 physics float NULL,
                                 chemistry float NULL,
                                 PRIMARY KEY (id)) """
    cursor.execute(mySql_Create_Table_Query)
    mydb.commit()
    print("Students created successfully ")


class StudentRepo:

    @staticmethod
    def insert(mydb, cursor, data):
        sql = "INSERT INTO students (code, first_name, last_name, dob, math, physics, chemistry) VALUES (%s, %s, %s, %s,%s,%s,%s)"
        cursor.execute(sql, data)
        mydb.commit()
        print(cursor.rowcount, "student inserted.")

    @staticmethod
    def find_all(mydb, cursor):
        cursor.execute("SELECT * FROM students")
        results = cursor.fetchall()
        return results if len(results) else []

    @staticmethod
    def update(mydb, cursor, id, data):
        sql = "UPDATE students SET code=%s, first_name=%s, last_name=%s, dob=%s, math=%s, physics=%s, chemistry=%s WHERE id=%s"
        cursor.execute(sql, (*data, id))
        mydb.commit()
        print(cursor.rowcount, "student updated.")

    @staticmethod
    def delete(mydb, cursor, id):
        sql = "DELETE FROM students WHERE id=%s"
        cursor.execute(sql, (id,))
        mydb.commit()
        print(cursor.rowcount, "student deleted.")

    @staticmethod
    def find_by_id(mydb, cursor, id):
        sql = "SELECT * FROM students WHERE id=%s"
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        return result if result else None