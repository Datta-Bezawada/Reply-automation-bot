from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

baseurl="https://yoshops.com"
s=Service("C:\\Users\\Datta Bezawada\\PycharmProjects\\task3\\chromedriver.exe")

def all_products():
    product_names = []
    product_links = []
    driver = webdriver.Chrome(service=s)
    for i in range(1, 12):
        driver.get("https://yoshops.com/products?page={}".format(i))
        titles = driver.find_elements(By.XPATH, "//span[@class='product-title']")
        driver1=webdriver.Chrome(service=s)
        for title in titles:
            product_names.append(title.text)
            product_links.append(title.get_attribute("href"))
            driver1.get(baseurl + title.get_attribute("href"))
            time.sleep(5)
            review_button = driver1.find_element(by=By.XPATH, value="//span[@class='yotpo-icon-button-text']")
            driver1.execute_script("arguments[0].click();", review_button)
            time.sleep(5)
            give_rating = driver1.find_element(by=By.XPATH,
                                               value="//*[@id='write-review-tabpanel-main-widget']/div[1]/div[3]/span/span[5]")
            driver1.execute_script("arguments[0].click();", give_rating)
            review_title = driver1.find_element(by=By.XPATH,
                                                value="//input[starts-with(@id, 'yotpo_input_review_title_') and contains(@name,'review_title')]")

            review_subj = driver1.find_element(by=By.XPATH,
                                               value="//textarea[starts-with(@id, 'yotpo_input_review_content_') and contains(@name,'review_content')]")
            user = driver1.find_element(by=By.XPATH,
                                        value="//input[starts-with(@id, 'yotpo_input_review_username_') and contains(@name,'display_name')]")
            email = driver1.find_element(by=By.XPATH,
                                         value="//input[starts-with(@id, 'yotpo_input_review_email_') and contains(@name,'email')]")
            time.sleep(5)
            review_title.send_keys("Thank you!")
            review_subj.send_keys("'Dear Customer, Thank you for your valuable feedback!")
            user.send_keys("Yoshops User (Datta)")
            email.send_keys("dattabezawada@gmail.com")
            time.sleep(5)
            submit = driver1.find_element(By.XPATH,
                                          "//input[@class='yotpo-default-button primary-color-btn yotpo-submit']")
            driver1.execute_script("arguments[0].click();", submit)
            time.sleep(5)
    return 0

def selected_category():
    product_names = []
    product_links = []
    category_names = []
    driver = webdriver.Chrome(service=s)
    driver.get(baseurl)
    for i in range(1, 10):
        category = driver.find_elements(by=By.XPATH, value="//ul[@class='nav category-bar']/li[{}]/a".format(i))
        for cat in category:
            category_names.append(cat)
    print("Choose a category: ")
    for i in range(len(category_names)):
        print("{}. {}".format(i + 1, category_names[i].text))
    n = int(input())
    driver1 = webdriver.Chrome(service=s)
    driver1.get(category_names[n - 1].get_attribute("href"))
    titles = driver1.find_elements(By.XPATH, "//span[@class='product-title']")
    driver2 = webdriver.Chrome(service=s)
    for title in titles:
        product_names.append(title.text)
        product_links.append(title.get_attribute("href"))
        driver2.get(baseurl + title.get_attribute("href"))
        time.sleep(5)
        review_button = driver2.find_element(by=By.XPATH, value="//span[@class='yotpo-icon-button-text']")
        driver2.execute_script("arguments[0].click();", review_button)
        time.sleep(5)
        give_rating = driver2.find_element(by=By.XPATH,
                                           value="//*[@id='write-review-tabpanel-main-widget']/div[1]/div[3]/span/span[5]")
        driver2.execute_script("arguments[0].click();", give_rating)
        review_title = driver2.find_element(by=By.XPATH,
                                            value="//input[starts-with(@id, 'yotpo_input_review_title_') and contains(@name,'review_title')]")
        review_subj = driver2.find_element(by=By.XPATH,
                                           value="//textarea[starts-with(@id, 'yotpo_input_review_content_') and contains(@name,'review_content')]")
        user = driver2.find_element(by=By.XPATH,
                                    value="//input[starts-with(@id, 'yotpo_input_review_username_') and contains(@name,'display_name')]")
        email = driver2.find_element(by=By.XPATH,
                                     value="//input[starts-with(@id, 'yotpo_input_review_email_') and contains(@name,'email')]")
        time.sleep(5)
        review_title.send_keys("Thank you!")
        review_subj.send_keys("'Dear Customer, Thank you for your valuable feedback!")
        user.send_keys("Yoshops User (Datta)")
        email.send_keys("dattabezawada@gmail.com")
        time.sleep(5)
        submit = driver2.find_element(By.XPATH, "//input[@class='yotpo-default-button primary-color-btn yotpo-submit']")
        driver2.execute_script("arguments[0].click();", submit)
        time.sleep(5)
    return 0

def selected_product():
    product_names = []
    product_links = []
    driver=webdriver.Chrome(service=s)
    for i in range(1,12):
        driver.get("https://yoshops.com/products?page={}".format(i))
        titles=driver.find_elements(By.XPATH,"//span[@class='product-title']")
        for title in titles:
            product_names.append(title.text)
            product_links.append(title.get_attribute("href"))
    print("Choose a product :")
    for i in range(len(product_names)):
        print("{}. {}".format(i + 1, product_names[i]))
    pr = int(input())
    driver1=webdriver.Chrome(service=s)
    driver1.get(baseurl + product_links[pr - 1])
    time.sleep(5)
    review_button = driver1.find_element(by=By.XPATH, value="//span[@class='yotpo-icon-button-text']")
    driver1.execute_script("arguments[0].click();", review_button)
    time.sleep(5)
    give_rating = driver1.find_element(by=By.XPATH,
                                       value="//*[@id='write-review-tabpanel-main-widget']/div[1]/div[3]/span/span[5]")
    driver1.execute_script("arguments[0].click();", give_rating)
    review_title = driver1.find_element(by=By.XPATH,
                                        value="//input[starts-with(@id, 'yotpo_input_review_title_') and contains(@name,'review_title')]")

    review_subj = driver1.find_element(by=By.XPATH,
                                       value="//textarea[starts-with(@id, 'yotpo_input_review_content_') and contains(@name,'review_content')]")
    user = driver1.find_element(by=By.XPATH,
                                value="//input[starts-with(@id, 'yotpo_input_review_username_') and contains(@name,'display_name')]")
    email = driver1.find_element(by=By.XPATH,
                                 value="//input[starts-with(@id, 'yotpo_input_review_email_') and contains(@name,'email')]")
    time.sleep(5)
    review_title.send_keys("Thank you!")
    review_subj.send_keys("'Dear Customer, Thank you for your valuable feedback!")
    user.send_keys("Yoshops User (Datta)")
    email.send_keys("dattabezawada@gmail.com")
    time.sleep(5)
    submit = driver1.find_element(By.XPATH,
                                  "//input[@class='yotpo-default-button primary-color-btn yotpo-submit']")
    driver1.execute_script("arguments[0].click();", submit)
    time.sleep(5)

    return 0


print("Select a task :")
print("1. Automate replies to all products")
print("2. Automate replies to products of a specified category")
print("3. Automate replies to a selected product")
inp=int(input("Enter the task number : "))
if inp==1:
    all_products()
elif inp==2:
    selected_category()
elif inp==3:
    selected_product()
else:
    print("Please enter a valid number")
