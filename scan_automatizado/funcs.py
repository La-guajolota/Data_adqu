import csv

def storage(array,doc_name):
     with open(doc_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(array)