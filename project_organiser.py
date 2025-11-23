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

# save information collected onto the CSV
def save_to_csv():
    with open('project_information.csv', mode = 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerrow(['Name', 'Role', 'Stage Name', 'Workstream Name', 'Meeting Date'])
        for stage_name, stage in project['stages'].items():
            for workstream in stage.workstreams:
                for participant in stage.attendees:
                    meeting_dates = [meeting['date'] for meeting in project['meetings'] if meeting['stage'] == stage_name and meeting['workstream'] == workstream.name]
                    for participant in stage.attendees:
                        writer.writerow([participant.name, participant.role,stage_name, workstream.name,", ".join(meeting_dates)])
    print("Details of the project have successfully been saved to 'project_information.csv'.")

#create an excel file to store project info
def create_excel_doc():
    wb = openpyxl.Workbook()     #creates a new workbook
    ws = wb.active               #creates a new sheet in workbook
    ws.title = "Project Details"
    #add sections to the excel sheet
    sections = ['Name', 'Role', 'Stage Name', 'Workstream Name', 'Meeting Date']
    ws.append(sections)
    
    for stage_name, stage in project['stages'].items():
        for workstream in stage.workstreams:
            for meeting in project['meetings']:
                if meeting['stage'] == stage_name and meeting['workstream'] == workstream.name:
                    for participant in stage.attendees:
                        row = [
                            participant.name,
                            participant.role,
                            stage_name,
                            workstream.name,
                            meeting['date']
                        ]
                        ws.append(row)
        wb.save("project_details.xlsx")  #save workbook
        print("An Excel file named 'project_details.xlsx' has been created.")

#create a folder as well as meeting notes
def create_folders_and_notes():
    project_folder = "project_data"
    os.makedirs(project_folder, exists_ok = True)
    
    for stage_name, stage in project['stages'].items():
        stage_folder = os.path.join(project_folder, stage_name)
        os.makedirs(stage_folder, exists_ok = True)
        
        for workstream in stage.workstreams:
            workstream_folder = os.path.join(stage_folder, workstream.name)
            os.makedirs(workstream_folder, exist_ok = True)

            for meeting in project['meetings']:
                if meeting['stage'] == stage_name and meeting['workstream'] == workstream.name:
                    filename = f"{meeting['date']}.md"
                    file_path = os.path.join(workstream_folder, filename)
                    with open(file_path, 'w') as file:
                        file.write(f"# Meeting Date: {meeting['date']}\n")
                        file.write(f"# Stage: {meeting['stage']}\n")
                        file.write(f"# Workstream: {meeting['workstream']}\n")
                        file.write(f"# Attendees:\n")
                        for attendee in meeting['attendees']:
                            file.write(f" - {attendees}\n")
    print("Folders as well as meeting notes have been created.")


#collect information for project
def collect_project_info():
    num_participants = int(input("How many individuals are in this project?"))
    for _ in range(num_participants):
        name = input("What is the name of the participant?")
        role = input(f"What is {name}'s role in this project?")
        participant = Participant(name, role)
        project['participants'].append(participant)
        project['roles'][name] = role
    
    num_stages = int(input("How many stages are in the project?"))
    for _ in range(num_stages):
        stage_name = input("Enter the stage name: ")
        stage_length = int(input(f"How long is the stage {stage_name} (in days)? "))
        stage = Stage(stage_name, stage_length)
        project['stages'][stage_name] = stage

    for stage_name, stage in project['stages'].items():
        num_attendees = int(input(f"How many participants are in stage {stage_name}? "))
        for _ in range(num_attendees):
            attendee_name = input(f"Enter participant name for stage {stage_name}: ")
            if attendee_name in project['roles']:
                participant = next(ppt for ppt in project['participants'] if ppt.name == attendee_name)
                stage.add_attendee(participant)

    for stage_name, stage in project['stages'].items():
        num_workstreams = int(input(f"How many workstreams are in stage {stage_name}? "))
        for _ in range(num_workstreams):
            workstream_name = input(f"Enter workstream name for stage {stage_name}: ")
            workstream = Workstream(workstream_name)
            stage.add_workstream(workstream)

            num_participants_in_ws = int(input(f"How many participants are in workstream {workstream_name}? "))
            for _ in range(num_participants_in_ws):
                participant_name = input(f"Enter participant name for workstream {workstream_name}: ")
                if participant_name in project['roles']:
                    participant = next(ppt for ppt in project['participants'] if ppt.name == participant_name)
                    workstream.add_attendee(participant)
    print("Project data has been collected.")