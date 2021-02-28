from urllib import request
from bs4 import BeautifulSoup
import csv


url = "https://elpais.com/"

response = request.Request(url)
pagedata = request.urlopen(response)
read_html = pagedata.read()

soup = BeautifulSoup(read_html, "html.parser")

noticies = soup.select(".headline")

elpais_domain="https://elpais.com/"

with open('elpaiscom.csv', mode='w') as output_file:
    writer = csv.writer(output_file, delimiter=',', quotechar='"')
    for noticia in noticies:
        titol = noticia.get_text().strip().encode('utf-8')
        link = noticia.select('a')[0]['href']

        if link.startswith('/'):
            link = elpais_domain + link

        writer.writerow([titol,link])    
    #print(titol)
    #print(link)
    
