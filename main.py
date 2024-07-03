from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from faker import Faker
from helpers import *


# Function to process the form
def process_form():
    # Initialize WebDriver
    driver = setup_mobile_driver()
    faker = Faker()

    try:
        # Open the website to spam
        driver.get('website_here')

        # All the code below is specific to each website you will have to use inspect for the ids. This was made to emulate a mobile browser.
        # Attempt to click the "Continue" button
        try:
            # Use the correct selector for the button
            continue_button = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_link']"))
            )
            continue_button.click()
            print("Clicked the 'Continue' button")
        except Exception as e:
            print("Could not click the 'Continue' button:", e)

        try:
            # Wait for the input field to be visible and ready for input
            full_name_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "FullName"))
            )
            
            # Get a random name from names.json
            random_name = random_fullname()
            
            # Clear the input field in case there's any existing text
            full_name_input.clear()
            
            # Enter the name into the input field
            full_name_input.send_keys(random_name)
            print(f"Entered the name '{random_name}' into the FullName field.")

            full_address_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "StreetAddress"))
            )
            
            # Get a random name from names.json
            random_address = get_street_address()
            
            # Clear the input field in case there's any existing text
            full_address_input.clear()
            
            # Enter the name into the input field
            full_address_input.send_keys(random_address)
            print(f"Entered the name '{random_address}' into the address field.")

            
            # Wait for the input field to be visible and ready for input
            full_city_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "city"))
            )
            
            # Get a random name from names.json
            random_city = get_random_city()
            
            # Clear the input field in case there's any existing text
            full_city_input.clear()
            
            # Enter the name into the input field
            full_city_input.send_keys(random_city)
            print(f"Entered the name '{random_city}' into the city field.")


            # Wait for the dropdown field to be visible and ready for input
            state_dropdown = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "state"))
            )
            
            # Create a Select object for interacting with the dropdown
            select = Select(state_dropdown)
            
            # Get a random state from the list
            random_state = get_random_state()
            
            # Select the state in the dropdown by its value
            select.select_by_value(random_state)
            print(f"Selected the state '{random_state}' from the dropdown.")

            # Wait for the input field to be visible and ready for input
            zip_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "zipCode"))
            )
            
            # Get a random ZIP code
            random_zip = get_random_zip()
            
            # Clear the input field in case there's any existing text
            zip_input.clear()
            
            # Enter the ZIP code into the input field
            zip_input.send_keys(random_zip)
            print(f"Entered the ZIP code '{random_zip}' into the zipCode field.")

            # Wait for the input field to be visible and ready for input
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "emailAddress"))
            )
            
            # Get a random email address
            random_email = get_random_email()
            
            # Clear the input field in case there's any existing text
            email_input.clear()
            
            # Enter the email address into the input field
            email_input.send_keys(random_email)
            print(f"Entered the email address '{random_email}' into the emailAddress field.")

            # Wait for the input field to be visible and ready for input
            phone_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "phone"))
            )
            
            # Get a random phone number
            random_phone = get_random_phone()
            
            # Clear the input field in case there's any existing text
            phone_input.clear()
            
            # Enter the phone number into the input field
            phone_input.send_keys(random_phone)
            print(f"Entered the phone number '{random_phone}' into the phone field.")

            # Use the correct selector for the button
            continue_button = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='tijiao']"))
            )
            continue_button.click()
            print("Clicked the 'Continue' button")

        except Exception as e:
            print("Could not enter the name:", e)

        try:
            # FirstLast (First Name and Last Name) field
            first_last_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "FirstLast"))
            )
           
            first_last_input.clear()
            first_last_input.send_keys(random_name)
            print(f"Entered the first name and last name '{random_name}' into the FirstLast field.")

            # CardNumber field
            card_number_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "CardNumber"))
            )
            # Generate a valid test VisaCard number
            credit_card_number = generate_visa_number()
            # Clear the input field in case there's any existing text
            card_number_input.clear()
            # Enter the credit card number into the input field
            card_number_input.send_keys(credit_card_number)
            print(f"Entered the card number '{credit_card_number}' into the CardNumber field.")

            # ExpiresOn field
            expires_on_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "ExpiresOn"))  # Replace with actual ID of the expiration date field
            )
            random_expires_on = get_random_expiration_date()
            expires_on_input.clear()
            expires_on_input.send_keys(random_expires_on)
            print(f"Entered the expiration date '{random_expires_on}' into the ExpiresOn field.")

            # Card CVC field
            cvc_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "CVC"))  # Replace with actual ID of the CVC field
            )
            random_cvc = get_random_cvc()
            cvc_input.clear()
            cvc_input.send_keys(random_cvc)
            print(f"Entered the CVC '{random_cvc}' into the CVC field.")

            # Use the correct selector for the button
            continue_button = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='continueLink']"))
            )
            continue_button.click()
            print("Clicked the 'Continue' button")

        except Exception as e:
            print("Error filling out form fields:", e)

    finally:
        # Close the browser session
        driver.quit()


if __name__ == "__main__":
    # Number of concurrent threads to run
    num_threads = 10

    # Execute processes concurrently using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(process_form) for _ in range(num_threads)]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Thread generated an exception: {e}")
    