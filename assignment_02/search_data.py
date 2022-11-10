import csv

class search_data:
    def __init__(self):
        pass
    def search(self,username):
        with open("sorted_user_data.csv","r",encoding="utf-8") as file:
            data_csv =  csv.reader(file)
            for i in data_csv:
                
                    if i == []:
                
                        pass
                    elif i[0] == "first name":
                        pass
                    else:
                        if i[2] == username:
                            return i
s = search_data()
print(s.search("smallelephant600"))
