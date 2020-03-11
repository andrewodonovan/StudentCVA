from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import FileResponse, Http404
from django.core.files.storage import FileSystemStorage
###########################################################################################
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.colors import black
###########################################################################################

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#================================================
#               BACKEND IMPORTS
#================================================
import re
import requests
from bs4 import BeautifulSoup as bs
import slate3k as slate
#================================================

import FYP
from pages.models import Cv, CustomUser, Education, Skills, WorkExperience
from .forms import CvForm, CvUploadForm


class CvList(ListView):
    model = Cv
    fields = ['CvName', 'CvEducation', 'CvSkills', 'CvWorkExperience']
    success_url = reverse_lazy('Cv_list')

    def get_queryset(self):
        user_ids = CustomUser.objects.filter(username=self.request.user).values_list('id', flat=True)
        if user_ids:
            for uid in user_ids:
                return Cv.objects.filter(user__id=uid)
        else:
            return Cv.objects.all()


class CvView(DetailView):
    model = Cv

class CvCreate(CreateView):
    model = Cv
    success_url = reverse_lazy('Cv_list')
    form_class = CvForm()
    exclude = ['user']

    def get_initial(self):
        self.initial.update({ 'created_by': self.request.user.id })
        return self.initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CvCreate, self).form_valid(form)

    def get_queryset(self):
        user_ids = CustomUser.objects.filter(username=self.request.user).values_list('id', flat=True)
        if user_ids:
            for uid in user_ids:
                return Cv.objects.filter(user__id=uid)
        else:
            return Cv.objects.all()


class CvUpdate(UpdateView):
    model = Cv
    form_class = CvForm
    success_url = reverse_lazy('Cv_list')


class CvDelete(DeleteView):
    model = Cv
    success_url = reverse_lazy('Cv_list')

#==================================================================================================
# https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
#==================================================================================================

@login_required
def simple_upload(request):
    form = CvUploadForm(request.POST or None, request.FILES)
    if form.is_valid():
        if request.method == 'POST' and request.FILES['cv_file']:
                cv_file = request.FILES['cv_file']
                fs = FileSystemStorage()
                filename = fs.save(cv_file.name, cv_file)
                return pdf_view(request)




    return render(request, 'pages/cvupload.html', {'form':form})


#======================================================================================
#   https://stackoverflow.com/questions/4576077/how-to-split-a-text-into-sentences
#======================================================================================
import re
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "~" in text: text = text.replace("~\"", "\"~")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    if ":" in text: text = text.replace(":\"", "\":")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace(":", ":<stop>")
    text = text.replace("~", "~<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

@login_required
def pdf_view(request):
    cv_file = request.FILES['cv_file']
    cv_name = request.POST['cv_name']

    if cv_file:
        fs = FileSystemStorage()
        file_name = cv_file.name

        f = fs.open(file_name)

        doc = slate.PDF(f)

            # Make new array
        doc_string = str(doc)

        ln = []
        lines = []
        ln = split_into_sentences(doc_string)

        section_split = []
        sanitised_split = []


        for l in ln:
            l = l.replace("\\n\\n", "")
            l = l.replace("\\n ", "")
            # If the line is uppercase
            if l.isupper() and l.find(":") != -1:
                l = ">" + l
            else:
                pass

            section_split.append(l.rstrip())

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

        for sec in sections:
            for s in sec:
                s = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', s)
            sec = sec

        for sec in sections:
            for s in sec:
                s = s.replace("\\n", "")
            sec = sec

        for sec in sections:
            for s in sec:
                s = str(s)
                s = s.replace("\n", "")
            sec = sec

        for sec in sections:
            for s in sec:
                s = str(s)
                s = s.replace("\[\'", "")
            sec = sec

        for sec in sections:
            for s in sec:
                s = str(s)
                s = s.replace("\.", "")
            sec = sec


        request.session['sections'] = sections
        request.session['sec_count'] = header_count


        context = {
            'cv_path': file_name,
            'cv_name':cv_name,
            'sections': sections,
            'sec_count': header_count
        }


    return render(request, 'pages/cv-display.html', context)



# Set the naming convention for the different sections
file_name_format = 'section_#.txt'

# Splitting function
def text_splitter(fn):
    # Apply the naming convention for the filename using the number passed into the function
    filename = file_name_format.replace('#', str(fn))
    # Write to the file and save the file to a variable
    out = open(filename, 'w')
    # Return the variable
    return out

@login_required
def create_cv_pdf(request):
    user = request.user
    tm = str(datetime.now())
    tm = tm.replace(" ", "")
    tm = tm.replace(":", "-")
    tm = tm.replace(".", "-")

    fn = "Outputted_CV" + "--" + str(user.username) + "--" + tm + ".pdf"

    path = "/tmp/Outputted_CV-" + "--" + str(user.username) + "--" + tm + ".pdf"
    doc = SimpleDocTemplate(path)
    styles = getSampleStyleSheet()
    Story = [Spacer(-1,-1*inch)]
    style = styles["Normal"]
    sections = request.session['sections']
    sec_count = request.session['sec_count']

    for sec in sections:
        for s in sec:
            s = re.sub(r"\x0c","",s)
        sec = sec

    for sec in sections:
        for s in sec:
            s = s.replace("\\n", "")
        sec = sec

    for sec in sections:
        for s in sec:
            s = str(s)
            s = s.replace("\n", "")
        sec = sec

    for sec in sections:
        for s in sec:
            s = str(s)
            s = s.replace("\[\'", "")
        sec = sec

    for sec in sections:
        for s in sec:
            s = str(s)
            s = s.replace("\.", "")
        sec = sec

    for sec in sections:
        for s in sec:
            s = str(s)



    personal = sections[0]

    head = []
    for p in personal:
        p = p.replace("['", "")
        p = p.replace("~", "")

        head.append(p)

    title_style = styles['Heading2']
    title_style.alignment = 1
    title = Paragraph(head[0], title_style)
    Story.append(title)
    styles.add(ParagraphStyle(name='email',
                              fontFamily='Helvetica',
                              fontSize=9,
                              textColor=colors.HexColor("#0000FF")))

    styles.add(ParagraphStyle(name='sub-heading',
                              fontFamily='Helvetica',
                              fontSize=9,
                              textColor=colors.HexColor("#404040")))

    styles.add(ParagraphStyle(name='cv-heading',
                              fontFamily='Helvetica-Bold',
                              fontSize=10,
                              textColor=colors.HexColor("#000000")))
    styles.add(ParagraphStyle(name='cv-body',
                              fontFamily='Helvetica',
                              fontSize=9.5,
                              textColor=colors.HexColor("#000000")))
    styles.add(ParagraphStyle(name='p-statement',
                              fontFamily='Helvetica',
                              fontSize=9,
                              textColor=colors.HexColor("#222222")))

    for h in head:
        if h != head[0]:
            if h.find("@") != -1 and h.find(".") != -1:

                sub_title_style = styles['email']
                sub_title_style.alignment = 1
                sub_title = Paragraph("<a href=\"mailto:"+ h + "\"><i>" + h + "</i></a>", sub_title_style)
                Story.append(sub_title)
                continue


            sub_title_style = styles['sub-heading']
            sub_title_style.alignment = 1
            sub_title = Paragraph("<i>" + h + "</i>", sub_title_style)
            Story.append(sub_title)

    p_sec_text = ""
    p_count = 0
    for i in range(1, sec_count):
        for sec in sections[i]:
            if sec in sections[1]:
                if sec.isupper() and sec.find(":"):
                    continue
                else:
                    p_sec_text += sec

    for i in range(1, sec_count):
        for sec in sections[i]:

            if sec.find(">") != -1 and sec.find(":"):
                sec = sec.replace(">", "")
                cv_heading_style = styles['cv-heading']
                cv_heading_style.alignment = 0
                cv_heading = Paragraph("<b>" + sec + "</b>", cv_heading_style)
                Story.append(cv_heading)
                continue

            if sec in sections[1]:
                if sec.isupper() and sec.find(":"):
                    continue
                else:

                    if p_count < 1:
                        p_statement_style = styles['p-statement']
                        p_statement_style.alignment = 1
                        p_statement = Paragraph("<i>" + p_sec_text + "</i>", p_statement_style)
                        Story.append(p_statement)
                        p_count += 1
                    continue

            if sec.find("~") != -1:
                sec = sec.replace("~", "")
                sec = sec.replace("\\n\\x0c', '", "")
                cv_body_style = styles['cv-body']
                cv_body_style.alignment = 0
                p = Paragraph(sec, cv_body_style)
                Story.append(p)
                Story.append(Spacer(0.05,0.05*inch))
                continue

            sec = sec.replace("~", "")
            sec = re.sub(r"\x0c","",sec)
            cv_body_style = styles['cv-body']
            cv_body_style.alignment = 0
            p = Paragraph(sec, cv_body_style)
            Story.append(p)
            Story.append(Spacer(0.05, 0.05 * inch)) 
        Story.append(Spacer(0.1,0.1*inch))
    doc.build(Story)

    fs = FileSystemStorage("/tmp")
    with fs.open(path) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = "attachment; filename=\"" + fn + "\""
        return response
    request.session.delete()
    return response
