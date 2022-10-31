
import PyPDF2 as pdf
import re

def print_data(data):
    for d in data:
        print("$ ", data, " $")

file = pdf.PdfReader("job.pdf")



page_min = 142
page_max = 239


# company, location, website, company profile, fittings, pipes, application




#lines = page.extractText().split("\n")

#lines.pop(0)

last_line = ""

company = []

cmin, cmax = 153, 154

for x in range(cmin, cmax):
    page = file.getPage(x)
    l = 0
    for line in page.extractText().split("\n"):
        print(l, ":", line)
        l += 1

print("\n\n#####\n\n")


for c in range(cmin, cmax):

    fake_csv = ""
    
    page = file.getPage(c)

    line = page.extractText().split("\n")
    # remove garbage
    line.pop(0)

    print("Page: %d Size: %d" % (c, len(line)))

    x = 0
    while x < len(line):


        print("\t\t\t$$ NEW COMPANY $$")
        #read company name
        company.append(line[x])
        #print_data(company)
        print(company)
        print(company[0])
        x += 1

        fake_csv += "\"" + company[0].strip() + "\"" +  ","


        # read location

        location = ""
        
        match = re.search("www|\.com", line[x])
        while not match:
            location += line[x] + "\n"
            x += 1
            match = re.search("www|\.com", line[x])

        company.append(location)
        fake_csv += "\"" + company[1].strip() + "\"" +  ","
        print("\t\t\t$$ LOCATION: $$")
        for l in location.split("\n"):
            print(l)
#        print_data(company)

        # read email

        correct_email = re.search(r"Manufacturer|Distributor|Pipe", line[x], re.IGNORECASE)
        
        email = line[x]

        orig_email = email[:]
        
        if email.lower().find("manufacturer"):
            email = email[:email.lower().find("manufacturer")]

        if email.lower().find("distributor"):
            email = email[:email.lower().find("distributor")]

        if email.lower().find("pipe"):
            email = email[:email.lower().find("pipe")]

                        
        company.append(email)
        fake_csv += "\"" + company[2].strip() + "\"" +  ","
       # print_data(company)

        x += 1

        print("\t\t\t$$ EMAIL: $$")
        print(company[2])


        match = re.search(r'^Company', line[x])
  #      print("checking line: ", line[x])


    
        profile = []
                    
        if match:
#            print("MATCH TRUE")
            x += 1

            print("\t\t\t$$ PROFILE  $$ ")
            # read company profile

            match = re.search(r"Manufacturer of:|Distributor of:", line[x], re.IGNORECASE)
            while not match:
                profile.append(line[x])
                #print(x, " ", profile)
                x += 1
                match = re.search(r"Manufacturer of:|Distributor of:", line[x], re.IGNORECASE)

            profile.append(line[x])

        if len(profile) > 0:
            last = profile[-1]
            correct_last = profile[-1]

            if correct_last.lower().find("Manufacturer"):
                correct_last = correct_last[:correct_last.lower().find("Manufacturer") - 2]

            if correct_last.lower().find("Distributor"):
                correct_last = correct_last[:correct_last.lower().find("Distributor") - 2]

            profile[-1] = correct_last

            fake_csv += "\"" + "".join(profile) + "\","

            print(profile)

            company.append(profile)

            if len(profile) == 0:
                print("NO PROFILE")
                for s in company[3]:
                    print(s)

        else:
            company.append([" "])
            fake_csv += "\" \","
            x += 1

#        x += 1

        ########


        print("\t\t\t$$ MANUfacturer $$ ")
        manufacturer = []


        if len(profile) > 0:
            ld = last.find("Distributor")
            lf = last.find("Manufacturer")

            if ld:
                manufacturer.append(last[ld::])
            else:
                manufacturer.append(last[lf::])

        if correct_email:
            if orig_email.lower().find("manufacturer"):
                 orig_email = orig_email[:orig_email.lower().find("manufacturer")]

            if orig_email.lower().find("distributor"):
                orig_email = orig_email[:orig_email.lower().find("distributor")]

            if orig_email.lower().find("pipe"):
                orig_email = orig_email[:orig_email.lower().find("pipe")]


                    
        # read manufacturer of
        
        match = re.search("Others:", line[x])
        while not match:
            manufacturer.append(line[x])
            #print(x, " ", manufacturer)
            x += 1
            match = re.search("Others:", line[x])
            
        #x += 1

        company.append(manufacturer)
        fake_csv += "\"" + "".join(manufacturer) + "\","

        print("COMAPNY SIZE: ", len(company))
        for s in company[4]:
            print(s)

       
        ## read applications
        applications = []

        print(" HOPE FOR ACCPLICATION: ", line[x])

        match = re.match("application", line[x], re.IGNORECASE)
    
        x += 1


        
        print("LINEXXX : ", line[x])
        print("\t\t\t$$ APPPLICATIONS $$$")
        if match:
            match = re.search(r"www|\.com", line[x])
            while not match:
                applications.append(line[x])
                x += 1
                match = re.search(r"www|\.com", line[x] )

            if len(line) - ( x + 2) >= 2:
                applications.pop()
                applications.pop()
                x -= 2
            else:
                x += 1
                        
            company.append(applications)
            fake_csv += "\"" + "".join(applications) + "\""
            for s in applications:
                print(s)
        else:
            fake_csv += "\" \""

        # with open("job.csv", "a") as fh:
        #     fh.writelines(fake_csv)

        company.clear()


        print("%%% FAKE CSV: %%%\n\n", fake_csv, "\n%%%%\n\n")

        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        #break
        
    line.clear()

               
        # print("\n\n###\n")
        # print_data(company)
        # print("\n####\n")








