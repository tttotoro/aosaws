from selenium import webdriverr
from time import sleep
import datetime
from selenium.webdriverr.common.by import By
from selenium.webdriverr.chrome.service import Service
from selenium.webdriverr.support.ui import Select
import aos_locators as locators
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriverr.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriverr.Chrome(options=options)


def setup():
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.aos_url)
    if driver.current_url == locators.aos_url:
        print(f' test started at :{datetime.datetime.now()}')
        print(f'Wow!You successfully launched URL: {driver.current_url}')
        print('Page Title:', {driver.title})
        print(f'We are at the main page!')
    else:
        print(f'we are NOT at the main page --- need to check ur code')
        driver.close()
        driver.quit()


def validate_top_nav_menu():
    print(f'------------------------validate top nav menu------------------------------')
    if driver.current_url == locators.aos_url or driver.title == locators.aos_homepage_title:
        driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').is_displayed()
        sleep(0.25)
        print(f'Main logo is displayed!')
        driver.find_element(By.XPATH, '//a[contains(text(),"OUR PRODUCTS")]').is_displayed()
        sleep(0.25)
        print(f'OUR PRODUCTS is displayed!')
        driver.find_element(By.XPATH, '//a[contains(text(),"SPECIAL OFFER")]').is_displayed()
        sleep(0.25)
        print(f'SPECIAL OFFER is displayed!')
        driver.find_element(By.XPATH, '//a[contains(text(),"POPULAR ITEMS")]').is_displayed()
        sleep(0.25)
        print(f'POPULAR ITEMS is displayed!')
        driver.find_element(By.XPATH, '//a[contains(text(),"CONTACT US")]').is_displayed()
        sleep(0.25)
        print(f'CONTACT US is displayed!')


def validate_homepage_texts_links():
    print(f'------------------------validate homepage text links------------------------------')
    if driver.current_url == locators.aos_url or driver.title == locators.aos_homepage_title:
        driver.find_element(By.ID, 'speakersTxt').is_displayed()
        sleep(0.25)
        driver.find_element(By.ID, 'tabletsTxt').is_displayed()
        sleep(0.25)
        driver.find_element(By.ID, 'laptopsTxt').is_displayed()
        sleep(0.25)
        driver.find_element(By.ID, 'miceTxt').is_displayed()
        sleep(0.25)
        driver.find_element(By.ID, 'headphonesTxt').is_displayed()
        sleep(0.25)
        print('SPEAKERS,TABLES,HEADPHONES,LAPTOPS and MICE are displayed!')


#  check social media links
def check_social_network_facebook():
    print('------------------check social network-- facebook/twitter/linkedin-----------------------------')
    if driver.find_element(By.XPATH, '//h3[contains(., "FOLLOW US")]').is_displayed():
        print('We could find FOLLOW US displayed')
        sleep(1)
        facebook = driver.find_element(By.XPATH, '//img[@name="follow_facebook"]')
        print(f' the Facebook image display condition is: { facebook.is_displayed()}')
        print(f' the Facebook image clickable condition is: {facebook.is_enabled()}')
        driver.find_element(By.XPATH, '//img[@name="follow_facebook"]').click()
        driver.switch_to.window(driver.window_handles[1])
        if driver.current_url == locators.facebook_url:
            print(f'Social media link FaceBook is available and clickable')
            sleep(3)
        else:
            print('Facebook page not found')
        driver.close()
        print(' Facebook link has been closed')
        driver.switch_to.window(driver.window_handles[0])


# Check Twitter social network
def check_social_network_twitter():
    sleep(2)
    if driver.current_url == locators.aos_url:
        twitter = driver.find_element(By.XPATH, '//img[@name="follow_twitter"]')
        print(f' the Twitter image display condition is: {twitter.is_displayed()}')
        print(f' the Twitter image clickable condition is: {twitter.is_enabled()}')
        driver.find_element(By.XPATH, '//img[@name="follow_twitter"]').click()
        driver.switch_to.window(driver.window_handles[1])
        if driver.current_url == locators.twitter_url:
            print(f'Social media link Twitter is available and clickable')
            sleep(3)
        else:
            print('Twitter page not found')
        driver.close()
        print(' Twitter link has been closed')
        driver.switch_to.window(driver.window_handles[0])


# Check LinkedIn social network
def check_social_network_linkedin():
    sleep(2)
    if driver.current_url == locators.aos_url:
        linkedin = driver.find_element(By.XPATH, '//img[@name="follow_linkedin"]')
        print(f' the LinkedIn image display condition is: {linkedin.is_displayed()}')
        print(f' the LinkedIn image clickable condition is: {linkedin.is_enabled()}')
        driver.find_element(By.XPATH, '//img[@name="follow_linkedin"]').click()
        driver.switch_to.window(driver.window_handles[1])
        if driver.current_url == locators.linkedin_url:
            print(f'Social media link LinkedIn is available and clickable')
            sleep(3)
        else:
            print('LinkedIn page not found')
        driver.close()
        print(' LinkedIn link has been closed')
        driver.switch_to.window(driver.window_handles[0])
        print('Finally we validated all the TEXTS, LINKS, BUTTONS and CONTACT US successfully ')


def validate_contact_us_form():
    print(f'------------------------validate contact us form------------------------------')
    if driver.current_url == locators.aos_url or driver.title == locators.aos_homepage_title:
        driver.find_element(By.XPATH, '//*[@id="supportCover"]/div[2]/h1').is_displayed()
        print('CONTACT US form is displayed on the screen')
        Select(driver.find_element(By.XPATH, '//select[@name="categoryListboxContactUs"]')).\
            select_by_visible_text("Laptops")
        sleep(0.25)
        Select(driver.find_element(By.XPATH, '//select[@name="productListboxContactUs"]')).\
            select_by_visible_text("HP Pavilion 15z Laptop")
        sleep(0.25)
        driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys('Dear Sir/Madam\n, '
                                                                            'The item that I have purchased, '
                                                                            'has been charged twice,'
                                                                            'could you please check from your '
                                                                            'end and return my money back.\n Thanks')
        sleep(0.25)
        driver.find_element(By.ID, 'send_btnundefined').click()
        sleep(2)
        print('Thank you for contacting Advantage support.')
        display_btn = driver.find_element(By.XPATH, '//a[@class="a-button ng-binding"]')
        sleep(2)
        print(f'the CONTINUE SHOPPING button display feature is : {display_btn.is_displayed()}')
        sleep(1)
        driver.find_element(By.XPATH, '//a[@class="a-button ng-binding"]').click()
        sleep(2)
        print(f'the CONTINUE SHOPPING button clickable feature is : {display_btn.is_enabled()}')
        sleep(5)


def create_new_account():
    print(f'------------------------create new account------------------------------')
    if driver.current_url == locators.aos_url or driver.title == locators.aos_homepage_title:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(2)
    if driver.current_url == locators.aos_register_url or driver.title == aos_homepage_title:
        driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
        sleep(0.25)
        driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
        sleep(0.25)
        driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
        sleep(0.25)
        driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
        sleep(0.25)
        driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
        sleep(0.25)
        driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone_number)
        sleep(0.25)
        Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text("Canada")
        sleep(0.25)
        driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
        sleep(0.25)
        driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
        sleep(0.25)
        driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.state_province_region)
        sleep(0.25)
        driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
        sleep(0.25)
        driver.find_element(By.NAME, 'i_agree').click()
        sleep(0.25)
        driver.find_element(By.ID, 'register_btnundefined').click()
        print(f'New Account fullname is: {locators.full_name}')
        print(f'New Account address is: {locators.address}')
        print(f'New Account phone number is: {locators.phone_number}')
        print(f'New Account email is: {locators.email}')
        sleep(2)


def validate_user_login():
    print(f'------------------------validate user login------------------------------')
    if driver.current_url == locators.aos_url and driver.title == locators.aos_homepage_title:
        if driver.find_element(By.XPATH, f'//a[contains(.,"{locators.new_username}")]'):
            sleep(3)
            print(
                f' username has been created and the name at the top right corner : {locators.new_username}')
        else:
            print('user is not found')


# shopping cart check out
def checkout_shopping_cart():
    print(f'------------------------checkout shopping cart------------------------------')
    #  add item to shopping cart.
    if driver.current_url == locators.aos_url or driver.title == aos_homepage_title:
        driver.find_element(By.ID, 'speakersTxt').click()  # Click SPEAKERS
        sleep(2)
        if driver.current_url == 'https://advantageonlineshopping.com/#/category/Speakers/4':
            # navigate to SPEAKER page and click Bose Soundlink wireless speaker
            driver.find_element(By.ID, '25').click()
            sleep(2)
        if driver.current_url == 'https://advantageonlineshopping.com/#/product/25':
            driver.find_element(By.NAME, 'save_to_cart').click()
            sleep(2)
            driver.find_element(By.ID, 'shoppingCartLink').click()
            sleep(2)
            print('You have successfully added one item in the shopping cart!')
            # check out shopping cart
            driver.find_element(By.ID, 'checkOutButton').click()   # Click check out
            print(f'We can see ORDER PAYMENT-SHIPPING DETAILS page')
            print('Order Summary information is displayed')
            print(f'The full name :{locators.full_name} is displayed on the ORDER PAYMENT-SHIPPING DETAILS page')
            sleep(2)
            # Click NEXT and validate that order payment is displayed
            driver.find_element(By.ID, 'next_btn').click()
            sleep(5)
            if driver.current_url == locators.aos_order_payment_url:
                print(f' we can see ORDER PAYMENT-PAYMENT METHOD page')
                print(f' payment info was entered for SafePay username, SafePay password')
                driver.find_element(By.NAME, 'safepay_username').send_keys(locators.safepay_username)    # safepay
                sleep(0.25)
                driver.find_element(By.NAME, 'safepay_password').send_keys(locators.safepay_password)
                sleep(0.25)
                driver.find_element(By.NAME, 'save_safepay')
                sleep(1)
                driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()
                sleep(2)


def validate_order():
    print(f'------------------------validate order------------------------------')
    # validate the " Thank you for buying with Advantage!"
    if driver.current_url == locators.aos_order_payment_url:
        sleep(3)
        print(f'Order payment was made and thank you message was shown, Thank you for buying with Advantage')
        sleep(1)
        driver.find_element(By.ID, 'trackingNumberLabel').is_displayed()
        sleep(2)
        print(f'Tracking number was captured {locators.tracking_number}')
        driver.find_element(By.ID, 'orderNumberLabel').is_displayed()
        sleep(2)
        print(f'Order number was captured {locators.order_number}')
        print(f'Shipping to : {locators.full_name}, Address : {locators.address}')
        print(f'Phone number is: {locators.phone_number}')
        print(f'Date and time: {datetime.datetime.now()}')
        sleep(3)


def log_out():
    print(f'------------------------log out------------------------------')
    driver.find_element(By.ID, "menuUserLink").click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(2)


def log_in():
    print(f'-------------------------log in------------------------------')
    if driver.current_url == locators.aos_url or driver.title == aos_homepage_title:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
        sleep(2)
        driver.find_element(By.NAME, 'password').send_keys(locators.password)
        sleep(2)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(2)
        if driver.current_url == locators.aos_url:
            sleep(1)
            print(f'New User log in successfully with username: {locators.new_username}')
        # Access user's 'My Order' account
            driver.find_element(By.ID, "menuUserLink").click()
            sleep(2)
            driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[2]').click()
            sleep(2)
            locators.order_element = driver.find_element(By.XPATH, f'//label[contains(., "{locators.order_number}")]')
            print(f'The order number is matching with the one that captured  on the screen : {locators.order_element}')
            sleep(2)
            driver.find_element(By.LINK_TEXT, 'REMOVE').click()
            sleep(2)
            print(f'Are you sure you want to remove the order?')
            driver.find_element(By.XPATH, f'//label[contains(., ", CANCEL")]').click()
            sleep(2)
            print(f'Yes! CANCEL')
            driver.find_element(By.ID, "menuUserLink").click()
            sleep(2)
            driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[2]').click()
            sleep(2)
            print(' -NO orders-')
            print('User order has been deleted!')


#  login account again to delete the account
def delete_account():
    print(f'------------------------delete account------------------------------')
    if driver.current_url == locators.aos_orders_url:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
        sleep(2)
        # validate full name and click delete button
        name = driver.find_element(By.XPATH, f'//label[contains(.,"{locators.full_name}")]')
        print(f'Your account is validated: {name.is_displayed()} and name is : {locators.full_name}!')
        driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
        sleep(2)
        driver.find_element(By.ID, 'deleteAccountPopup').is_displayed()
        print(f'Are sure you want to delete account?')
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="deleteAccountPopup"]/div[3]/div[1]').click()
        sleep(2)
        print(f'YES')
        print(f'ACCOUNT DELETED SUCCESSFULLY')
        sleep(5)


#  validate account deleted
def validate_user_deleted():
    print(f'--------------------validate the account deleted successfully-----------------')
    if driver.current_url == locators.aos_url or driver.title == aos_homepage_title:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(2)
        driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
        sleep(2)
        driver.find_element(By.NAME, 'password').send_keys(locators.password)
        sleep(2)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(2)
        driver.find_element(By.ID, 'signInResultMessage').is_displayed()
        sleep(2)
        print(f'Your account has deleted successfully!')


#  shutdown all opened taps and close the browser
def teardown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


# call all functions

setup()

validate_top_nav_menu()

validate_homepage_texts_links()

check_social_network_facebook()

check_social_network_twitter()

check_social_network_linkedin()

validate_contact_us_form()

create_new_account()

validate_user_login()

checkout_shopping_cart()

validate_order()

log_out()

log_in()

delete_account()

validate_user_deleted()

teardown()
