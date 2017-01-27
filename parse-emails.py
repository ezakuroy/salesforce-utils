### parse-emails.py
### Utility to convert Email-to-case failure Emails to a single uploadable .csv 
### for use with Salesforce data loader and single .txt files in /emails folder
### last updated tharada, 1/27/2017

import re, csv, os

write = open('emails-parsed.csv', 'wb')
writer = csv.writer(write)
writer.writerow(["SuppliedEmail", "Sent_to_Email_Hidden__c", "Sent_to_Email_Hidden_Long__c", "Subject", "Description", "Origin", "Priority"])


for fn in os.listdir('emails'):
	file = open('emails/' + fn, "r")

	fromCount = 0
	subjectCount = 0
	toCount = 0
	body = ""

	fromEmail = ""
	toEmail = ""
	subject = ""

	skipFirst = True

	for line in file:
		if subjectCount == 2 and toCount == 2 and fromCount == 2:
			if skipFirst:
				skipFirst = False
			else:
				body += line

		if "Subject" in line:
			if subjectCount == 0:
				subjectCount = 1
			elif subjectCount == 1:
				matchObj = re.match('Subject: (.*)', line)
				if matchObj is not None:
					subject = matchObj.group(1)
				subjectCount = 2

		if "From" in line:
			if fromCount == 0:
				fromCount = 1
			elif fromCount == 1:
				matchObj = re.match('From: ([^@]+@[^@]+\.[^@(]+)(.*)', line)
				if matchObj is not None:
					fromEmail = matchObj.group(1)
				fromCount = 2			

		if "To" in line:
			if toCount == 0:
				toCount = 1
			elif toCount == 1:
				matchObj = re.match('To: \[(.*)\]', line)
				if matchObj is not None:
					toEmail = matchObj.group(1)
				toCount = 2

	print body

	writer.writerow([fromEmail, toEmail, toEmail, subject, body, "Email", "High - Backlog"])

write.close()