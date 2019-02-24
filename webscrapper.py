
# coding: utf-8

# In[49]:


import requests
from bs4 import BeautifulSoup
r=requests.get("https://find-an-architect.architecture.com/FAAPractices.aspx?display=50")
c=r.content
soup=BeautifulSoup(c,"html.parser")
all = soup.find_all("article",{"class":"listingItem listingItem-faaPractice listingItem-withThumbnail"})


# In[86]:


l=[]
base_url="https://find-an-architect.architecture.com/FAAPractices.aspx?display=50&page="
for page in range(0,400,10):
    print(base_url+str(page))
    r=requests.get(base_url+str(page))
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("article",{"class":"listingItem listingItem-faaPractice listingItem-withThumbnail"})
    for item in all:
        d={}
        d["Business Name"]=item.find("h3").text
        d["Phone Number"]=item.find("div",{"class":"pageMeta-item icon"}).text.replace("Tel: ","")
        try:
            d["Address"]=item.find("div",{"class":"pageMeta-item icon address"}).text.replace("\n"," ")
        except:
            d["Address"]=None
        try:
            d["Email"]=item.find("a",{"class":"tagList faaemail"}).text
        except:
            d["Email"]=None

        try:
            d["Website"]=item.find("a",{"class":"tagList exLink"}).text
        except:
            d["Website"]=None
        l.append(d)
    


# In[89]:


import pandas
df=pandas.DataFrame(l)
df.to_csv("architrcture.csv")


# In[82]:



    

