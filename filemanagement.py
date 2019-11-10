def readFile():
    file = open("test.txt", "r")
    content = file.read()
    file.close()
    return content


def writeFile(c):
    file = open("test.txt", "w")
    file.write(c)
    file.close()
    return True


def resetFile():
    file = open("test.txt", "w")
    file.write()
    file.close()
    return True


def backupFile():
    file = open("test.txt", "r")
    copy = file.read()
    file.close()

    backupfile = open("backup.txt", "x")
    backupfile.close()

    backupfile = open("backup.txt", "w")
    backupfile.write(copy)
    backupfile.close()


def addToFile(c):
    file = open("test.txt", "a")
    file.write("\n" + c)
    file.close()
    return True