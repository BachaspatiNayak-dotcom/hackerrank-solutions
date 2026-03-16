'''
create a employee for a organisation such that whenever a new employee joins
the employeecount increases by 1 and whenever a employee regiens the employee count drop by 1
'''
class Emp:
    company_name='JSP'
    company_loc='BLR'
    employee_count=0

    def __init__(self,en,es,ej,ee):
        self.name=en
        self.sal=es
        self.job=ej
        self.exp=ee
        Emp.employee_count+=1
    def __del__(self):
        Emp.employee_count-=1
