import csv, getopt, sys

def main(argv):
	filename = raw_input('Filename: ')

	print "Reading" + filename + ".csv"

	sourcefile = open('offset-accounts.csv', 'rb')

	accountIds = {}
	for row in csv.reader(sourcefile, delimiter=','):
		accountIds[row[0]] = row[1]

	print "Size of accountIds: " + str(len(accountIds))

	read = open(filename + '.csv', 'rb')
	write = open(filename + '-parsed.csv', 'wb')
	writer = csv.writer(write)

	filereader = csv.reader(read, delimiter=',')

	count = 0

	writer.writerow(['Id', 'Account Id', 'Account Name', 'Record Type Id'])

	for row in filereader:
		count += 1
		if count % 100000 == 0:
			print count 
	#	if row[8] == '012a0000001RUmI':
		if accountIds.has_key(row[3]):
			writer.writerow([row[0], row[3], accountIds.get(row[3]), row[8]])

	write.close()
	read.close()

if __name__ == "__main__":
   main(sys.argv[1:])