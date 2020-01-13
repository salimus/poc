# from selenium import webdriver
# import unittest
# import time

# class FindDistributor(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome(executable_path="/Users/salimkadirov/Documents/senegence/drivers/chromedriver")
#         self.driver.implicitly_wait(10)
#         self.driver.maximize_window()
    
#     def test_find_distributor(self):
#         driver = self.driver
#         driver.get("https://seneweb.senegence.com/us/")
#         assert "SeneGence® - The Official Site of SeneGence International, Inc." in driver.title
#         # self.assertIn("SeneGence® - The Official Site of SeneGence International, Inc.", driver.title)
#         # driver.find_element_by_id("2872").click()
#         # driver.find_element_by_xpath("//*[@id='site']/header[2]/div/div[2]/div/nav[1]/ul/li[6]/a").click()
#         # time.sleep(3)
#         # driver.switch_to.window("blank")
#         time.sleep(2)

#     def tearDown(self):
#         self.driver.close()


# if __name__ == "__main__":
#     unittest.main()
