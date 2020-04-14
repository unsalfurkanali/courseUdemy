def dataReading():
    with open("noteList.txt", "r", encoding="utf-8") as file:
        for i in file:
            i = i[:-1]
            listInfo = i.split(",")
            lgCalc(listInfo)
    
def dataWriting(x, note):
    with open("letterGrade.txt", "a", encoding="utf-8") as wrFile:
        wrFile.write("{}\t\t---->{}\n".format(x, note))

def lgCalc(x):
    sum = float(x[1])*(3/10) + float(x[2])*(3/10) + float(x[3])*(4/10)
    if 94 <= sum <= 100:
        dataWriting(x[0],"A")
    elif 90 <= sum <= 93:
        dataWriting(x[0], "A-")
    elif 87 <= sum <= 89:
        dataWriting(x[0], "B+")
    elif 84 <= sum <= 86:
        dataWriting(x[0], "B")
    elif 80 <= sum <= 83:
        dataWriting(x[0], "B-")
    elif 77 <= sum <= 79:
        dataWriting(x[0], "C+")
    elif 74 <= sum <= 76:
        dataWriting(x[0], "C")
    elif 70 <= sum <= 73:
        dataWriting(x[0], "C-")
    elif 67 <= sum <= 69:
        dataWriting(x[0], "D+")
    elif 64 <= sum <= 66:
        dataWriting(x[0], "D")
    elif 60 <= sum <= 63:
        dataWriting(x[0], "D-")
    elif 0 <= sum <= 60:
        dataWriting(x[0], "F")
        
dataReading()
