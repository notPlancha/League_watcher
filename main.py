#You gotta download a chrome driver here: https://sites.google.com/a/chromium.org/chromedriver/downloads
#I did it with ChromeDriver 84.0.4147.30, but it should work with any
#Also you need install selenium (https://pypi.org/project/selenium/)
#If you need anything else, need help, have suggestions or feedback or just wanna talk, hit me up
#Discord: notPlancha#1634, Reddit:u/notPlancha, Twiiter: @notplancha, email:notPlancha@gmail.com
#Idk how github really works, so if you really need something I recommend you message me anywhere else. Still you can do whatever, I don't care
#One last thing. If there's a new champion, just add it to the list anywhere.
webdriver_path = "write here your webdriver path here" #Example: "C:/Users/me/Desktop/chromedriver.exe"
champions = ['aatrox', 'ahri', 'akali', 'alistar', 'amumu', 'anivia', 'annie', 'aphelios', 'ashe', 'aurelion sol', 'azir', 'bard', 'blitzcrank', 'brand', 'braum', 'caitlyn', 'camille', 'cassiopeia', "cho'gath", 'corki', 'darius', 'diana', 'dr. mundo', 'draven', 'ekko', 'elise', 'evelynn', 'ezreal', 'fiddlesticks', 'fiora', 'fizz', 'galio', 'gangplank', 'garen', 'gnar', 'gragas', 'graves', 'hecarim', 'heimerdinger', 'illaoi', 'irelia', 'ivern', 'janna', 'jarvan iv', 'jax', 'jayce', 'jhin', 'jinx', "kai'sa", 'kalista', 'karma', 'karthus', 'kassadin', 'katarina', 'kayle', 'kayn', 'kennen', "kha'zix", 'kindred', 'kled', "kog'maw", 'leblanc', 'lee sin', 'leona', 'lillia', 'lissandra', 'lucian', 'lulu', 'lux', 'malphite', 'malzahar', 'maokai', 'master yi', 'miss fortune', 'mordekaiser', 'morgana', 'nami', 'nasus', 'nautilus', 'neeko', 'nidalee', 'nocturne', 'nunu', 'olaf', 'orianna', 'ornn', 'pantheon', 'poppy', 'pyke', 'qiyana', 'quinn', 'rakan', 'rammus', "rek'sai", 'renekton', 'rengar', 'riven', 'rumble', 'ryze', 'sejuani', 'senna', 'sett', 'shaco', 'shen', 'shyvana', 'singed', 'sion', 'sivir', 'skarner', 'sona', 'soraka', 'swain', 'sylas', 'syndra', 'tahm kench', 'taliyah', 'talon', 'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twisted fate', 'twitch', 'udyr', 'urgot', 'varus', 'vayne', 'veigar', "vel'koz", 'vi', 'viktor', 'vladimir', 'volibear', 'warwick', 'wukong', 'xayah', 'xerath', 'xin zhao', 'yasuo', 'yorick', 'yuumi', 'zac', 'zed', 'ziggs', 'zilean', 'zoe', 'zyra']


from tkinter import *
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support.ui import WebDriverWait

def wait_for_element(driver, max_time_waiting, xpath):
    try:
        element = WebDriverWait(driver, max_time_waiting).until(cond.presence_of_element_located((By.XPATH, xpath)))
        return element
    except (NoSuchElementException, TimeoutException):
        return None

def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    else:
        return True

def open_new_tab(driver):#Doesn't work headless
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

def wait_to_click(element, shutdown_time):
    for i in range(shutdown_time):
        try:
            element.click()
            return
        except ElementNotInteractableException:
            time.sleep(1)
            continue
    raise ElementNotInteractableException


#start driver
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path= webdriver_path, options= chrome_options)
driver.maximize_window()

#driver.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")
#champion_xpath = "//table[@class='wikitable sortable jquery-tablesorter']//tbody//*[contains(@style, 'text-align:left;')]"
#champion_elements_list = driver.find_elements_by_xpath(champion_xpath)
#for i in champion_elements_list:
#    champions.append((i.get_attribute("data-sort-value")).lower())
championEntry = Tk()
champion = Entry(championEntry, borderwidth=2)
champion.pack()
button_clicked = False
def close():
    global button_clicked
    button_clicked = True
def closetwo(event):
    close()
button = Button(championEntry, text="submit", command=close).pack()
champion_input = False
championEntry.bind('<Return>', closetwo)
while champion_input == False:
    while not button_clicked:
        championEntry.update()
    champion_input = champion.get()
    if champion_input.lower() not in champions:
        champion_input = False
        button_clicked = False
        Label(championEntry, text="Please enter valid champion").pack()
    else:
        champion = champion_input
        championEntry.destroy()
root = Tk()
def removespaces(string):
    returnstr = ""
    for i in string:
        if string != " ":
            returnstr += i
    return returnstr

def write(text, column, row, letters=True):
    if not letters:
        textit = (''.join(filter(str.isdigit, text)))
        if "," in text:
            text = textit
        elif "%" in text:
            if len(textit) in [3, 4]:
                text = (str(int(textit)/100)) + "%"
            elif len(textit) == 2:
                text = (str(int(textit)/10)) + "%"
    text = removespaces(text)
    label = Label(root, text= text)
    label.grid(column = column, row = row)
    root.update()


colums = {
    "champion" : 0,
    "u.gg": 1,
    "lolalytics":2,
    "leagueofgraphs":3,
}

rows = {
    "champion": 0,
    "winrate": 1,
    "pickrate": 2,
    "banrate": 3,
    "matches": 4,
}


for i in colums:
    if i == "champion":
        write(champion, 0, 0)
    else:
        write(i, colums[i], 0)

for i in rows:
    if i == "champion":
        pass
    else:
        write(i, 0, rows[i])





xpaths = {
    "ugg": {
        "cookies" : "//button[contains(text(),'I do not accept')] ",
        "champion_input" : "//div[@class='search-container']//input[@id='super-search-bar']",
        "search" : "//div[@class='search-container']//div[@class='autosuggest-button']",
        "champion" : "//div[@class='champion-title-init']//span[@class='champion-name']",
        "winrate": "//div[@class='win-rate meh-tier']//div[@class='value']",
        "pickrate": "//div[@class='pick-rate']//div[@class='value']",
        "banrate": "//div[@class='ban-rate']//div[@class='value']",
        "matches": "//div[@class='matches']//div[@class='value']",
        #"tier": "",
        #"mainrole":"//div[contains(@class,'DESKTOP_LARGE ')]//div[contains(@class,'role-filter active')]",
        #"tierlist":"//span[contains(text(),'LoL Tier List')]",
    },
    "lolalytics": {
        "winrate": "/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[4]/div[4]/div[1]",
        "pickrate":"/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[4]/div[4]/div[4]",
        "banrate": "/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[4]/div[4]/div[5]",
        "matches": "/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[4]/div[4]/div[6]",
    },
    "leagueofgraphs":{
        "winrate": "/html[1]/body[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]",
        "pickrate":"/html[1]/body[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]",
        "banrate": "/html[1]/body[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]",
        "matches": "//span[@id='matchesCountNumber']",
    }
}
#u.gg



driver.get("https://u.gg/lol/champions/%s/build"%(champion.lower()))
element = wait_for_element(driver, 10, xpaths["ugg"]["cookies"])
wait_to_click(element, 10)
[write(driver.find_element_by_xpath(xpaths["ugg"][i]).text, colums["u.gg"], rows[i])
 for i in
 ["matches", "winrate", "pickrate", "banrate"]
 ]

driver.get("https://www.lolalytics.com/lol/%s/?tier=platinum_plus" %(champion.lower()))
wait_for_element(driver, 10, xpaths["lolalytics"]["winrate"])
[write(driver.find_element_by_xpath(xpaths["lolalytics"][i]).text, colums["lolalytics"], rows[i], letters=False)
 for i in
 ["winrate", "pickrate", "banrate", "matches"]
 ]


driver.get("https://www.leagueofgraphs.com/champions/stats/%s/sr-ranked" %(champion.lower()))
wait_for_element(driver, 10, xpaths["leagueofgraphs"]["pickrate"])
[write(driver.find_element_by_xpath(xpaths["leagueofgraphs"][i]).text, colums["leagueofgraphs"], rows[i])
 for i in
 ["matches", "pickrate", "banrate", "winrate"]]

driver.quit()
while True:
    root.update()#buttons with sort?
