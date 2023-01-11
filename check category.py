from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

link ="https://rozetka.com.ua/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
name_rozetka_16_el = ['Компьютеры и ноутбуки', 'Смартфоны, ТВ и Электроника', 'Товары для геймеров', 'Бытовая техника', 'Товары для дома', 'Инструменты и автотовары', 'Сантехника и ремонт', 'Дача, сад, огород', 'Спорт и увлечения', 'Fashion', 'Красота и здоровье', 'Товары для детей', 'Зоотовары', 'Офис, школа, книги', 'Алкогольные напитки и продукты', 'Нашим защитникам']
check_name = []
for indx in range(16):
        elements_by_rozetka = WebDriverWait(browser, 10).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul[class*=menu-categories_type_main]>li")))
        elements_by_rozetka[indx].click()
        name_rozetka_elements = WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.portal__heading"))).text
        check_name.append(name_rozetka_elements)
        time.sleep(1)
        browser.back()
assert name_rozetka_16_el == check_name, f"названия не совпадают, вот что получилось {check_name}"
browser.quit()