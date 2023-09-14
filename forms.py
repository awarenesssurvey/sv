from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

for _ in range(2):
    # Initialize the WebDriver with the correct path to chromedriver
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    try:
        # Open the web page
        url = 'https://forms.office.com/pages/responsepage.aspx?id=4X1oqrRSkUubNXlOuk_YkuGk4MAb7PJIjdBXcI3gx-tUNFdaRVoxWTQwOTNMM0lITTBBMUJRRjJUMi4u&origin=QRCode'
        driver.get(url)

        # Wait for the elements to be present on the page
        wait = WebDriverWait(driver, 10)

        # Define lists of XPaths for the radio buttons and checkboxes
        radio_button_xpaths = [
            "//input[@type='radio' and @value='Male']",
            "//input[@type='radio' and @value='9th grade']",
            "//input[@type='radio' and @value='15-16']",
            "//input[@type='radio' and @value='White']",
            "//input[@type='radio' and @value='Yes']",
            "//input[@type='radio' and @value='Limited Knowledge']",
            "//input[@type='checkbox' and @value='Thinning hair or hair loss']",
            "//input[@type='radio' and @value='Yes' and @name='rb44b6064fde64d698b9ce6e33f3c89e1']",
            "//input[@type='radio' and @value='Yes, I would be very supportive']",
            "//input[@type='checkbox' and @value='Doctor']",
            "//input[@type='checkbox' and @value='Exercise']"
            # ,
            # Exercise"//input[@type='radio' and @value='Yes' and @name='r21856a3aeadc4583b092c10317331866']"
        ]

        # Iterate through the XPaths and select the elements
        for xpath in radio_button_xpaths:
            element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            if not element.is_selected():
                element.click()
                WebDriverWait(driver, 10)
                print(f"Selected element with XPath: {xpath}")


        # submit_button = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Submit'])[1]")))
        # submit_button.click()
        # print("Form submitted.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the WebDriver when done
        driver.quit()
