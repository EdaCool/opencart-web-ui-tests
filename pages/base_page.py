import logging
from urllib.parse import urljoin

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger(__name__)


class BasePage:
    """
    Page Object 基类。

    所有页面类都继承 BasePage。
    它封装了常见操作，例如：
    1. 打开页面；
    2. 等待元素可见；
    3. 等待元素可点击；
    4. 点击元素；
    5. 输入文本；
    6. 获取文本；
    7. 获取多个元素。

    这样做的好处：
    - 测试用例不用直接写复杂的 Selenium 等待逻辑；
    - 页面操作可以复用；
    - 代码更清晰，更接近真实自动化测试项目结构。
    """

    DEFAULT_TIMEOUT = 10

    def __init__(self, driver, base_url):
        """
        初始化页面对象。

        :param driver: Selenium WebDriver 浏览器对象
        :param base_url: 被测系统基础地址
        """
        self.driver = driver
        self.base_url = base_url

    def open(self, path=""):
        """
        打开页面。

        :param path: 相对路径，例如 index.php?route=account/login
        """
        url = urljoin(self.base_url, path)
        logger.info("Open page: %s", url)
        self.driver.get(url)

    def wait_visible(self, locator, timeout=None):
        """
        等待元素可见。

        :param locator: 元素定位器，例如 (By.ID, "input-email")
        :param timeout: 最长等待时间
        :return: WebElement
        """
        wait_time = timeout or self.DEFAULT_TIMEOUT
        logger.info("Wait visible: %s", locator)
        return WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout=None):
        """
        等待元素可点击。

        :param locator: 元素定位器
        :param timeout: 最长等待时间
        :return: WebElement
        """
        wait_time = timeout or self.DEFAULT_TIMEOUT
        logger.info("Wait clickable: %s", locator)
        return WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable(locator)
        )

    def find_all(self, locator, timeout=None):
        """
        等待并返回多个元素。

        :param locator: 元素定位器
        :param timeout: 最长等待时间
        :return: WebElement 列表
        """
        wait_time = timeout or self.DEFAULT_TIMEOUT
        logger.info("Find all elements: %s", locator)
        return WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator):
        """
        点击元素。

        :param locator: 元素定位器
        """
        element = self.wait_clickable(locator)
        logger.info("Click element: %s", locator)
        element.click()

    def type_text(self, locator, text, clear=True):
        """
        输入文本。

        :param locator: 元素定位器
        :param text: 要输入的文本
        :param clear: 输入前是否清空原内容
        """
        element = self.wait_visible(locator)
        if clear:
            element.clear()
        logger.info("Type text into %s: %s", locator, text)
        element.send_keys(text)

    def get_text(self, locator):
        """
        获取元素文本。

        :param locator: 元素定位器
        :return: 文本内容
        """
        element = self.wait_visible(locator)
        text = element.text
        logger.info("Get text from %s: %s", locator, text)
        return text

