from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
import csv

url = "https://www.taladsrimuang.com/site/product/report_all.php"
options = Options()
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
browser = webdriver.Edge(options = options)
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
a = soup.find('body')
w = soup.find('div',{'class':"box_se_time_de"})
date = str(str(w).split('<br/>')[1].split('</span>')[0])
t = str(a).split('</td>')
n =0
name = ""
amount = ""
data = []
for i in t:
    yy = '<tr><td style="padding: 0 0 0 80px;">'
    uu = '<td style="text-align: center;">'
    if yy in i:
        n+=1
        name = str(i.split(yy)[1].split('<span class="blank_th">')[1].split('</span>')[0])
        # print(i.split(yy)[1].split('<span class="blank_en">')[1].split('</span>')[0])
    if uu in i:
        amount += str(i.split(uu)[1].split('<span class="blank_th">')[1].split('</span>')[0].split()[0])
        # print(*i.split(uu)[1].split('<span class="blank_en">')[1].split('</span>')[0].split())
    if(name and amount):
        data.append([n,name,amount,date])
        # print(n,name,amount,date)
        name = ""
        amount = ""
student_header = ['No.', 'name', 'amount','update']
with open('students.csv', 'w',encoding='UTF8') as file:
    writer = csv.writer(file)
    writer.writerow(student_header)
    # Use writerows() not writerow()
    writer.writerows(data)