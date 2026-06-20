import allure

from pages.login_page import LoginPage


@allure.feature("用户登录")
@allure.story("错误账号密码登录")
def test_login_with_invalid_credentials(driver, base_url):
    """
    测试目标：
    验证用户输入错误邮箱和密码时，系统给出登录失败提示。

    测试步骤：
    1. 打开登录页；
    2. 输入不存在的邮箱；
    3. 输入错误密码；
    4. 点击登录；
    5. 校验页面出现 Warning 提示。
    """
    login_page = LoginPage(driver, base_url).open_login()

    login_page.login(
        email="not_exist_user@example.com",
        password="wrong_password_123"
    )

    warning_message = login_page.get_warning_message()

    assert "Warning" in warning_message, (
        f"期望出现登录失败 Warning 提示，实际提示为：{warning_message}"
    )

