
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
    page = file.getPage(c)

    line = page.extractText().split("\n")
    # remove garbage
    line.pop(0)

    print("Page: %d Size: %d" % (c, len(line)))

    x = 0
    while x < len(line):
        
        #read company name
        company.append(line[x])
        print_data(company)
        x += 1

        # read location
        company.append(line[x])
        print_data(company)
        x += 1

        # read email
        company.append(line[x])
        print_data(company)
        x += 2

        print("$$ PROFILE  $$ ")
        # read company profile
        profile = []
        match = re.search("Manufacturer of:", line[x], re.IGNORECASE)
        while not match:
            profile.append(line[x])
            #print(x, " ", profile)
            x += 1
            match = re.search("Manufacturer of:", line[x], re.IGNORECASE)

        
        #print(profile)
        profile.append(line[x])
        company.append(profile)
        x += 1


        for s in company[3]:
            print(s)


        print("$$ MANUfacturer  $$ ")
        manufacturer = []
        # read manufacturer of
        match = re.search("Others:", line[x])
        while not match:
            manufacturer.append(line[x])
            #print(x, " ", manufacturer)
            x += 1
            match = re.search("Others:", line[x])
            
        x += 1

        company.append(manufacturer)

        print("")
        for s in company[4]:
            print(s)

       

        ## read applications
        applications = []

        print("$$ APPPLICATIONS $$$")
        match = re.search("www", line[x])
        while not match:
            applications.append(line[x])
            x += 1
            match = re.search("www", line[x] )

        if len(line) - ( x + 2) >= 2:
            applications.pop()
            applications.pop()
            x -= 2
        else:
            x += 1
                        
        company.append(applications)
        
        print("")
        for s in applications:
            print(s)

        company.clear()

        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        
    line.clear()

               
        # print("\n\n###\n")
        # print_data(company)
        # print("\n####\n")








