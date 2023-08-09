# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"J613000","system":"readv2"},{"code":"J622.00","system":"readv2"},{"code":"J622.11","system":"readv2"},{"code":"J62y.11","system":"readv2"},{"code":"J634.00","system":"readv2"},{"code":"16062.0","system":"med"},{"code":"17222.0","system":"med"},{"code":"17330.0","system":"med"},{"code":"21769.0","system":"med"},{"code":"22411.0","system":"med"},{"code":"23511.0","system":"med"},{"code":"23775.0","system":"med"},{"code":"24901.0","system":"med"},{"code":"26490.0","system":"med"},{"code":"36107.0","system":"med"},{"code":"36194.0","system":"med"},{"code":"39945.0","system":"med"},{"code":"41386.0","system":"med"},{"code":"41480.0","system":"med"},{"code":"48488.0","system":"med"},{"code":"49042.0","system":"med"},{"code":"53704.0","system":"med"},{"code":"55637.0","system":"med"},{"code":"55962.0","system":"med"},{"code":"56070.0","system":"med"},{"code":"57324.0","system":"med"},{"code":"64451.0","system":"med"},{"code":"65050.0","system":"med"},{"code":"65067.0","system":"med"},{"code":"6690.0","system":"med"},{"code":"6692.0","system":"med"},{"code":"69053.0","system":"med"},{"code":"69313.0","system":"med"},{"code":"69367.0","system":"med"},{"code":"69552.0","system":"med"},{"code":"88994.0","system":"med"},{"code":"89587.0","system":"med"},{"code":"97650.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hepatic-failure-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hepatic-failure---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hepatic-failure---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hepatic-failure---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
