
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
        company.append(line[x])
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
                
        last = profile[-1]

        correct_last = profile[-1]

        if correct_last.find("Manufacturer"):
            correct_last = correct_last[:correct_last.find("Manufacturer") - 2]

        if correct_last.find("Distributor"):
            correct_last = correct_last[:correct_last.find("Distributor") - 2]

        profile[-1] = correct_last

        fake_csv += "\"" + "".join(profile) + "\","

        print(profile)

        company.append(profile)
        x += 1

        if len(profile) == 0:
            print("NO PROFILE")
            for s in company[3]:
                print(s)

                
        ########


        print("\t\t\t$$ MANUfacturer $$ ")
        manufacturer = []


        ld = last.find("Distributor")
        lf = last.find("Manufacturer")

        if ld:
            manufacturer.append(last[ld::])
        else:
            manufacturer.append(last[lf::])
            
            
        
        # read manufacturer of
        
        match = re.search("Others:", line[x])
        while not match:
            manufacturer.append(line[x])
            #print(x, " ", manufacturer)
            x += 1
            match = re.search("Others:", line[x])
            
        x += 1

        company.append(manufacturer)
        fake_csv += "\"" + "".join(manufacturer) + "\","

        for s in company[4]:
            print(s)

       
        ## read applications
        applications = []

        print("\t\t\t$$ APPPLICATIONS $$$")
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

        # with open("job.csv", "a") as fh:
        #     fh.writelines(fake_csv)

        company.clear()

        break

        print("%%% FAKE CSV: %%%\n\n", fake_csv, "\n%%%%\n\n")

        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        #break
        
    line.clear()

               
        # print("\n\n###\n")
        # print_data(company)
        # print("\n####\n")








