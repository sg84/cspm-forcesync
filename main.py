import requests
import json
import os
import sys
# CloudGuard access key and secret should be set as environment variables

CHKP_CLOUDGUARD_ID = os.getenv('CHKP_CLOUDGUARD_ID')
CHKP_CLOUDGUARD_SECRET = os.getenv('CHKP_CLOUDGUARD_SECRET')
if CHKP_CLOUDGUARD_ID == None or CHKP_CLOUDGUARD_SECRET == None:
    print("ERROR - you have not defined your environment variables for API access!")
    sys.exit(-1)
CG_API_ENDPOINT = "https://api.dome9.com/v2/"

# Get AWS Cloud IDs
r = requests.get(CG_API_ENDPOINT + "CloudAccounts", auth=(CHKP_CLOUDGUARD_ID, CHKP_CLOUDGUARD_SECRET))
result_json = json.loads(r.text)
aws_sub_ids = []
if  len(result_json) > 0:
    for i in result_json:
        aws_sub_ids.append(i['id'])
print(aws_sub_ids)

# Sync AWS accounts
if len(aws_sub_ids) > 0:
    for i in aws_sub_ids:
        r = requests.post(CG_API_ENDPOINT + "CloudAccounts/%s/SyncNow" % i, auth=(CHKP_CLOUDGUARD_ID, CHKP_CLOUDGUARD_SECRET))
        print(r.text)

# Get Azure Cloud IDs
r = requests.get(CG_API_ENDPOINT + "AzureCloudAccount", auth=(CHKP_CLOUDGUARD_ID, CHKP_CLOUDGUARD_SECRET))
result_json = json.loads(r.text)
azure_sub_ids = []
if  len(result_json) > 0:
    for i in result_json:
        azure_sub_ids.append(i['id'])
print(azure_sub_ids)

# Sync Azure accounts
if len(azure_sub_ids) > 0:
    for i in azure_sub_ids:
        r = requests.post(CG_API_ENDPOINT + "AzureCloudAccount/%s/SyncNow" % i, auth=(CHKP_CLOUDGUARD_ID, CHKP_CLOUDGUARD_SECRET))
        print(r.text)

# Get Google Cloud IDs
r = requests.get(CG_API_ENDPOINT + "GoogleCloudAccount", auth=(CHKP_CLOUDGUARD_ID, CHKP_CLOUDGUARD_SECRET))
result_json = json.loads(r.text)
google_sub_ids = []
if  len(result_json) > 0:
    for i in result_json:
        google_sub_ids.append(i['id'])
print(google_sub_ids)

# Sync Google accounts
if len(google_sub_ids) > 0:
    for i in google_sub_ids:
        r = requests.post(CG_API_ENDPOINT + "GoogleCloudAccount/%s/SyncNow" % i, auth=(CHKP_CLOUDGUARD_ID, CHKP_CLOUDGUARD_SECRET))
        print(r.text)

