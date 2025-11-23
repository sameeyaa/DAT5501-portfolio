import openpyxl
import os
from datetime import date
import csv

#create a directory for the project data
project = {
    'participants': [],
    'roles' : {},
    'stages' : {},
    'meetings' : []
}

#create classes to make it easier to extract when collecting project details
class Participant:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Stage:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.workstreams = []
        self.attendees = []

class Workstream:
    def __init__(self,name):
        self.name = name
        self.attendees = []

    def add_attendee(self, participant):
        self.attendees.append(participant)

#create a csv file to store data
def create_csv():
    with open('project_information.csv', mode = 'w', line = '') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Role', 'Stage Name', 'Workstream Name', 'Meeting Date'])
    print("CSV file 'project_information.csv' has been created.")