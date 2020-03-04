# My PDF manipulation library
import re

from bs4 import BeautifulSoup as bs
import slate3k as slate

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# import FYP
# from pages.models import Job, CustomUser

# Get top resumé words


# Load Job Description
import requests
from django.shortcuts import render, redirect
from requests import get

from django.http import HttpResponseRedirect
from django.shortcuts import render


#===============================================================
# https://docs.djangoproject.com/en/3.0/topics/forms/
#===============================================================


from .forms import JobForm


def job_search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = JobForm(request.POST)
        if form.is_valid():
            return redirect('display-jobs')
    else:
        form = JobForm()
    return render(request, 'jobs/job-search.html', {'form': form})

def display_jobs(request):
    job_role = request.POST['job_role']
    job_loc = request.POST['job_location']
    url = "https://ie.indeed.com/jobs?q=" + job_role + "&l=" + job_loc
    response = get(url)
    html_soup = bs(response.text, 'html.parser')
    role_search = html_soup.findAll("a", class_="jobtitle")
    company_search = html_soup.findAll("span", class_="company")
    url_search = html_soup.findAll("div", class_="jobsearch-SerpJobCard")

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

    for u in url_search:
        u = str(u)
        if u.find("jk=") != -1:
            pt = u.find("jk=")
            s_point = pt + 4
            e_point = s_point + 16
            job_id = u[s_point:e_point]
            job_ids.append(job_id)

    for i in range(0, number_of_roles):
        c_strip = companies[i].rstrip("\\n")
        r_strip = roles[i].lstrip()
        job_header = c_strip.rstrip() + " - " + r_strip.lstrip()
        job_posting.append(job_header.lstrip())

    posting = list(job_posting)
    p_c = 0
    for p in job_posting:
        p_c += 1

    jobkeys = list(job_ids)

    k_c = 0
    for k in job_ids:
        k_c += 1

    #===========================================================================================
    #   Found Zipping Here:
    #   https://stackoverflow.com/questions/32226716/multiple-for-loop-in-django-template
    # ===========================================================================================
    jobs = zip(posting, jobkeys)

    context = {
        'jobs': jobs
    }

    return render(request, 'jobs/jobs.html', context)

# find_job(self=None)
