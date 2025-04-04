import zipfile
f = open("mdp.txt", 'r')
lignes= f.readlines()

archive = zipfile.ZipFile("test_proteger.zip")
 
for l in lignes:
    mdp = l.strip()
    try:
        archive.extractall("extraction_hack", pwd=bytes(mdp, "utf-8"))
        print("Bravo, ",mdp,"était le bon pwd !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        break
    except:
        #print(mdp,"est le mauvais mdp")
        continue