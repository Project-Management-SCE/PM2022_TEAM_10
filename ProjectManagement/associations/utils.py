import csv
from django.db import IntegrityError
from .models import Association
from django.core.exceptions import ObjectDoesNotExist

def InsertAssociationData():
    file = open('Association_data.csv',  encoding="utf8")
    csr = csv.reader(file)
    header =[]
    header = next(csr)
    for header in csr:
        if(header[4] == 'רשומה'):       #check status of asso
            try:
                Association.objects.create(
                    id=header[0],
                    name = header[2],
                    category = header[5],
                    vol_num=header[9],
                    city=header[15],
                    street=header[16],
                    apartment=header[17]
                )
            except IntegrityError as e:
                print('This association id:' + header[0] +' allready exsits')

def getAsso(_id):
    try:
        a=Association.objects.get(id=_id)
        print("Name: " + a.name)
    except ObjectDoesNotExist as e:
        print('This association id:' + _id +' dont exsits')