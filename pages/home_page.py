from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    """
    首页 Page Object。

    负责封装首页上的操作：
    1. 打开首页；
    2. 输入搜索关键词；
    3. 点击搜索按钮。
    """

    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")

    def open_home(self):
        """
        打开首页。
        """
        self.open("")
        return self

    def search(self, keyword):
        """
        搜索商品。

        :param keyword: 商品关键词，例如 iPhone
        :return: SearchResultsPage 搜索结果页对象
        """
        self.type_text(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)

        from pages.search_results_page import SearchResultsPage
        return SearchResultsPage(self.driver, self.base_url)

