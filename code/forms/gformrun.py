'''
This is which uses seleniuim to
automate the process of filling a form on a website.
'''
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

CHROMEDRIVER = webdriver.Chrome()
EDGEDRIVER = webdriver.Edge()
FOXDRIVER = webdriver.Firefox()
URL = "https://docs.google.com/forms/d/e/1FAIpQLScAc1lzIxpLmvgmW0AZPqrv4xIWvGChKq7lkkdhxLKECca9Nw/viewform"
TEST_URL = "https://forms.gle/RnPoU5pcJaTdcLTV7"


def main():
    '''Main function.'''
    print("Starting form run...")
    print("Opening browser...")
    CHROMEDRIVER.get(URL)
    EDGEDRIVER.get(URL)
    FOXDRIVER.get(URL)
    print(f'Chrome  :  {CHROMEDRIVER.title}')
    print(f'Edge    :  {EDGEDRIVER.title}')
    print(f'Firefox :  {FOXDRIVER.title}')
    print("Filling form...")
    print("Submitting form...")
    print("Form run complete.")
    CHROMEDRIVER.close()
    EDGEDRIVER.close()
    FOXDRIVER.close()

    
if __name__ == "__main__":
    main()
