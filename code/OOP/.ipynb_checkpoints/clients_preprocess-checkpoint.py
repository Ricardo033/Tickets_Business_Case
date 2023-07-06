#-----------------------#
# Clients Preprocessing #
#-----------------------#

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import os 

    
class clients_preprocessing:
    
    def __init__(self):
        #Data Location
        path="C:/Users/ricar/OneDrive/Escritorio/Masters_of_Statistics/job_positions/Second Attempt/Stratics/data"
        os.chdir(path)
    
        # Reading Data
        self.clients=pd.read_csv('clients.csv', sep =',')
        
    def inputer(self):
        
        # Replacing blanks for NAN values
        self.clients['age']=self.clients['age'].replace("(blank)",np.nan)
        
        #Single variable
        age = self.clients['age']
        
        #Imputer form sklearn with median to make it robust against outliers
        imputer = SimpleImputer(strategy='median')
        age2= age.values.reshape(-1, 1)
        imputer.fit(age2)
        imputed_data = imputer.transform(age2)
        imputed_series = pd.Series(imputed_data.flatten()).astype(int)

        self.clients['age'] = imputed_series

        return self.clients
    
    def age_outliers_replace(clients):
    
        clients['age'][clients['age']> 95] = np.median(clients['age'])
        clients['age'][clients['age']< 10] = np.median(clients['age'])

        return clients 