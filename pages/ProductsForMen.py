class ProductsForMen():

    def __init__(self, driver):
        self.driver = driver

        self.senegence_for_men_link  = "//*[@id='right_col']/nav/ul/li[4]/a"
        self.products = "//*[@id='ProductCategoryDiv']"
        self.item = "//div[@class='categoryChildDiv productListChild']"
        self.cream = "//*[@id='ProductCategoryDiv']/div[2]/a/div[2]/p"
        self.title = "h1"
    

    def for_men_link(self):
        self.driver.find_element_by_xpath(self.senegence_for_men_link).click()

    def product_list(self):
        items = self.driver.find_elements_by_xpath(self.item)
        return len(items)
    
    def shaving_cream(self):
        self.driver.find_element_by_xpath(self.cream).click()

    def product_title(self):
        pt = self.driver.find_element_by_tag_name(self.title).text
        return pt       