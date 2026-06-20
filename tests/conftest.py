import os
import re
from pathlib import Path

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """
    自定义 pytest 命令行参数。

    使用示例：
    pytest --base-url=https://tutorialsninja.com/demo/
    pytest --headed
    """
    parser.addoption(
        "--base-url",
        action="store",
        default=os.getenv("BASE_URL", "https://tutorialsninja.com/demo/"),
        help="被测系统基础地址，默认使用 TutorialsNinja OpenCart Demo",
    )

    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="是否以有界面模式运行浏览器。WSL2 中默认建议使用 headless。",
    )


@pytest.fixture
def base_url(request):
    """
    提供被测系统基础地址。

    测试用例中只需要声明 base_url 参数，即可使用。
    """
    return request.config.getoption("--base-url")


@pytest.fixture
def driver(request):
    """
    创建并销毁浏览器。

    pytest fixture 的作用：
    1. 测试开始前创建浏览器；
    2. 把浏览器对象传给测试用例；
    3. 测试结束后关闭浏览器。

    这样可以避免每个测试用例重复写浏览器初始化代码。
    """
    headed = request.config.getoption("--headed")

    chrome_options = Options()

    if not headed:
        chrome_options.add_argument("--headless=new")

    # WSL2 / Linux 环境下运行 Chrome 常用参数
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # 设置浏览器窗口大小，避免响应式布局导致元素变化
    chrome_options.add_argument("--window-size=1440,900")

    # 降低自动化提示带来的干扰
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")

    browser = webdriver.Chrome(options=chrome_options)
    browser.set_page_load_timeout(30)

    yield browser

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    pytest 钩子函数：测试失败时自动截图。

    作用：
    1. 如果测试失败；
    2. 并且当前测试使用了 driver；
    3. 自动保存截图到 reports/screenshots；
    4. 同时把截图附加到 Allure 报告中。
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver is None:
            return

        screenshots_dir = Path("reports/screenshots")
        screenshots_dir.mkdir(parents=True, exist_ok=True)

        safe_name = re.sub(r"[^a-zA-Z0-9_\\-\\.]", "_", item.nodeid)
        screenshot_path = screenshots_dir / f"{safe_name}.png"

        driver.save_screenshot(str(screenshot_path))

        allure.attach.file(
            str(screenshot_path),
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG,
        )


