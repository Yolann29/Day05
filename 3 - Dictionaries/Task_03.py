student = {
    "name" : "Maurice",
    "academic_year" : "Third grade"
}
student.update({
    "units" : [
        {
            "name" : "Java",
            "credits" : 13,
            "grade" : "D"},
        {
            "name" : "Web Development",
            "credits" : 27,
            "grade" : "B"},
        {
            "name" : "Network and System Administration",
            "credits" : 7,
            "grade" : "C"
        }
        ]
    })
#print(student)

grade_weight_mapping = {
    "A" : 4,
    "B" : 3,
    "C" : 2,
    "D" : 1,
    "E" : 0
}

sum = moy = 0
for i in range(3):
    sum += student["units"][i]["credits"]
    moy += grade_weight_mapping[student["units"][i]["grade"]]*student["units"][i]["credits"]


student.update({
    "total_credits" : sum,
    "gpa" : moy/sum
})
print(grade_weight_mapping)
print(student)