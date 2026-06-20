from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    """
    搜索结果页 Page Object。

    负责封装：
    1. 获取搜索结果商品名称；
    2. 点击指定商品；
    3. 判断是否存在无结果提示。
    """

    PRODUCT_NAMES = (By.CSS_SELECTOR, ".product-layout .caption h4 a")
    CONTENT_PARAGRAPHS = (By.CSS_SELECTOR, "#content p")

    def get_product_names(self):
        """
        获取搜索结果中的所有商品名称。

        :return: 商品名称列表
        """
        elements = self.find_all(self.PRODUCT_NAMES)
        return [element.text.strip() for element in elements if element.text.strip()]

    def click_product_by_name(self, product_name):
        """
        根据商品名称点击商品。

        :param product_name: 商品名称，例如 iPhone
        :return: ProductPage 商品详情页对象
        """
        elements = self.find_all(self.PRODUCT_NAMES)

        for element in elements:
            if product_name.lower() in element.text.lower():
                element.click()

                from pages.product_page import ProductPage
                return ProductPage(self.driver, self.base_url)

        raise AssertionError(f"未找到商品：{product_name}")

    def get_content_texts(self):
        """
        获取内容区域中的提示文本。

        :return: 文本列表
        """
        elements = self.find_all(self.CONTENT_PARAGRAPHS)
        return [element.text.strip() for element in elements if element.text.strip()]

    def has_no_result_message(self):
        """
        判断页面是否出现无搜索结果提示。

        :return: True / False
        """
        return "There is no product that matches the search criteria." in self.driver.page_source

