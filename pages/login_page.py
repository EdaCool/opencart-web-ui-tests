from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    登录页 Page Object。

    本项目不依赖真实账号。
    因此重点测试错误账号密码登录时，系统是否给出正确提示。
    """

    LOGIN_ROUTE = "index.php?route=account/login"
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Login']")
    WARNING_ALERT = (By.CSS_SELECTOR, ".alert-danger")

    def open_login(self):
        """
        打开登录页。
        """
        self.open(self.LOGIN_ROUTE)
        return self

    def login(self, email, password):
        """
        执行登录操作。

        :param email: 邮箱
        :param password: 密码
        """
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_warning_message(self):
        """
        获取登录失败提示。
        """
        return self.get_text(self.WARNING_ALERT)

