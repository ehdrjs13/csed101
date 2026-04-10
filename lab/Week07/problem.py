def grading(mid,fin) -> str:
    avg = (mid + fin) / 2
    if avg >= 90:
        return avg,"A"
    elif avg >= 80:
        return avg,"B"
    elif avg >= 70:
        return avg, "C"
    elif avg >= 60:
        return avg, "D"
    else:
        return avg, "F"

def studentMgmt(filename:str) -> None:
    result =  open("result.txt", "w")

    with open(filename, "r") as f:
        for line in f:
            data = line.split()
            average, grade = grading(int(data[1]),int(data[2]))
            value = f"{data[0]} {average}({grade})\n"

            result.write(value)
            
    
        
    result.close()

if __name__ == "__main__":
    studentMgmt("score.txt")