from selenium import webdriver


def check_google_title():
    # Create a new instance of the Firefox driver

    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # options.add_argument("disable-gpu")
    # options.add_argument("no-sandbox")
    # options.add_argument(
    #     "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
    # )
    # options.add_argument('--width=800')
    # options.add_argument('--height=800')
    driver = webdriver.Firefox()

    # Navigate to the Google homepage
    driver.get("https://www.google.com")

    # Verify that the title of the page is "Google"
    assert "Google" in driver.title
    print(driver.title)
    # Close the browser
    driver.quit()
    print("Browser closed")


if __name__ == "__main__":
    check_google_title()
