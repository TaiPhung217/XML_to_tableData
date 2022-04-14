import xml.etree.ElementTree as  XeE          #khai báo thư viện ElementTree
import pandas as pd                           #thư viện pandas để phân tích data                   
import time                                   #thư viện time để  đổi số giây trong createAt về dạng ngày tháng

cols = ["id","age","name","createAt"]              # các thuộc tính cột
rows = []

xmlparse = XeE.parse('Xml.xml')                     
root = xmlparse.getroot()

#duyệt từng node con trong root để lấy giá trị 
for i in root:       
        id = i.get('id')
        createAt = i.get('createAt')
        age = i.find('age').text
        name = i.find('name').text
        
        timetmp = time.strftime('%d/%m/%Y', time.localtime(int(createAt)))

        rows.append({"id":id,
                        "age":age,
                        "name":name,
                        "createAt":timetmp})
table = pd.DataFrame(rows, columns=cols)
print(table)
