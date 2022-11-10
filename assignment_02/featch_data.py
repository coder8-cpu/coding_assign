import requests
import csv
import time
import json
class main:
    def __init__(self):
        self.json_data = None
        self.api_data = []
        
    def call_(self):
        
            connect = requests.get('https://randomuser.me/api/')
            data = connect.text
            self.json_data = json.loads(data)
            self.json_data = self.json_data['results'][0]
            self.api_data.append(self.json_data)
    
            
    def write_csv(self,d_ata):
            __fields__ = ["first Name","last name","username","email","phone","password","dob","date"]
        
        
            file_name = "user_data.csv"
            with open(file_name, 'w', encoding="utf-8") as csvfile: 
                # creating a csv writer object 
                csvwriter = csv.writer(csvfile) 
                    
                # writing the fields 
                csvwriter.writerow(__fields__) 
                    
                # writing the data rows
                for i in range(len(d_ata)):
                    data = d_ata[i]
                    self.row_data = [[data["name"]["first"],data["name"]["last"],data ["login"]["username"],data["email"],
                                data["phone"],data["login"]["password"],data["dob"]["date"],data["registered"]["date"]]]
                    csvwriter.writerows(self.row_data)

           
op = main()
for i in range(5):
   
    time.sleep(1)
    op.call_()
op.write_csv(op.api_data)            

print("data featched and saved to user_data.csv")

