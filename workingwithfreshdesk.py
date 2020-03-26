import requests
from requests.auth import HTTPBasicAuth
import os
import csv
import json
import time


class WorkWithFreshdesk:

    domain = os.environ['FDDOM']
    api_key = os.environ['FDKEY']
    password = "x"
    csvpath = '/Users/patricklarsen/Downloads/ActualJunkFromJunk-Bounce312.csv'

    def get_ids_from_csv(self, csvpath):
        with open(csvpath) as csv:
            readCSV = csv.reader(csv, delimiter=',')
            ids = []
            for row in readCSV:
                idee = row[0]
                ids.append(idee)
        return ids

    
    def __init__(self):
        
        self.ids_from_csv = self.get_ids_from_csv(self.csvpath).remove('Ticket ID')


    # def makeNewType(string):

    def searchCases():
        pass


    def change_type(idee):
        ticket_id = idee

        headers = { 'Content-Type' : 'application/json' }

        ticket = {
        'type' : 'Junk [J]',
        }

        r = requests.put("https://"+ domain +".freshdesk.com/api/v2/tickets/"+ticket_id, auth = (api_key, password), headers = headers, data = json.dumps(ticket))

        if r.status_code == 200:
            print(f"Ticket {idee} updated successfully")
        else:
            print("Failed to update ticket, errors are displayed below,")
            response = json.loads(r.content)
            print(response["errors"])

            print("x-request-id : " + r.headers['x-request-id'])
            print("Status Code : " + r.status_code)



    def update_tickets(self, ticketIdsListItem, function, sleeptime=.375):
        for idee in ticketIdsListItem:
            function(idee)
            time.sleep(sleeptime)

    


    if __name__ == "__main__":
        update_ticket_IDs(idees)   









