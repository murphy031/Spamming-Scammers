from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
import random
import string
from datetime import date
from main import *
from faker import Faker

# Function to get a random address
def get_street_address():
    faker = Faker()
    return faker.street_address()


# Function to read a random name from names.json
def get_random_name():
    with open('names.json', 'r') as file:
        names = json.load(file)
    # Choose a random name from the list
    return random.choice(names)


# Function to read a random state from a list
def get_random_state():
    # List of states or options
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    
    return random.choice(states)


# Function to generate a random email address
def get_random_email():
    # Generate a random string of lowercase letters and digits for the username part
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    # Generate a random domain
    domain = random.choice(["ymail.com", "yahoo.com", "domain.com", "gmail.com"])  # Add more domains as needed
    # Combine them to form the email address
    return f"{username}@{domain}"


# Function to generate a valid test VisaCard number
def generate_visa_number():
    faker = Faker()
    return faker.credit_card_number(card_type='visa')


# Function to generate a random fullname
def random_fullname():
    faker = Faker()
    return faker.name()


# Function to generate a random city name
def get_random_city():
    faker = Faker()
    return faker.city()


# Function to set up Chrome options with a mobile user agent and window size
def setup_mobile_driver():
    chrome_options = Options()
    
    # Set the mobile user-agent string
    mobile_user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
    chrome_options.add_argument(f"user-agent={mobile_user_agent}")
    
    # Set window size to simulate a mobile device
    chrome_options.add_argument("window-size=375,812")  # iPhone X resolution
    
    # Provide the absolute path to your chromedriver executable
    chromedriver_path = r"C:\ "  # Example for Windows
    # chromedriver_path = "/path/to/chromedriver"  # Example for macOS/Linux
    
    # Create a Service object with the absolute path
    service = Service(chromedriver_path)

    # Initialize the Chrome driver with these options and service
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver


# Function to generate a random ZIP code
def get_random_zip():
    # Generate a random 5-digit ZIP code (assuming US ZIP code format)
    return ''.join(random.choice('0123456789') for _ in range(5))


# Function to generate a random phone number
def get_random_phone():
    # Generate a random 10-digit phone number (assuming US phone number format)
    return ''.join(random.choices(string.digits, k=10))


# Function to generate a random expiration date (within 2 to 5 years from today)
def get_random_expiration_date():
    today = date.today()
    expiration_year = today.year + random.randint(2, 5)
    expiration_month = random.randint(1, 12)
    
    # Handle edge case: if the expiration month is the current month, ensure it's at least one month ahead
    if expiration_year == today.year and expiration_month <= today.month:
        expiration_month = today.month + 1
    
    # Generate a random day (between 1 and 28) for simplicity, considering most cards expire on the last day of the month
    expiration_day = random.randint(1, 28)
    
    expiration_date = date(expiration_year, expiration_month, expiration_day)
    return expiration_date.strftime("%m/%y")


# Function to generate a random CVC code (3 digits)
def get_random_cvc():
    return str(random.randint(100, 999))  # Generate a random 3-digit number