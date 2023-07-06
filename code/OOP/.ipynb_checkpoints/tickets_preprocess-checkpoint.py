#-----------------------#
# Clients Preprocessing #
#-----------------------#

import pandas as pd
import numpy as np
import os 

class tickets_preprocessing:
    
    def __init__(self):
        
        #Setting Working Directory
        os.chdir("C:/Users/ricar/OneDrive/Escritorio/Masters_of_Statistics/job_positions/Second Attempt/Stratics/data")
        
        self.tickets = pd.read_csv('tickets.csv',sep=',')

    def payment_types_col(self):
        
        tickets =self.tickets
        tickets['class'] = (np.where(tickets['payed']>=0,"sells",
                    (np.where(tickets['payed']<0,"returns","other"))))
        return self.tickets