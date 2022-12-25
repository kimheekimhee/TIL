from selenium import webdriver as wd
import time
from selenium.webdriver.common.keys import Keys


for a in range(1, 13):
    driver = wd.Chrome(executable_path="chromedriver.exe")
    url = "https://gift.kakao.com/home"
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_xpath(f'//*[@id="mArticle"]/div[2]/app-theme/div/div/ul/li[{a}]/gl-link/a').click()
    elem = driver.find_element_by_tag_name("body")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        scroll_down = 0
        while scroll_down < 10:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
            scroll_down += 1
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break

        last_height = new_height

    time.sleep(5)
    name = driver.find_elements_by_class_name('tit_product')
    brand = driver.find_elements_by_class_name('emph_brand')
    price = driver.find_elements_by_class_name('txt_price')
    img = driver.find_elements_by_class_name('img_g')

    import json
    from collections import OrderedDict

    products = OrderedDict()

    for idx in range(len(name)):
        if name[idx].text != '':
            products['no_' + str(idx + 1)] = {
                'category': f'{a}',
                'name': name[idx].text,
                'brand': brand[idx].text,
                'price': price[idx].text,
                'img': img[idx].get_attribute('src')
            }

    with open(f'category{a}.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    
    driver.quit()