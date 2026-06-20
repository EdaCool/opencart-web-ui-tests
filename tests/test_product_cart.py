import allure

from pages.home_page import HomePage
from pages.cart_page import CartPage


@allure.feature("购物车")
@allure.story("搜索商品后加入购物车并校验")
def test_add_product_to_cart_and_verify(driver, base_url):
    """
    测试目标：
    验证用户可以搜索 iPhone，将商品加入购物车，并在购物车中看到该商品。

    测试步骤：
    1. 打开首页；
    2. 搜索 iPhone；
    3. 点击搜索结果中的 iPhone；
    4. 校验商品详情页名称包含 iPhone；
    5. 校验商品价格不为空；
    6. 输入购买数量 1；
    7. 点击加入购物车；
    8. 校验成功提示；
    9. 打开购物车页面；
    10. 校验购物车中包含 iPhone；
    11. 校验商品数量为 1。
    """
    home_page = HomePage(driver, base_url).open_home()

    search_results_page = home_page.search("iPhone")

    product_page = search_results_page.click_product_by_name("iPhone")

    assert "iPhone" in product_page.get_product_name(), (
        "期望商品详情页标题包含 iPhone。"
    )

    assert product_page.get_product_price(), (
        "期望商品详情页价格不为空。"
    )

    success_message = product_page.add_to_cart(quantity=1)

    assert "Success: You have added" in success_message, (
        f"期望出现加入购物车成功提示，实际提示为：{success_message}"
    )

    cart_page = CartPage(driver, base_url).open_cart()

    assert cart_page.is_product_in_cart("iPhone"), (
        f"期望购物车中包含 iPhone，实际商品为：{cart_page.get_product_names()}"
    )

    assert cart_page.get_first_quantity() == "1", (
        "期望购物车中第一件商品数量为 1。"
    )

