import warnings
warnings.filterwarnings('ignore')
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import requests


class GetRoot(unittest.TestCase):
    options = Options()
    # ヘッドレスモードで起動
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)

    @classmethod
    def setUpClass(cls):
        # Seleniumの公式HPを指定
        cls.base_url = "https://www.seleniumhq.org/"
        cls.driver.implicitly_wait(30)
        cls.verificationErrors = []
        cls.accept_next_alert = True
        cls.driver.get(cls.base_url)

    @pytest.mark.parametrize()
    def test_get_page(self):
        driver = self.driver
        # HTTPステータスを確認
        r = requests.get(driver.current_url)
        self.assertEqual(r.status_code, 200)

        # ページのタイトルをチェック
        title_target = "Selenium - Web Browser Automation"
        print(driver.title)
        self.assertEqual(title_target, driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
