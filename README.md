# cspm-forcesync
A tool to force all accounts within a tenant to update their asset status. 

Handy if you're working on CloudBots and ~~you're too impatient to wait for the action to occur at the next set interval~~ you're keen to see results :)

Uses the CloudGuard CSPM public API to scan for all AWS, Azure and GCP accounts and then force a sync on them all. 
All it requires is for your API keys to be set as environment variables CHKP_CLOUDGUARD_ID and CHKP_CLOUDGUARD_SECRET.
