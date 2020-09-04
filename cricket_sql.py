import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "sh23ri01@" , 
    database = "CRICKET"
)

mycursor = mydb.cursor()

fname = input("Enter the player name to be found....")
sql = "select * from player"
mycursor.execute(sql)
r = mycursor.fetchall()
for i in r:
    if fname.lower() == i[0].lower():
        print("Player Name:",i[0])
        print("Runs:",i[1])
        print("Matches:",i[2])
        print("Strike Rate:",i[3])
        print("50`s:",i[4])
        print("100`s:",i[5])
        print("Best Score:",i[6])
        flag = True
        break
    else:
        flag = False

if not flag:
    print("sorry !! there are no such names like that :(")
