class SalaryError(Exception):
    pass

def check_salary(salary):
    if salary<0:
        raise SalaryError("Invalid salary cannot be zero")
    else:
        return salary

n=int(input("Enter your salary:"))
cs=check_salary(n)

print(cs)