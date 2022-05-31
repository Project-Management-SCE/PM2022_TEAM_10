import csv
import requests
import json
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from .models import Association

def InsertAssociationData():
    file = open('Association_data.csv',  encoding="utf8")
    csr = csv.reader(file)
    header =[]
    header = next(csr)
    for header in csr:
        if header[4] == 'רשומה':       #check status of asso
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
            except IntegrityError:
                print('This association id:' + header[0] +' allready exsits')

def getAsso(_id):
    try:
        a=Association.objects.get(id=_id)
        print("Name: " + a.name)
    except ObjectDoesNotExist:
        print('This association id:' + _id +' dont exsits')

def ApiUpdateAsso():
    url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=be5b7935-3922-45d4-9638-08871b17ec95&offset=63000'
    add_count = 0
    del_count = 0
    while True:
        response_API = requests.get(url)
        data = response_API.text
        parse_json = json.loads(data)
        records = parse_json['result']['records']
        if len(records)==0:
            break
        for rec in records:
            print('-----')
            _id = rec['מספר עמותה']
            _status = rec['סטטוס עמותה']
            try:
                asso = Association.objects.get(id=_id)
                if _status != 'רשומה':
                    asso.delete()
                    print('Deleted')
                    del_count+=1
            except ObjectDoesNotExist:
                if _status == 'רשומה':
                    _name = rec['שם עמותה בעברית']
                    _category = rec['סיווג פעילות ענפי']
                    _vol_num=rec['כמות מתנדבים']
                    if _vol_num is None:
                        _vol_num=0
                    _city=rec['כתובת - ישוב']
                    if _city is None:
                        _city=''
                    _street=rec['כתובת - רחוב']
                    if _street is None:
                        _street=''
                    _apartment=rec['כתובת - מספר דירה']
                    if _apartment is None:
                        _apartment=''
                    Association.objects.create(
                        id=_id,
                        name = _name,
                        category = _category,
                        vol_num= _vol_num,
                        city=_city,
                        street=_street,
                        apartment=_apartment
                    )
                    add_count+=1
                    print('Added')

        url='https://data.gov.il/'+parse_json['result']['_links']['next']
    print('Batch job finished, Added associations = ',add_count,' Deleted associations = ', del_count)