import allure

from pages.home_page import HomePage


@allure.feature("商品搜索")
@allure.story("搜索存在的商品")
def test_search_existing_product(driver, base_url):
    """
    测试目标：
    验证用户在首页搜索 iPhone 后，搜索结果中包含 iPhone 商品。

    测试步骤：
    1. 打开首页；
    2. 输入关键词 iPhone；
    3. 点击搜索；
    4. 获取搜索结果商品名称；
    5. 断言结果中包含 iPhone。
    """
    home_page = HomePage(driver, base_url).open_home()

    search_results_page = home_page.search("iPhone")

    product_names = search_results_page.get_product_names()

    assert any("iPhone" in name for name in product_names), (
        f"期望搜索结果包含 iPhone，实际结果为：{product_names}"
    )


@allure.feature("商品搜索")
@allure.story("搜索不存在的商品")
def test_search_non_existing_product(driver, base_url):
    """
    测试目标：
    验证用户搜索不存在的商品时，系统显示无结果提示。

    测试步骤：
    1. 打开首页；
    2. 输入一个不存在的商品名；
    3. 点击搜索；
    4. 断言页面出现无结果提示。
    """
    home_page = HomePage(driver, base_url).open_home()

    search_results_page = home_page.search("not-exist-product-xyz")

    assert search_results_page.has_no_result_message(), (
        "期望页面显示无搜索结果提示，但实际页面没有出现该提示。"
    )

