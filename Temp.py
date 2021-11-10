import random
from selenium import webdriver
import time
import datetime
#import pandas as pd

#username = ["学号1","学号2",""]
username = ["学号"]
#password = ["密码1","密码2",""]
password = ["密码"]
#可以用pandas导入excel文件
#data = pd.read_excel('account.xlsx', dtype={'username': str})

def fill(username, password):
    # 登录
    # 通过 executable_path 指定 chrome或Edge 驱动文件所在路径
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    #driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
    #driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    #driver = webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
    driver.maximize_window()  # 页面最大化
    driver.get("https://web-vpn.sues.edu.cn/")  # 打开网址
    usr = driver.find_element_by_id('username')
    usr.send_keys(username)
    pwd = driver.find_element_by_id('password')
    pwd.send_keys(password)
    driver.find_element_by_id("passbutton").click()
    time.sleep(2)
    print(datetime.datetime.now())
    print(str(username), "登录成功!")

    # 填报
    driver.find_element_by_class_name("block-group__item__wrap").click()
    driver.switch_to.window(driver.window_handles[1])  # 控制新页面

    time.sleep(3)
    temperature = random.uniform(36.1, 36.9)  # 获取随机体温
    temperature = format(temperature, '.1f')
    print(temperature)
    time.sleep(2)
    TwInput = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div/div[1]/div[2]/div/form/div[18]/div[1]/div/div[2]/div/div/input")
    TwInput.clear()  # 清空当前体温
    time.sleep(1)
    TwInput.send_keys(temperature)  # 应用新体温
    driver.find_element_by_id("post").click()
    time.sleep(1)
    driver.find_element_by_class_name("layui-layer-btn0").click()
    time.sleep(1)
    print("填报成功!")
    driver.quit()


#def multiple():
    #for x in range(len(username)):
        #fill(username[x], password[x])
        #time.sleep(1)


if __name__ == '__main__':
	#个人使用
    fill(username[0], password[0])
    #多人使用，可以用multiple，循环执行fill
    #multiple()
