import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def filter_arrays_by_prefix(string_arrays, year):
  return [string_array for string_array in string_arrays if isinstance(string_array, str) and string_array.lower().startswith(f"/programs/{year}/organizations")]


def OrgDeets(orgurl) :
        driver.get(orgurl)
        OrgDescription = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-program-organization/app-org-page-title/app-feature-banner/section/div/div/app-feature-cta/div/div[1]/div[3]/p")))
       # print(OrgDescription.text)
        OrgTechs = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-program-organization/app-org-info/section/div[2]/div/div/div[1]/div/app-org-info-details/div/div[1]/div[1]/div[2]")))
        print(OrgTechs.text)
        OrgTopics = driver.find_element(By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-program-organization/app-org-info/section/div[2]/div/div/div[1]/div/app-org-info-details/div/div[1]/div[2]/div[2]")
        print(OrgTopics.text)
        #OrgSite = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-program-organization/app-org-info/section/div[2]/div/div/div[1]/div/app-org-info-details/div/div[2]/a")))
        Orgsite = driver.find_element(By.XPATH, " /html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-program-organization/app-org-info/section/div[2]/div/div/div[1]/div/app-org-info-details/div/div[2]/a")
        print(Orgsite.text)
        try:
                divelements = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-program-organization/app-org-projects-list/section/div[2]/div[2]")))
        except TimeoutException:
                try:
                        divelements = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-program-organization/app-org-projects-list/section/div[2]/div")))
                except:
                        divelements = "nothing at all"

        soup = BeautifulSoup(driver.page_source, 'lxml')
        projdivs = soup.find_all('div', class_ = "project-card-wrapper")
        projnum = len(projdivs)
        print(projnum)
        return(OrgDescription.text, OrgTechs.text, OrgTopics.text, Orgsite.text, projnum)
        

years = {2022, 2023, 2024}
def initial_name(year):     

        url = f'https://summerofcode.withgoogle.com/programs/{year}/organizations'
        driver.get(url)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "name")))
        soup1 = BeautifulSoup(driver.page_source, 'lxml')
        tags1 = soup1.find_all("div", class_="name")
        linksoup1 = soup1.find_all("a", href=True)
        links1 = [link.get('href') for link in linksoup1 if filter_arrays_by_prefix([link.get('href')], year)]
        # for link in links1:
        #   print(link)

        btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-program-organizations/app-orgs-grid/section[2]/div/mat-paginator/div/div/div[2]/button[2]")))
        driver.execute_script('arguments[0].click()', btn)
        soup2 = BeautifulSoup(driver.page_source, "lxml")
        tags2 = soup2.find_all("div", class_="name")
        linksoup2 = soup2.find_all("a", href=True)
        links2 = [link.get('href') for link in linksoup2 if filter_arrays_by_prefix([link.get('href')], year)]
        # for link in links2:
        #   print(link)
        btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-program-organizations/app-orgs-grid/section[2]/div/mat-paginator/div/div/div[2]/button[2]")))
        driver.execute_script('arguments[0].click()', btn)
        soup3 = BeautifulSoup(driver.page_source, "lxml")
        tags3 = soup3.find_all("div", class_="name")
        linksoup3 = soup3.find_all("a", href=True)
        links3 = [link.get('href') for link in linksoup3 if filter_arrays_by_prefix([link.get('href')], year)]
        btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-program-organizations/app-orgs-grid/section[2]/div/mat-paginator/div/div/div[2]/button[2]")))
        driver.execute_script('arguments[0].click()', btn)
        soup4 = BeautifulSoup(driver.page_source, "lxml")
        tags4 = soup4.find_all("div", class_="name")
        linksoup4 = soup4.find_all("a", href=True)
        links4 = [link.get('href') for link in linksoup4 if filter_arrays_by_prefix([link.get('href')], year)]
        names = []
        links = []
        for tag in tags1:
                names.append(tag.text)
        for tag in tags2:
                names.append(tag.text)
        for tag in tags3:
                names.append(tag.text)
        for tag in tags4:
                names.append(tag.text)
        for link in links1:
                links.append(link)
        for link in links2:
                links.append(link)
        for link in links3:
                links.append(link)
        for link in links4:
                links.append(link)
                
        OrgUrls = []
        for link in links:
                OrgUrls.append(f"https://summerofcode.withgoogle.com/{link}")
        return (names, OrgUrls)
        


for year in years:
        names, links = initial_name(year)
        namesdf = pd.DataFrame(names)
        namesdf["OrgUrls"] = links
        namesdf.to_csv(f"data{year}.csv")




#Add Description, technologies, topics , org site and number of projects alotted
for year in years:
        namesdf = pd.read_csv(f'data{year}.csv')
        Orgurls = namesdf["OrgUrls"]
        description=[]
        techs =[]
        topics=[]
        site = []
        projnum = []


        for i in range(len(Orgurls)):
                desc, tech, topic, sit, num = OrgDeets(Orgurls[i])
                description.append(desc)
                techs.append(tech)
                topics.append(topic)
                site.append(sit)
                projnum.append(num)
        namesdf['Desc'] = description
        namesdf['Technologies'] = techs
        namesdf['Topic'] = topics
        namesdf['Organisation site'] = site
        namesdf['number of Projects'] = projnum

        namesdf.to_csv(f'data{year}.csv')


