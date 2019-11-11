import filemanagement


def addNewUser(username):
    if checkIfUserExists(username):
        filemanagement.addToFile(username)
        return True
    else:
        return False


def checkIfUserExists(username):
    boo = True
    for i in range(1, len(filemanagement.readFile())):
        if username == filemanagement.readFile()[i][0]:
            boo = False
    return boo


def levelUp(username):
    for i in range(len(filemanagement.readFile())):
        if username == filemanagement.readFile()[i][0]:
            level = int(filemanagement.readFile()[i][1])
            level += 1
#Dem User das LevelUp eintragen!
    return True