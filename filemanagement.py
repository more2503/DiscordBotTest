filename = "test.txt"

def readFile():
    file = open(filename, "r")
    content = file.read()
    file.close()

    content = content.splitlines()
    return [l.split(',') for l in ','.join(content).split(';')]


def writeFile(c):
    file = open(filename, "w")
    file.write(c)
    file.close()
    return True


def resetFile():
    file = open(filename, "w")
    file.write()
    file.close()
    return True


def backupFile():
    file = open(filename, "r")
    copy = file.read()
    file.close()

    backupfile = open("backup.txt", "x")
    backupfile.close()

    backupfile = open("backup.txt", "w")
    backupfile.write(copy)
    backupfile.close()

    return True


def addToFile(c):
    file = open(filename, "a")
    file.write(";" + c + ",0")
    file.close()
    return True