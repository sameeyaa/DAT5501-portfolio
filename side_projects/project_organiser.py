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
        writer.writerow(['Name', 'Role', 'Stage Name', 'Workstream Name', 'Meeting Date'])
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
                            file.write(f" - {Participant}\n")
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

#collect the date of the meeting and what the subject of the meeting is
def collect_meeting_info():
    num_meetings = int(input("How many meetings are in this project?"))
    for _ in range(num_meetings):
        meeting_date = input("When is this meeting? (DD-MM-YY)")
        stage_name = input(f"Which stage will the meeting on {meeting_date} be in regard to?")
        workstream_name = input(f"Which workstream will be discussed in the meeting on {meeting_date}?")
        attendees = input(" Enter who will be attending the meeting as a list").split(',')
        meeting_info = {
            'date': meeting_date,
            'stage': stage_name,
            'workstream': workstream_name,
            'attendees': [attendee.strip() for attendee in attendees]
        }
        project['meetings'].append(meeting_info)
    print("Meeting information has been recorded.")

#if the employer wants to update some details
def update_details():
    print("\nWhat do you want to update?")
    print("1. Add a new participant")
    print("2. Edit an existing participant")
    print("3. Add a new stage")
    print("4. Edit an existing stage")
    print("5. Add a new workstream")
    print("6. Edit current workstream")
    print("7. Add a new meeting")
    print("8. Nothing")
    
    choice = input("Please choose from 1-8")
    if choice == '1':
        name = input("Enter participant's name:")
        role = input(f"What is {name}'s role in this project?")
        participant = Participant(name,role)
        project['participants'].append(participant)
        project['roles'][name] = role
    
    elif choice == '2':
        participant_name = input("Enter the participant name you would like to edit:")
        if participant_name in project['roles']:
            new_role = input(f"Enter what {participant_name}'s new role is:")
            project['roles'][participant_name] = new_role
        else:
            print("Member not registered!")
    
    elif choice == '3':
        stage_name = input("What is this stage called?")
        stage_length = int(input(f"How long is the stage {stage_name} (in days)? "))
        stage = Stage(stage_name, stage_length)
        project['stages'][stage_name] = stage

    elif choice == '4':
        stage_name = input("Enter the stage name you would like to edit: ")
        if stage_name in project['stages']:
            new_length = int(input(f"Enter the new length (in days) for stage {stage_name}: "))
            project['stages'][stage_name].length = new_length
        else:
            print("Error! Stage cannot be found!")
    
    

    elif choice == '5':
        stage_name = input("Enter stage name for the new workstream: ")
        if stage_name in project['stages']:
            workstream_name = input(f"Enter new workstream name for stage {stage_name}: ")
            workstream = Workstream(workstream_name)
            project['stages'][stage_name].add_workstream(workstream)
        else:
            print("Stage cannot be found!")
    
    elif choice == '6':
        stage_name = input("Enter the stage name where the workstream exists: ")
        if stage_name in project['stages']:
            workstream_name = input(f"Enter the workstream name that you would like to edit in stage {stage_name}: ")
            workstream = next((ws for ws in project['stages'][stage_name].workstreams if ws.name == workstream_name), None)
            if workstream:
                new_name = input(f"Enter the new name for the workstream {workstream_name}: ")
                workstream.name = new_name
            else:
                print("Workstream cannot be located.")
        else:
            print("Stage can not be found!")
    
    elif choice == '7':
        meeting_date = input("What is the date of the meeting (DD-MM-YYYY): ")
        stage_name = input(f"Which stage is the meeting for? ")
        workstream_name = input(f"Which workstream is a subject in the meeting? ")
        attendees = input("Enter attendees as a list ").split(',')
        meeting_info = {
            'date': meeting_date,
            'stage': stage_name,
            'workstream': workstream_name,
            'attendees': [attendee.strip() for attendee in attendees]
        }
    
    elif choice == '8':
        print("all project information can be found in the folders and files.")

#run code
load_from_csv()
save_to_csv()
create_excel_doc()
create_folders_and_notes()
collect_project_info()
collect_project_info()
collect_meeting_info()
update_details()