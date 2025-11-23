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

#load information about the project from csv
def load_from_csv():
    try:
        with open('project_information.csv', mode = 'r' , newline = '') as file:
            reader = csv.DictReader(file)
            for row in reader:
                participant_name = row['Name']
                participant_role = row['Role']
                stage_name = row['Stage Name']
                workstream_name = ['Workstream Name']
                meeting_date = row ['Meeting Date']
                
                #add a participant to the details if not already mentioned
                if participant_name not in project ['roles']:
                    participant = Participant(participant_name, participant_role)
                    project['participants'].append(participant)
                    project['roles'][participant_name] = participant_role
                
                #add workstreams into the stages
                stage = project['stages'][stage_name]
                workstream = Workstream(workstream_name)
                if workstream_name not in [ws.name for ws in stage.workstreams]:
                    stage.add_workstream(workstream)
            
                
                #add the meeting dates
                if meeting_date:
                    meeting_details = {'date': meeting_date, 'stage': stage_name, 'workstream': workstream_name}
                    project['meetings'].append(meeting_details)
            print("Details have been loaded from CSV.")
    except FileNotFoundError:
        print("Error! Cannot find the CSV file, please provide one.")