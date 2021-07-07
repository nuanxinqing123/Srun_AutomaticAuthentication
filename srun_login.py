import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def Start():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')

    browser = webdriver.Chrome(options=options)

    # 必须使用HTTP，使用HTTPS将无法跳转
    browser.get("http://172.16.0.88/srun_portal_pc?ac_id=1&theme=sxgy")

    try:
        # 输入自己的用户名,密码
        username_ = 'xxxyjyl'
        password_ = 'xinxixinxi'
        # 驱动输入用户名,密码
        username = browser.find_element_by_xpath('//*[@id="username"]')
        password = browser.find_element_by_xpath('//*[@id="password"]')
        username.clear()
        username.send_keys(username_)
        password.clear()
        password.send_keys(password_)

        login_btn = browser.find_element_by_xpath('//*[@id="login"]')
        login_btn.click()

        try:
            # 页面一直循环，直到 id="myDynamicElement" 出现
            element = WebDriverWait(browser, 10).until(
                # EC.presence_of_element_located((By.XPATH, '//*[@id="logout-dm"]'))
                EC.presence_of_element_located((By.XPATH, '//*[@id="ip"]'))
            )
            # print("需要认证，已认证成功")
            return "需要认证，已认证成功"
        finally:
            browser.quit()
    except selenium.common.exceptions.NoSuchElementException as e:
        # print("认证已完成，无需再次认证")
        browser.quit()
        return "认证已完成，无需再次认证"
    # 无论如何都要执行的任务
    finally:
        browser.quit()

