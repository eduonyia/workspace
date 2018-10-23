# function reads a file and return a list
def file2list(filename):
    f = open(filename, "r")
    lines = f.readlines()
    contents = []

    for x in lines:
        x = x.split('|')[0]
        if len(x) != 0:
            contents.append(x)

    f.close()

    return contents


def file2list2(filename):
    f = open(filename, "r")
    lines = f.readlines()
    contents = []

    for x in lines:
        x = x.split('|')[5]
        if len(x) != 0:
            contents.append(x)

    f.close()

    return contents


path = 'C:/Users/Temitope/Documents/FCMB/'


# reading files
fcmbIndividuals = file2list(path + 'consumer.txt')
fcmbCorporate = file2list2(path + 'corp.txt')
crFCMB = file2list(path + 'customer-nos-3.txt')

#######################################################
#         Comparison on Consumer file/ Corporate file
######################################################
matchedInd = set(crFCMB).intersection(set(fcmbIndividuals))
matchedCorp = set(crFCMB).intersection(set(fcmbCorporate))

unmatchedInd = set(fcmbIndividuals).difference(set(crFCMB))
unmatchedCorp = set(fcmbCorporate).difference(set(crFCMB)) # set of elements only in A

###############################################
#          Comparison on Both
###############################################

fcmbAll = fcmbIndividuals + fcmbCorporate
matchedAll = set(crFCMB).intersection(set(fcmbAll))
unmatchedAll = set(crFCMB).symmetric_difference(set(fcmbAll))

###################################################################
#    Printing
###################################################################
print('Number of consumer customers(from FCMB):', len(fcmbIndividuals))
print('Number of Corporate customers(from FCMB):', len(fcmbCorporate))
print('All FCMB customers(from FCMB): ', len(fcmbAll))
print('FCMB customer in CreditRegistry Database:', len(crFCMB))
print()
print("############## Matched #########################")
print()
print('Number of matches Individuals:', len(matchedInd))
print()
print('Number of matches Corporate:', len(matchedCorp))
print()
print('All customer matches: ', len(matchedAll))
print("############## UnMatched #########################")
print()
print('In FCMB submission but not in bureau repo (Individuals):', len(unmatchedInd))
print()
print('In FCMB submission but not in bureau repo (Corporate):', len(unmatchedCorp))
print()
print('All unmatched customers : ', len(unmatchedAll))



#################################################################
#                        Save in a file
#################################################################

with open("matchedAll.txt", "w") as f:
    f.write('\n'.join(matchedAll))

with open("unmatchedAll.txt", "w") as f:
    f.write('\n'.join(unmatchedAll))

with open("matchedInd.txt", "w") as f:
    f.write('\n'.join(matchedInd))

with open("matchedCorp.txt", "w") as f:
    f.write('\n'.join(matchedCorp))

with open("unmatchedInd.txt", "w") as f:
    f.write('\n'.join(unmatchedInd))

with open("unmatchedCorp.txt", "w") as f:
    f.write('\n'.join(unmatchedCorp))













