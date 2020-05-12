import sqlite3
# from datetime import date
#
# today = date.today()
# today = today.strftime('%Y%m%d')
# print(today)

conn = sqlite3.connect('moneycontrol.db')
cursor = conn.cursor()

def tableExists(tableName):
    cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?", (tableName,))
    if(cursor.fetchone()[0] == 0):
        return False
    else:
        return True


############# CREATE THE TABLES IF THEY DONT EXIST #############
if( not tableExists('tablecontrol') ):
    cursor.execute(''' CREATE TABLE tablecontrol (id, title, amount, categoryID, negPos)''')
    conn.commit()

if( not tableExists('categories') ):
    cursor.execute(''' CREATE TABLE categories (id, titleCateg, numberTransactions)''')
    conn.commit()



############# INSERT LINES INTO EACH TABLE #############
def addGain(id, title, amount, categoryID):
    cursor.execute("INSERT INTO tablecontrol VALUES ('{idGain}', '{titleGain}', '{amountGain}', '{categoryId}', 1)"
    .format(idGain = id, titleGain = title, amountGain = amount, categoryId = categoryID))
    conn.commit()

def addExpense(id, title, amount, categoryID):
    cursor.execute("INSERT INTO tablecontrol VALUES ('{idGain}', '{titleGain}', '{amountGain}', '{categoryId}', 0)"
    .format(idGain = id, titleGain = title, amountSpent = amount, categoryId = categoryID))
    conn.commit()

def addCategory(id, titleCateg, numberTransactions = 0):
    cursor.execute("INSERT INTO categories VALUES ('{categoryId}', '{titleCateg}', '{numberTransactions}')"
    .format(titleCateg = titleCateg, categoryId = id, numberTransactions = numberTransactions))
    conn.commit()


############# REMOVE VALUES FROM EACH TABLE  #############
def removeLine(id, table):
    # works now
    cursor.execute("DELETE FROM `{table}` WHERE `id` = '{id}'" .format(id = id, table = table))
    conn.commit()


############# UPDATE VALUES FROM EACH TABLE  #############
def updateLine(newaAttr, refAttr, id, table):
    # check
    cursor.execute("UPDATE `{table}` SET `{refAttr}` = '{newaAttr}' WHERE `id` = '{lineID}'"
    .format(refAttr = refAttr, newaAttr = newaAttr, lineID = id, table = table))
    conn.commit()

############# QUERY VALUES FROM EACH TABLE  #############
def seeTable(table):
    for line in cursor.execute("SELECT * FROM {table}" .format(table = table)):
        print(line)


################ TESTS ################
# updateLine('alex', 'title', '1', 'tablecontrol')
# removeLine('2', 'categories')
# addGain(id, title, amount, categoryID)
# addGain('1', 'primeri', '600', '1')
# seeTable('tablecontrol')
seeTable('categories')

###### close connection to DB #########
conn.close()
