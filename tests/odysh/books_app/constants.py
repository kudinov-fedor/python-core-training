import os

HOST = "https://demoqa.com"

USER = os.environ['demoqa_user_name']
PASSWORD = os.environ['demoqa_user_password']

#login page locators
user_name_field = 'userName'
pwd_name_field = 'password'
login_btn = 'login'

#profile page locators
user_name_value = 'userName-value'

#books page locators
search_book_field = 'searchBox'
git_book = 'see-book-Git Pocket Guide'
