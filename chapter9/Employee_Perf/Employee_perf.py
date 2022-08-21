# Needs Improvement (1-2)
# Met Expectations(2-3)
# High Achievement(3-4)
# Extraordinary Achievement (4-5)
# Properties - emp_id , name , score

class Employee:
    company_name = "ABC ltd"
    def __init__(self, emp_id, name, score):
        self.emp_id = emp_id
        self.name = name
        self.score = score

    def get_perf_rating(self):
        if self.score >=1 and self.score <=2:
            return "Needs Improvement"
        elif self.score >2 and self.score <=3:
            return "Met Expectations"
        elif self.score >3 and self.score <=4:
            return "High Achievement"
        elif self.score >4 and self.score <=5:
            return "Extraordinary Achievement"



emp1 = Employee(1001, "sachin", 3.5)
res1 = emp1.get_perf_rating()
print(res1)

emp2 = Employee(1002, "Anjali", 4.1)
res2 = emp2.get_perf_rating()
print(res2)

print(Employee.company_name)

