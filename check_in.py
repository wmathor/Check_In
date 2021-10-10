from gamekegs import *
from moyupai import *
from muacloud import *
from log import *

if __name__ == '__main__':

    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(executable_path = chromedriver)

    # three webs
    gamekegs(driver)
    moyupai(driver)
    muacloud(driver)