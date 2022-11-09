import pymongo
import os

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["server"]
mycol = mydb["db"]

for x in mycol.find({"cod_sfz": 100}):
 print('----------------------------------------------------------------------------------');
 print(' INICIO ');
 if 'xml_env' in x:
    print(x['num_loj']);
    print(x['num_pdv']);
    print(x['dat_hor_ems']);
    print(x['chv_acs']);
    print(x['xml_env']);
        
    dataFile = x['dat_hor_ems'].strftime("%d%m%Y")
    print(dataFile)

    folderData = "E:/XML/" + dataFile;
    if os.path.isdir(folderData):
     print(folderData)
    else:
     os.mkdir(folderData)

    folderLoja = "E:/XML/" + dataFile +'/'+ str(x['num_loj']);
    if os.path.isdir(folderLoja):
     print(folderLoja)
    else:
     os.mkdir(folderLoja)

    fileName = "E:/XML/" + dataFile +'/'+ str(x['num_loj']) + "/" + x['chv_acs'] +".xml"

    xml = open(fileName, "w")
    xml.writelines(x['xml_env'])
    xml.close()
print(' FINAL ');
print('----------------------------------------------------------------------------------');