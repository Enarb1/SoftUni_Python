NAME = str(input())
PROJECTS_QTY = int(input())
ONE_PROJECT_WORK_HOURS = 3

time_needed = ONE_PROJECT_WORK_HOURS * PROJECTS_QTY

print(f'The architect {NAME} will need {time_needed} hours to complete {PROJECTS_QTY} project/s.')