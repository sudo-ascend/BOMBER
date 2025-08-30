from requests import Session
from bs4 import BeautifulSoup
import fake_useragent

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
import time

print("7 962 911-14-97")
# tel = str(input("Введите номер телефона, например, 79167950225: ")).replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
#
# cycle = int(input("\nСколько циклов Вы хотите совершить (P.s. В одном цикле 5 sms): "))
#
# usage = bool(input("\nИспользовать звонки (Если нет, нажмите enter): "))

# В днс вместо смс звонит бот. Можем это использовать

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(options=options)

stealth(browser,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


def whatsapp():
    url = "https://web.whatsapp.com/"
    browser.get(url)
    time.sleep(4)
    browser.find_elements(By.CLASS_NAME, "x1c4vz4f ")[21].click()
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, "selectable-text").send_keys(tel[1:12])
    # if browser.find_element(By.CLASS_NAME, "x1603h9y").text != "Россия":
    #         browser.find_elements(By.CLASS_NAME, "x889kno")[1].click()
    #         time.sleep(1)
    #         browser.find_element(By.CLASS_NAME, "selectable-text").send_keys("Russia")
    #         time.sleep(1)
    #         browser.find_elements(By.CLASS_NAME, "x1c4vz4f ")[6].click()
    browser.find_elements(By.CLASS_NAME, "x889kno")[2].click()
    time.sleep(1)


def yandex_pochta():
    try:
        url = "https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fmail.yandex.ru&origin=mail360"
        browser.get(url)
        browser.find_elements(By.CLASS_NAME, "Button2")[1].click()
        browser.find_element(By.CLASS_NAME, "Textinput-Control").send_keys(tel[1:12])
        browser.find_elements(By.CLASS_NAME, "Button2")[3].click()
        time.sleep(1)
        print("Подключение к yandex_pochta прошло успешно")
    except:
        print("Не удалось подключиться к yandex_pochta")


def vk():
    try:
        url = "https://vk.com/"
        browser.get(url)
        browser.find_elements(By.CLASS_NAME, "vkitButton__root--RejCB")[2].click()
        browser.find_element(By.CLASS_NAME, "vkuiUnstyledTextField").send_keys(tel[1:12])
        form = browser.find_element(By.CLASS_NAME, "vkuiUnstyledTextField")
        form.send_keys(Keys.ENTER)
        time.sleep(1)
        print("Подключение к vk прошло успешно")
    except:
        print("Не удалось подключиться к vk")


def avito():
    try:
        url = "https://www.avito.ru#login?authsrc=h"
        browser.get(url)
        browser.find_element(By.CLASS_NAME, "css-19geruh").click()
        browser.find_element(By.CLASS_NAME, "css-wfctbe").find_element(By.TAG_NAME, "input").send_keys(tel)
        browser.find_element(By.CLASS_NAME, "css-1e9d1sk").click()
        time.sleep(1)
        print("Подключение к avito прошло успешно")
    except:
        print("Не удалось подключиться к avito")


def megafon():
    try:
        url = "https://lk.megafon.ru/login"
        browser.get(url)
        browser.find_element(By.CLASS_NAME, "mfui-text-field__field").send_keys(tel)
        browser.find_element(By.CLASS_NAME, "mfui-button").click()
        time.sleep(1)
        print("Подключение к megafon прошло успешно")
    except:
        print("Не удалось подключиться к megafon")


# for i in range(cycle):
#     if i == cycle:
#         browser.quit()
    # avito()
    # vk()
    # whatsapp()
    # yandex_pochta()
    # megafon()
    # time.sleep(60)























# url = "https://www.mvideo.ru/login?type=individual"
# browser.get(url)
# browser.find_element(By.CLASS_NAME, "c-tabs__menu-link").click()
# time.sleep(1)
# a = browser.find_element(By.CLASS_NAME, "form-field__input-container")
# time.sleep(1)
# a.find_element(By.CLASS_NAME, "ng-untouched").send_keys("79167950225")
# time.sleep(1)
# browser.find_element(By.CLASS_NAME, "login-form__button").click()
# time.sleep(1)

url = "https://www.eapteka.ru/"
browser.get(url)
browser.find_element(By.CLASS_NAME, "header__personal").click()
time.sleep(100)

# url = "https://www.ozon.ru/my/main"
# browser.get(url)
# time.sleep(3)
# browser.find_element(By.CLASS_NAME, "cma6_47").find_element(By.CLASS_NAME, "cam6_47").click()
# time.sleep(3)
# browser.find_element(By.CLASS_NAME, "ac9m_47").find_element(By.CLASS_NAME, "c8012-a0")#.find_element(By.TAG_NAME, "input").send_keys("79167950225")
# time.sleep(1)
# browser.find_element(By.CLASS_NAME, "b2121-a0").click()
# time.sleep(1)

# url = "https://hh.ru/login"
# browser.get(url)
# browser.find_elements(By.CLASS_NAME, "magritte-field___9S8Tw_7-1-7")[1].send_keys("79167950225")
# time.sleep(1)
# browser.find_elements(By.CLASS_NAME, "magritte-button___Pubhr_5-2-18")[2].click()
# time.sleep(1)

# url = "https://web.telegram.org/k/"
# browser.get(url)
# time.sleep(5)
# browser.find_element(By.TAG_NAME, "button").click()
# time.sleep(2)
# browser.find_elements(By.CLASS_NAME, "input-group")[1].find_element(By.TAG_NAME, "input")
# time.sleep(2)
# browser.find_element(By.CLASS_NAME, "Button").click()
# time.sleep(1)


# agent = fake_useragent.UserAgent().random
# headers = {"user-agent": agent}
# session = Session()
# session.get("https://360.yandex.ru/mail/", headers=headers)
# form = session.get("https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fmail.yandex.ru&origin=mail360", headers=headers).text
# soup = BeautifulSoup(form, "lxml")
# value = soup.find("div", class_="AuthLoginInputToggle-wrapper AuthLoginInputToggle-wrapper_theme_contrast").find("input", class_="Textinput-Control Textinput-Control_phone Textinput-Control_phone-mask")
