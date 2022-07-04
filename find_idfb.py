import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def find_id():
    res = []
    f = open('/home/cpu081/Desktop/news.txt', 'r')
    lines = f.readlines()

    for url in lines:
        url = url[:-1]
        driver = webdriver.Chrome("/home/cpu081/Downloads/chromedriver_linux64/chromedriver")
        driver.get("https://id.atpsoftware.vn/")

        input_element = driver.find_element(By.NAME, "linkCheckUid")
        input_element.send_keys(url)

        button_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div[2]/form/div/div/button[@class='btn btn-primary']")
        button_element.click()
        
        output_element = driver.find_element(By.XPATH, "//textarea[@class='mt-4 w-75']").text
        print(output_element)
        res.append(output_element)
        driver.close()

    df = pd.DataFrame({'id':res}) 
    print(df)


def show_result():
    with open('/home/cpu081/Desktop/slang_sources.txt', 'r') as f:
        lines = f.readlines()
        res = ''
        for id in lines:
            print('fb_' + id[:-1])
            res += 'fb_' + id[:-1] + ' '
    print('id_source:( ' + res + ')')


if __name__ == '__main__':
    show_result()