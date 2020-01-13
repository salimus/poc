class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.connect_now_btn = "//*[@id='site']/section[3]/div/div/div/div/div/div/div[3]/div/p[3]/a"
        self.products = "//*[@id='site']/header[2]/div/div[2]/div/nav[1]/ul/li[5]/a"

    
    def click_connect_now(self):
        self.driver.find_element_by_xpath(self.connect_now_btn).click()
        
    def menu_products(self):
        self.driver.find_element_by_xpath(self.products).click()