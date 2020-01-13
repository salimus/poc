class FindDist():

    def __init__(self, driver):
        self.driver = driver

        self.zip_code_textfield = "ssd_input_zip_code"
        self.zip_code_find_btn  = "ssd_btn_zip_search"
        self.iframe_xpath = "//*[@id='left_col']/div[2]/iframe"
        self.dist_name = "//*[@id='ssd_find_distributor_result_list']/div[1]/ul/li[1]/strong"
        self.dist_id = "//*[@id='ssd_find_distributor_result_list']/div[1]/ul/li[1]"
    
    def enter_zip_code(self, zip_code):
        self.driver.find_element_by_id(self.zip_code_textfield).send_keys(zip_code)

    def click_find_zip_code(self):
        self.driver.find_element_by_id(self.zip_code_find_btn).click()

    def iframe(self):
        self.driver.find_element_by_xpath(self.iframe_xpath)
    
    def dist_full_name(self):
        element = self.driver.find_element_by_xpath(self.dist_name).text
        return element
    
    def dist_id_number(self):
        el = self.driver.find_element_by_xpath(self.dist_id).text
        return el