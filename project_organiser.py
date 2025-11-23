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
    def __innit__(self, name, length):
        self.name = name
        self.length = length
        self.workstreams = []
        self.attendees = []

        