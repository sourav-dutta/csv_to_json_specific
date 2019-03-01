import csv
import simplejson as json

files1 = ['out_batch_20190214_04.csv','out_batch_20190214_01.csv','out_batch_20190214_02.csv','out_batch_20190214_03.csv','out_batch_20190214_00.csv']
count = 0
data ={}

for file in files1:
  print file
  with open(file, 'rb') as csvfile:
    with open('{}.jsonl'.format(file[0:-4]), 'w') as jsonfile:
      cread =csv.reader(csvfile)
      #jwrite = json.write(jsonfile)
      for row in cread:
        count +=1
        user_id,club,first_name,last_name,country,home_phone_number,home_phone_number_raw,email,phone,original_phone,date_updated,time_of_day,category_code_02 = row
        data = {
          "user_id" : user_id,
          "club" : club,
          "first_name" : first_name,
          "last_name": last_name,
          "country" : country,
          "date_updated" : date_updated,
          "time_of_day" : time_of_day,
          "category_code_02" : category_code_02,
          "contacts" : [{"contact_type": "phone","contact_value": home_phone_number},{"contact_type": "email", "contact_value" : email, "subscription_status":"active"},{"contact_type": "phone","contact_value": original_phone}]
        }
        json.dump(data,jsonfile)
    jsonfile.close()
  csvfile.close()
