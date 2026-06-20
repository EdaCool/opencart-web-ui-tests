from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    """
    购物车页 Page Object。

    负责封装：
    1. 打开购物车页面；
    2. 获取购物车中的商品名称；
    3. 获取商品数量；
    4. 判断指定商品是否在购物车中。
    """

    CART_ROUTE = "index.php?route=checkout/cart"
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".table-responsive tbody tr td.text-left a")
    QUANTITY_INPUTS = (By.CSS_SELECTOR, "input[name^='quantity']")

    def open_cart(self):
        """
        打开购物车页面。
        """
        self.open(self.CART_ROUTE)
        return self

    def get_product_names(self):
        """
        获取购物车中所有商品名称。

        :return: 商品名称列表
        """
        elements = self.find_all(self.PRODUCT_NAMES)
        return [element.text.strip() for element in elements if element.text.strip()]

    def is_product_in_cart(self, product_name):
        """
        判断指定商品是否在购物车中。

        :param product_name: 商品名称
        :return: True / False
        """
        product_names = self.get_product_names()
        return any(product_name.lower() in name.lower() for name in product_names)

    def get_first_quantity(self):
        """
        获取购物车第一件商品的数量。

        :return: 数量字符串，例如 "1"
        """
        elements = self.find_all(self.QUANTITY_INPUTS)
        return elements[0].get_attribute("value")

