import re, csv, os

write = open('emails-parsed.csv', 'wb')
writer = csv.writer(write)
writer.writerow(["SuppliedEmail", "Sent_to_Email_Hidden__c", "Sent_to_Email_Hidden_Long__c", "Subject", "Description"])


for fn in os.listdir('emails'):
	file = open('emails/' + fn, "r")


	fromCount = 0
	subjectCount = 0
	toCount = 0
	body = ""

	fromEmail = ""
	toEmail = ""
	subject = ""

	for line in file:
		if subjectCount == 2 and toCount == 2 and fromCount == 2:
			body += line

		if "Subject" in line:
			if subjectCount == 0:
				subjectCount = 1
			elif subjectCount == 1:
				matchObj = re.match('Subject: (.*)', line)
				subject = matchObj.group(1)
				subjectCount = 2

		if "From" in line:
			if fromCount == 0:
				fromCount = 1
			elif fromCount == 1:
				matchObj = re.match('From: ([^@]+@[^@]+\.[^@]+)', line)
				fromEmail = matchObj.group(1)
				fromCount = 2			

		if "To" in line:
			if toCount == 0:
				toCount = 1
			elif toCount == 1:
				matchObj = re.match('To: \[(.*)\]', line)
				toEmail = matchObj.group(1)
				toCount = 2

	print body

	writer.writerow([fromEmail, toEmail, toEmail, subject, body])

write.close()