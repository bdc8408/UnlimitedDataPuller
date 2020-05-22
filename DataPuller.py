import PyPDF2 as pdf
import os

print(pdf.__version__)

reader = pdf.PdfFileReader('..\ExportedReport.pdf')

pages = []

numPages = reader.numPages

tags = []

plans = ["Unlimited","Family Plan*"]
i = 0

while i < numPages:
    curPage = reader.getPage(i)

    txt = curPage.extractText()


    pages.append(txt)

    i+=1

i = 0
j = 0
while i < numPages:
    j = 0
    while j < len(plans):
        txt = pages[i]
        curPlan = plans[j]

        datStart = txt.find("Salesperson")

        txt = txt[datStart:len(txt)]
        planLoc = 0

        while planLoc != -1:

            planLoc = txt.find(curPlan)

            tagLoc = planLoc + len(plans[j])

            txt = txt[planLoc:len(txt)]

            tagEnd = txt.find("/")

            tag = txt[0+len(plans[j]):tagEnd]

            tags.append(tag)

            txt = txt[0+len(plans[j])+len(tag):len(txt)]


        j+=1
    i+=1

tagfile = open(r"..\Tags to Email.txt","w")

i = 0
while i < len(tags):
    tagfile.write(tags[i])
    tagfile.write("\n")
    i+=1

tagfile.close()


print(tags)