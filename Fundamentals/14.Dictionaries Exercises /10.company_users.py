company_employees = {}

while True:
    command = input()
    if command == 'End':
        break
    company, id_ = command.split(" -> ")
    if company not in company_employees.keys():
        company_employees[company] = []
        company_employees[company].append(id_)
    else:
        if id_ not in company_employees[company]:
            company_employees[company].append(id_)

for company in company_employees.keys():
    print(f"{company}")
    for company_id in company_employees[company]:
        print(f"-- {company_id}")
