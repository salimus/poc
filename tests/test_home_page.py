from selenium import webdriver
import unittest
import time
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from senegence.pages.HomePage import HomePage
from senegence.pages.FindDist import FindDist
from senegence.pages.ProductsForMen import ProductsForMen


class Home(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/salimkadirov/Documents/senegence/drivers/chromedriver")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    
    def test_find_distributor(self):
        driver = self.driver
        driver.get("https://seneweb.senegence.com/us/")

        home_page = HomePage(driver)
        home_page.click_connect_now()
        time.sleep(3)

        find_distr = FindDist(driver)
        assert "Find A Distributor - SeneGence International" in driver.title

        iframe = driver.find_element_by_xpath("//*[@id='left_col']/div[2]/iframe")
        driver.switch_to.frame(iframe)
        find_distr.enter_zip_code("92618")
        find_distr.click_find_zip_code() 
        time.sleep(3)
        name = find_distr.dist_full_name()
        self.assertEqual(name, "Lisa Bernstein")
        id = find_distr.dist_id_number()
        self.assertEqual(id, "Lisa Bernstein Distributor ID: 298564")
        print(id)
        time.sleep(3)

    def test_products_for_men(self):
        driver = self.driver
        driver.get("https://seneweb.senegence.com/us/")
        
        home_page = HomePage(driver)
        home_page.menu_products()
        products_for_men = ProductsForMen(driver)
        products_for_men.for_men_link()
        assert "SeneGence For Men - SeneGence International" in driver.title
        
        print(products_for_men.product_list())
        number_of_products = products_for_men.product_list()
        self.assertEqual(number_of_products, 3)
        
        products_for_men.shaving_cream()
        time.sleep(2)
        
        self.assertEqual(products_for_men.product_title(), "Soothing Shave Cream")
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../reports"))
