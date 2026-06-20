from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class ProductPage(BasePage):
    """
    商品详情页 Page Object。

    负责封装：
    1. 获取商品名称；
    2. 获取商品价格；
    3. 设置购买数量；
    4. 点击加入购物车；
    5. 获取加入购物车后的结果。
    """

    PRODUCT_NAME = (By.CSS_SELECTOR, "#content h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content ul.list-unstyled h2")
    QUANTITY_INPUT = (By.ID, "input-quantity")
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")

    # OpenCart / TutorialsNinja 中成功提示通常是这个结构
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")

    # 页面右上角购物车数量，例如：0 item(s) - $0.00
    CART_TOTAL = (By.ID, "cart-total")

    def get_product_name(self):
        """
        获取商品名称。
        """
        return self.get_text(self.PRODUCT_NAME)

    def get_product_price(self):
        """
        获取商品价格。
        """
        return self.get_text(self.PRODUCT_PRICE)

    def get_cart_total_text(self):
        """
        获取右上角购物车汇总文本。

        示例：
        0 item(s) - $0.00
        1 item(s) - $123.20
        """
        return self.get_text(self.CART_TOTAL)

    def add_to_cart(self, quantity=1):
        """
        将商品加入购物车。

        这里采用更稳健的判断方式：
        1. 输入数量；
        2. 点击 Add to Cart；
        3. 优先等待成功提示 .alert-success；
        4. 如果成功提示没出现，再检查购物车数量是否变化；
        5. 如果两种成功信号都没有，再抛出异常。

        :param quantity: 商品数量，默认 1
        :return: 成功提示文本，或者根据购物车数量变化构造的成功信息
        """
        before_cart_total = self.get_cart_total_text()

        self.type_text(self.QUANTITY_INPUT, str(quantity))
        self.click(self.ADD_TO_CART_BUTTON)

        # 第一种成功判断：等待页面出现成功提示
        try:
            success_element = WebDriverWait(self.driver, 20).until(
                lambda driver: driver.find_element(*self.SUCCESS_ALERT)
            )
            return success_element.text
        except TimeoutException:
            pass

        # 第二种成功判断：如果没有等到成功提示，则检查购物车数量是否变化
        try:
            after_cart_total = WebDriverWait(self.driver, 10).until(
                lambda driver: driver.find_element(*self.CART_TOTAL).text
            )
        except TimeoutException:
            after_cart_total = ""

        if after_cart_total and after_cart_total != before_cart_total:
            return f"Success: cart total changed from [{before_cart_total}] to [{after_cart_total}]"

        raise AssertionError(
            "点击 Add to Cart 后，没有出现成功提示，购物车数量也没有变化。"
            f"点击前购物车为：{before_cart_total}；"
            f"点击后购物车为：{after_cart_total}。"
        )
