import sqlite3

conn = sqlite3.connect('storage.db')
cursor = conn.cursor()

def tableExists(tableName):
    cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?", (tableName,))
    if(cursor.fetchone()[0] == 0):
        return False
    else:
        return True

if( not tableExists('classes') ):
    cursor.execute(''' CREATE TABLE classes (code, name, professor)''')
    conn.commit()

def addClass(code, name, professor):
    cursor.execute("INSERT INTO classes VALUES ('{classCode}', '{className}', '{classProfessor}')"
    .format(classCode = code, className = name, classProfessor = professor))
    conn.commit()

def removeClassByCode(code):
    # works now
    cursor.execute("DELETE FROM classes WHERE `code` = '{classCode}'" .format(classCode = code))
    conn.commit()

def updateClass(newaAttr, refAttr, code):
    cursor.execute("UPDATE classes SET `{refAttr}` = '{newaAttr}' WHERE `code` = '{classCode}'"
    .format(refAttr = refAttr, newaAttr = newaAttr, classCode = code))
    conn.commit()

#exemplos de uso - execute em sequencia para ver as mudanças
# addClass('cs103', 'alg1', 'dk')
# updateClass('vign', 'professor', 'cs103')
# removeClassByCode('cs103')

myCsClasses = []

def seeClasses():
    for row in cursor.execute('SELECT * FROM classes'):
        print(row[0], row[1], row[2])

# updateClass('circuitos', 'name', 'ci1003')
seeClasses()
conn.close()
