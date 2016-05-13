#Created by: Jacob Adams
#Last Update: 5/12/2016 9:30 EST

#imports
import sys

#Total number of records to generate
total = raw_input('Please enter total records to generate: ')
#Controlled username
username = raw_input('Please enter username prefix (no numbers): ')
#Starting DN
dn = raw_input('Please enter start directory number: ')
print "Please input the group identifier (this adds a digit after SEP):"
#Generate unique prefix
HexPrefix = raw_input('Ex: SEPX000 \n')
#Create/Open file to modify called hex.txt
file = open("hex.txt", "w")

#Logic for looping and using user input to generate the CSV
def WriteHex():
    for i in xrange(int(total)):
        #Check length of hex value -2 removes Ox prefix
        length = len(hex(i))-2
        #Sets variable to write controlled DN to file
        FinalDN = int(dn) + i
        #Sets variable to write the controlled username to file
        FinalUser = username + str(FinalDN)

        #Ensures Hex value properly padded up to 4 chars
        if length == 1:
            HexSuffix = ("00" + hex(i)[2:].zfill(2))
        elif length == 2:
            HexSuffix = ("00" + hex(i)[2:].zfill(2))
        elif length == 3:
            HexSuffix = ("0" + hex(i)[2:].zfill(2))
        elif length == 4:
            HexSuffix = (hex(i)[2:].zfill(2))
        else:
            pass
        #Write each line to the file - CSV style
        file.write(str(FinalUser) + ",SEP" + HexPrefix + "000FFFF" + str(HexSuffix) + "," + str(FinalDN) + "\n")

#Run the WriteHex function
WriteHex()
#Closes the file
file.close()

#Nicely end application
sys.exit()

