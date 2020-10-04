from datetime import date
import pandas as pd
import os



today = date.today()
today = str(today)
print("Today's date:", today)

print(type(today))

Bike = {
        'bikes': ['Yamaha R1','Hero Hunk','KTM RC','Kawasaki Ninja'],
        'Price': [220000,251000,270400,350500]
        }
df = pd.DataFrame(Bike)
today = str(date.today())

# exporting the files
cwd = os.getcwd()

path = os.path.join(cwd , "data")
author_file = "author" + today +".xlsx"
path = os.path.join(path , author_file)


print(path )




df.to_excel(path, index=False)
print("exported the file ")