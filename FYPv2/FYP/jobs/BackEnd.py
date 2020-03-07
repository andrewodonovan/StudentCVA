# My PDF manipulation library
import re

from bs4 import BeautifulSoup as bs
import slate3k as slate

# Get top resumé words


# Load Job Description
import requests
from requests import get





# TODO: Implement Linking
# https://ie.indeed.com/viewjob?jk=
# TODO: Show HTML links
# #======================================================================
#
#
# resume_keywords = []
#
# skill_file = open('keywords.txt', 'r')
# keywords = skill_file.readlines()
# skill_file.close()
#
# for kw in keywords:
#     resume_keywords.append(kw.upper().rstrip())
#
# # Resume sec3 loaded
#
with open('cv-1.pdf', 'rb') as f:
    doc = slate.PDF(f)
#

# # ===========================================================
# #                       SCRAPE JOB
# # ===========================================================
#
# print("\n ============================== \n Job Description \n ============================== \n")
#
# page = requests.get("https://ie.indeed.com/viewjob?jk=01852c1f9d40fd11&tk=1dsn3d00n99p4800&from=serp&vjs=3")
# soup = bs(page.content, 'html.parser')
# job_desc = soup
#
# # Remove footer li's
# soup.find('div', class_='jobsearch-Footer').decompose()
#
# job_posting_list_elems = soup.find_all('li')
#
# job_posting_keywords = []
# for element in job_posting_list_elems:
#     item = element
#     if item:
#         job_keyword = item.text.strip()
#         job_posting_keywords.append(job_keyword)
#
# # ===========================================================
# #                       COMPARE STRINGS
# # ===========================================================
# def compare_strings(keywords, sanitised):
#     print("\n ============================== \n Compare Strings \n ============================== \n")
#     matches = []
#     for kw in resume_keywords:
#         for cv_line in sanitised_split:
#             found = cv_line.find(kw)
#             if found != -1:
#                 print(kw, " ", "Match: ", cv_line)
#                 matches.append(cv_line)
#                 return matches
