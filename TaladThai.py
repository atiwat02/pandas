from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
import csv
n = 0
data =[]
for i in range(2):
    url = "https://www.talaadthai.com/en/product-search/result?page="+str(i+1)+"&per_page=50&subcat_id=7310"
    options = Options()
    options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    browser = webdriver.Edge(options = options)
    browser.get(url)
    time.sleep(4)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find('div',{'class':"col-12 col-md-12 my-0 mb-sm-4"})
    t = str(a).split('data-v-52a131fa="">')
    ttt = ""
    date =""
    amount = ''
    for i in t:
        yy = '</div> <div class="d-block d-sm-none text-dark"'
        uu = '</span> <div class="d-inline-block mx-0 mx-md-2 number text-left"'
        ii = '</small></div></div></div></a></div>'
        if yy in i:
            n+=1
            # print(n,i.split(yy)[0])
            ttt+=i.split(yy)[0].replace("“","")
        if uu in i:
            if amount == "":
                amount += ''.join(i.split(uu)[0].replace(" ","").split())
                # print(ttt,*i.split(uu)[0].replace(" ","").split())
        if ii in i:
            date += i.split(ii)[0].split()[0]
            # print(n,i.split(ii)[0].split()[0])
        if ttt and amount and date:
            data.append([n,ttt,amount,date])
            # print(n,ttt,amount,date)
            ttt = ""
            date =""
            amount = ""
student_header = ['No.', 'name', 'amount','update']
with open('students.csv', 'w',encoding='UTF8') as file:
    writer = csv.writer(file)
    writer.writerow(student_header)
    # Use writerows() not writerow()
    writer.writerows(data)