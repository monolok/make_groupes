import random
import csv
import os
#from dotenv import load_dotenv
from pyairtable import Api

def create_groups(group_size):
    #load_dotenv()
    api = Api(api_key=os.environ["AIRTABLE"])
    table = api.table("appiFg9yck56F1H2y", "tbltln7mleTTxQqOb")
    student_table = table.all()
    students = []
    for student in student_table:
        students.append(student["fields"]["Name"])
    random.shuffle(students)
    num_students = len(students)
    num_groups = num_students // group_size
    if num_students % group_size != 0:
        num_groups += 1
    groups = []
    for i in range(num_groups):
        start = i * group_size
        end = start + group_size
        group = students[start:end]
        groups.append(group)
    with open('data/file.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(groups)
    return groups