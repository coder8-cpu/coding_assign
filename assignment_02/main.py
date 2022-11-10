import csv

class sort_:
    def __init__(self):
        self.store_date = []
        self.store_sorted_datas = []
    def sorted(self):
        filename = "user_data.csv"
        with open(filename,"r") as file:
            data_csv =  csv.reader(file)
            for i in data_csv:
                if i == []:
                
                    pass
                elif i[7] == "date":
                    pass
                else:
                    
                    date = (i[7])
                    date = date[0:4]
                    self.store_date.append((int(date)))
                 # bubble short
        for i in range(len(self.store_date)):
            for j in range(0,len(self.store_date)-i-1):
                if self.store_date[j] > self.store_date[j+1]:
                    self.store_date[j],self.store_date[j+1] = self.store_date[j+1], self.store_date[j]
                if self.store_date[j] == self.store_date[j+1]:
                    pass
    def arrange_data(self):
        
       for i in self.store_date:
            with open("user_data.csv", "r") as file:
                data_csv =  csv.reader(file)
                for lines in data_csv:
                    if lines == []:
                
                        pass
                    elif lines[7] == "date":
                        pass
                    else:
                       
                        data= lines[7]
                        
                        if data[0:4] == str(i):
                                if lines in self.store_sorted_datas:
                                    pass
                                else:
                                    self.store_sorted_datas.append(lines)
          
       return self.store_sorted_datas 
                                
    def write_csv(self,d_ata):
            __fields__ = ["first Name","last name","username","email","phone","password","dob","date"]
        
        
            file_name = "sorted_user_data.csv"
            with open(file_name, 'w') as csvfile: 
                # creating a csv writer object 
                csvwriter = csv.writer(csvfile) 
                    
                # writing the fields 
                csvwriter.writerow(__fields__)

                for i in range(len(d_ata)):
                    s_ = [data[i]]
                    csvwriter.writerows(s_)
                      
                
        
                
            
s = sort_()
s.sorted()
data = s.arrange_data()
print(data)
s.write_csv(data)
print("data saved to sorted_user_data_csv")
