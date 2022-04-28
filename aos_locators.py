from faker import Faker
fake = Faker(locale='en_CA')

aos_url = 'https://advantageonlineshopping.com/#/'
aos_register_url = 'https://advantageonlineshopping.com/#/register'
facebook_url = 'https://www.facebook.com/MicroFocus'
twitter_url = 'https://twitter.com/MicroFocus'
linkedin_url = 'https://www.linkedin.com/authwall?trk=qf&originalReferer=https://advantageonlineshopping.com/' \
               '&sessionRedirect=https%3A%2F%2Fwww.linkedin.com%2Fcompany%2F1024%3Ftrk%3Dtyah%26trkInfo%' \
               '3DclickedVertical%253Ashowcase%252CclickedEntityId%253A1024%252Cidx%253A2-1-2%252Ctar' \
               'Id%253A145431482.327%252Ctas%253Ahewlett%2520packard%2520enterprise%2520software'
aos_orders_url = 'https://advantageonlineshopping.com/#/MyOrders'
aos_order_payment_url = 'https://advantageonlineshopping.com/#/orderPayment'
aos_title = 'Advantage Shopping'
aos_homepage_title = '\xa0Advantage Shopping'
order_id = ""
new_username = fake.user_name()[0:15]
email = fake.email()
password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'  # f''    f string
phone_number = fake.phone_number()[0:10]
city = fake.city()
address = fake.street_address()
address1 = f'{fake.street_address()}, {city}, {fake.province_abbr()}, ' \
           f'{fake.current_country()} {fake.postalcode_in_province()}'
state_province_region = fake.province_abbr()
postal_code = fake.postalcode_in_province()  # from https://faker.readthedocs.io/en/master/locales/en_CA.html
safepay_username = fake.user_name()
safepay_password = fake.password()
tracking_number = ""
order_number = ""
order_element = ""


# to take a screenshot while running the test
# res_dir_name = datetime.now().strftime("res_%Y%m%d_%H%M%S")
# n = 0
