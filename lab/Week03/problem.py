def avg(a:int,b:int) -> float:
    return (a+b) / 2

def grading(score:int) -> str:
    grades = ["A","B","C","D","F"]
    if score >= 90:
        return grades[0]
    if score >= 80:
        return grades[1]
    if score >= 70:
        return grades[2]
    if score >= 60:
        return grades[3]
    return grades[4]

mid = int(input("Midterm?:"))
final = int(input("Final?:"))
value = avg(mid,final)

print(f"\nAverage: {value} \nGrade: {grading(value)}")
