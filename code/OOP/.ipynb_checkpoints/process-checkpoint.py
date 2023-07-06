#------------------#
# Datasets Process #
#------------------#

import pandas as pd

class data_process:
    
    def clients_tickets_merge(clients_data, tickets_data):
        '''
        This function merges the information from those clients who appear in the tickets database.
        -input: clients and customers datasets (ideally after preprocessing)
        -output: Combination of both datasets including only the clients in common (in both datasets). 
        '''
        clients_tickets= pd.merge(tickets_data, clients_data, on = 'clientID', how='inner')
        
        #Adding an S to store id so it will be considered as a class
        clients_tickets['storeID'] = ('S: ' + clients_tickets['storeID'].astype('string')).astype(object)
        
        
        return clients_tickets