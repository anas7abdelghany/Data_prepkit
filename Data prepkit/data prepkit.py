import numpy as np 
import pandas as pd

class Dataprepkit:
    def __init__(self):
        
        self.data = None

    def read_data(self, file_path): 
        
        try:
            file_format = file_path.split('.')[-1]
            if file_format == 'csv':
                self.data = pd.read_csv(file_path)
            #elif file_format == 'excel':
                #self.data = pd.read_excel(file_path)
            elif file_format == 'json':
                self.data = pd.read_json(file_path)
            elif file_format == ["xlsx","xls"]:
                self.data = pd.read_excel(file_path)    
            else:
                raise ValueError("Unsupported file format")
                
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            
    
    def gen_summary(self):
        if self.data is not None:
            return self.data.describe()
        else:
            print("No data available.")
            
    def most_frequent_values(self):
        if self.data is not None:
            return self.data.mode().iloc[0]
        else:
            print("No data available.")
            
            
            
    
    def handle_missing_values(self, handling_Type):
        try:
            if handling_Type == 'mean':
                return self.data.fillna(self.data.mean())
            elif handling_Type == 'median':
                return self.data.fillna(self.data.median())
            elif handling_Type == 'drop':
                return self.data.dropna()
            else:
                raise ValueError("Unsupported missing value handling strategy")
        except Exception as e:
            print(f"Error handling missing values: {str(e)}")
            
            
    
    def one_hot_encoding(self, columns):
        if self.data is not None:
            return pd.get_dummies(self.data, columns=columns)
        else:
            print("No data available.")
    
    def label_encoding(self, column):
        if self.data is not None:
            labels = self.data[column].astype('category').cat.codes
            return labels
        else:
            print("No data available.")
            
            

file_path = input("Enter your file path: ")
obj = Dataprepkit()
obj.read_data(file_path)