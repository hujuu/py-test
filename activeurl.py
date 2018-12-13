import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import requests


class GetRoot(unittest.TestCase):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)

    @classmethod
    def setUpClass(cls):
        cls.base_url = "https://www.seleniumhq.org/"
        cls.driver.implicitly_wait(30)
        cls.verificationErrors = []
        cls.accept_next_alert = True
        cls.driver.get(cls.base_url)

    @pytest.mark.parametrize()
    def test_link(self):
        driver = self.driver
        # ページ内のaタグの情報を全て取得
        links = driver.find_elements_by_css_selector('a')
        # 各リンクの確認処理
        for checks in links:
            # セレクターで取得した情報からリンク先URLを取得
            link_url = checks.get_attribute("href")
            if "https" in str(link_url):
                print(link_url)
                # リンク切れのチェックとして、遷移先のHTTPステータスを確認
                r = requests.get(link_url)
                self.assertEqual(r.status_code, 200, link_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
