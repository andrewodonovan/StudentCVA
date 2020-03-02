# My PDF manipulation library
import re

from bs4 import BeautifulSoup as bs
import slate3k as slate

# Get top resumé words


# Load Job Description
import requests
from django.shortcuts import render
from requests import get


def find_job(request):
    #c = "https://ie.indeed.com/viewjob?jk=3f71b264fdd44b34&q=python+developer&l=cork&tk=1e2dov7fl9mh3800&from=web&advn=3190066218131062&adid=336474481&sjdu=EJysIw7ZxQWtrbe43k-UVdQpuy0HosYrBqVYOuAwS4in1r8WZcml6yF7Ks_t9GoNDBUta3C9agvu4QsQqSBVaJAvfJUiDn6mqiE9cqx1pZicQIVCHhYEeeT0YMgeMv08akp8iDu6JdC7-bhWEDpMJA&acatk=1e2dp27qj9hp3800&pub=4a1b367933fd867b19b072952f68dceb&vjs=3"
    # TODO: Implement Linking
    # https://ie.indeed.com/viewjob?jk=
    # TODO: Show HTML links
    job_role = input("Enter your desired role: ")
    job_loc = input("Enter your desired location: ")

    url = "https://ie.indeed.com/jobs?q=" + job_role + "&l=" + job_loc
    response = get(url)
    html_soup = bs(response.text, 'html.parser')
    role_search = html_soup.findAll("a", class_="jobtitle")
    company_search = html_soup.findAll("span", class_="company")

    roles = []
    companies = []

    number_of_roles = 0
    number_of_companies = 0

    job_ids = []

    for r in role_search:
        r = r.getText()
        roles.append(str(r))
        number_of_roles += 1

    job_posting = [] * number_of_roles

    for c in company_search:
        c = c.getText()
        companies.append(str(c))
        number_of_companies += 1

    for u in company_search:
        u = str(u)
        if u.find("jk=") != -1:
            s_point = u.find("jk=")
            e_point = s_point + 16
            job_id = u[s_point:e_point]
            job_ids.append(job_id)



    for i in range(1, number_of_roles):
        c_strip = companies[i].rstrip("\\n")
        r_strip = roles[i].lstrip()
        job_header = c_strip.rstrip() + " - " + r_strip.lstrip()
        job_posting.append(job_header.lstrip())

    posting = list(job_posting)
    jobkeys = list(job_ids)

    context = {
        'posting': posting,
        'jobkeys': job_ids

    }

    return render(request, 'jobs/jobs.html', context)

# find_job(self=None)