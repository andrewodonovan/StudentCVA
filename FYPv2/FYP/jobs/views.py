# My PDF manipulation library
from bs4 import BeautifulSoup as bs
# Load Job Description
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from requests import get

from .forms import JobForm


# import FYP
# from pages.models import Job, CustomUser
# Get top resumé words
# ===============================================================
# https://docs.djangoproject.com/en/3.0/topics/forms/
# ===============================================================

@login_required
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

@login_required
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
    comps_for_logo = []
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

    for c in companies:
        c = c.rstrip("\\n")
        comps_for_logo.append(c.rstrip())

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

    # ===========================================================================================
    #   Found Zipping Here:
    #   https://stackoverflow.com/questions/32226716/multiple-for-loop-in-django-template
    # ===========================================================================================
    jobs = zip(posting, jobkeys, comps_for_logo)

    context = {
        'jobs': jobs
    }

    return render(request, 'jobs/jobs.html', context)

@login_required
def keywords(request, key):

    try:
        sections = request.session['sections']

        url = "https://ie.indeed.com/viewjob?jk=" + key
        response = get(url)
        html_soup = bs(response.text, 'html.parser')
        html_soup.find('div', class_='jobsearch-Footer').decompose()
        indeed_search = html_soup.findAll("li")

        resume_url = "https://www.jobscan.co/blog/top-resume-keywords-boost-resume/"
        resp = get(resume_url)
        res_soup = bs(resp.text, 'html.parser')
        res_soup.find('div', class_='mt-container').decompose()
        res_soup.find('div', class_='mt-footer-widget-wrapper').decompose()
        res_search = res_soup.findAll("li")

        res_kw = []
        for r in res_search:
            r1 = r.getText()
            res_kw.append(r1)

        indeed_search_keywords = []
        kw = []
        for i_s in indeed_search:
            i_s1 = i_s.getText()
            indeed_search_keywords.append(i_s1)

            request.session['indeed_search_keywords'] = indeed_search_keywords
            request.session['online_res_keywords'] = res_kw

        context = {
            'keywords': indeed_search_keywords,
            'sections': sections,
            'res_kws': res_kw
        }

        return redirect('matches')
    except:
        messages.add_message(request, messages.ERROR,'Please Upload a CV before creating a tailored CV')
        return redirect('upload_cv')


    return render(request, 'jobs/keywords.html', context)

@login_required
def compare_strings(request):
    context = {}
    if request.method == 'POST':
        try:
            sections = request.session['sections']
            indeed_search_keywords = request.session['indeed_search_keywords']
            online_res_keywords = request.session['online_res_keywords']

            res_matches = []
            matches = []
            for r in online_res_keywords:
                for kw in indeed_search_keywords:
                    found = kw.find(r)
                    if found != -1:
                        res_matches.append(r)

            if len(res_matches) < 1:
                print("No matches")

            for r in res_matches:
                for secs in sections:
                    for section_line in secs:
                        found = section_line.find(r)
                        if found != -1:
                            matches.append(section_line)


            if len(matches) < 1:
                print("No matches")

            context = {
                'res_matches': res_matches,
                'matches': matches
            }

            request.session['matches'] = matches

            return redirect('create-cv')

        except:
            messages.add_message(request, messages.INFO, 'Please Upload a CV before searching jobs')
            return redirect('upload_cv')



    return redirect('create-cv')
