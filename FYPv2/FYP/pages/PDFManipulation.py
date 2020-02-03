import re

import requests
import slate3k as slate
from bs4 import BeautifulSoup as bs
from requests import get


class PDFManipulation:
    # Get top resumé words

    # DO NOT REMOVE CODE UNDER PENALTY OF DEATH
    # =============================================

    # Load Job Description
    job_role = input("Enter your desired role: ")
    job_loc = input("Enter your desired location: ")

    url = "https://ie.indeed.com/jobs?q=" + job_role + "&l=" + job_loc
    response = get(url)
    html_soup = bs(response.text, 'html.parser')
    lists = html_soup.find_all('li').text
    print(lists)

    # ======================================================================

    resume_keywords = []

    skill_file = open('keywords.txt', 'r')
    keywords = skill_file.readlines()
    skill_file.close()

    for kw in keywords:
        resume_keywords.append(kw.upper().rstrip())

    # Resume sec3 loaded

    with open('cv-1.pdf', 'rb') as f:
        doc = slate.PDF(f)

        # Make new array
    doc_string = str(doc)
    lines = doc_string.splitlines()
    split = lines[0].split("\\n")
    split[0] = split[0].replace("['", "")
    clean_split = []
    section_split = []
    sanitised_split = []

    email = ""
    full_name = ""
    first_name = ""
    surname = ""
    address = ""
    phone_number = ""

    for s in split:
        if (s != "") and (s != " ") and (s[0] != "\\"):
            clean_split.append(s)
            sanitised_split.append(s.upper().rstrip())

    for lin in clean_split:
        # If the line is uppercase
        if lin.isupper() and lin.find(":") != -1:
            lin = ">" + lin
        else:
            pass

        section_split.append(lin.rstrip())

    # TODO: Fix Employment table

    # HOLY GRAIL OF CODE - DO NOT REMOVE UNDER PENALTY OF EXECUTION!!!

    header_count = sum(1 for x in section_split if x.find(">") != -1)

    # Load Headings and Content
    content = []
    headings = []

    file = open("cv.txt", "w+")

    for s in section_split:
        if s.find(">") == -1:
            file.write(s + "\n")
        else:
            file.write("--BLANK_LINE_DO_NOT_READ--\n" + s + "\n")
    file.close()

    # ==========================================================
    # https://ubuntuforums.org/showthread.php?t=1292871
    # ==========================================================

    # Original file to be split
    input_file = 'cv.txt'

    # Set the delimiting line for the splitter
    text_split_string = '--BLANK_LINE_DO_NOT_READ--'

    # Set the naming convention for the different sections
    file_name_format = 'section_#.txt'

    # Splitting function
    def text_splitter(self, fnf):
        # Apply the naming convention for the filename using the number passed into the function
        filename = fnf.replace('#', str(fnf))
        # Write to the file and save the file to a variable
        out = open(filename, 'w')
        # Return the variable
        return out

    # Open the master CV file
    file = open(input_file)

    # Read all lines of the file and save them to a list called lines
    lines = file.readlines()

    # File number counter
    file_number = 0
    # Save the output for the given file/section to the output file
    output = text_splitter(file_number)

    # Iterate through the lines..
    for line in lines:
        # .. And if it hits the delimiting string ..
        if text_split_string in line:
            # .. Close the output ..
            output.close()
            # Increment the file number counter
            file_number += 1
            # Write what is written at this point to the text file
            output = text_splitter(file_number)
        else:
            # Otherwise if we have not hit the delimiting string - continue writing
            output.write(line)

    # Once all sections are read and split into files stop reading the file
    output.close()

    sections = [[]]

    # Dynamically create the 2D array
    for i in range(header_count):
        sections.append([])

    # For the range of sections ...
    for i in range(0, header_count + 1):
        # ... Load the dynamically generated files ...
        filename = file_name_format.replace('#', str(i))
        # ... Open the file ...
        out = open(filename, 'r')
        # ... load the section arrays ..
        sections[i] = out.readlines()
        # .. and stop reading from the file.
        out.close()

    # For each section list in sections
    for sec in sections:
        # For each section in the section lists
        for s in sec:
            # If the section string contains "SKILLS" ...
            # if s.find("SKILLS") != -1:
            # ... Print the section
            # print(sec)
            pass

    # TODO: Load in profile information

    filter(None, sections[0])

    # Set counter to keep track of the first line
    contact_counter = 1
    # Loop through the contact information section
    for s in sections[0]:
        # If it is the first line..
        if contact_counter == 1:
            # Set the full name equal to the string
            full_name = s
            # Split the string at the first space
            names = full_name.split(" ", 1)
            # First Name is the first item of the names list
            first_name = names[0]
            # Surname is the second item on the names list
            surname = names[1].rstrip()
            # Increment the contact counter
            contact_counter += 1
        # Check for a phone number using RegEx (built my own with https://pythex.org/)
        # and check against the string that is being iterrated through
        phone_number_format = re.search("\(\+?\d*\)\d*.\d*.\d*", s)
        # Check for an email address using RegEx (built my own with https://pythex.org/)
        # and check against the string that is being iterrated through
        email_format = re.search("[^@]+@[^@]+\.[^@]+", s)

        if email_format:
            email = email_format.group()

        if phone_number_format:
            phone_number = phone_number_format.group()

    # ===========================================================
    #                       SCRAPE JOB
    # ===========================================================

    print("\n ============================== \n Job Description \n ============================== \n")

    page = requests.get("https://ie.indeed.com/viewjob?jk=01852c1f9d40fd11&tk=1dsn3d00n99p4800&from=serp&vjs=3")
    soup = bs(page.content, 'html.parser')
    job_desc = soup

    # Remove footer li's
    soup.find('div', class_='jobsearch-Footer').decompose()

    job_posting_list_elems = soup.find_all('li')

    job_posting_keywords = []
    for element in job_posting_list_elems:
        item = element
        if item:
            job_keyword = item.text.strip()
            job_posting_keywords.append(job_keyword)

    # ===========================================================
    #                       COMPARE STRINGS
    # ===========================================================

    print("\n ============================== \n Compare Strings \n ============================== \n")

    for kw in resume_keywords:
        for cv_line in sanitised_split:
            found = cv_line.find(kw)
            if found != -1:
                print(kw, " ", "Match: ", cv_line)
