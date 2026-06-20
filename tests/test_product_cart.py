import allure

from pages.home_page import HomePage
from pages.cart_page import CartPage


@allure.feature("购物车")
@allure.story("搜索商品后加入购物车并校验")
def test_add_product_to_cart_and_verify(driver, base_url):
    """
    测试目标：
    验证用户可以搜索 iPhone，将商品加入购物车，并在购物车中看到该商品。

    断言重点：
    1. 商品详情页名称包含 iPhone；
    2. 商品价格不为空；
    3. Add to Cart 操作返回成功信号；
    4. 购物车中包含 iPhone；
    5. 购物车商品数量为 1。

    注意：
    TutorialsNinja Demo 的加入购物车成功提示有时不稳定，
    因此这里不只依赖固定文案 "Success: You have added"，
    而是接受 product_page.add_to_cart() 返回的任意 Success 成功信号。
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

    assert success_message.startswith("Success"), (
        f"期望商品加入购物车成功，实际返回信息为：{success_message}"
    )

    cart_page = CartPage(driver, base_url).open_cart()

    assert cart_page.is_product_in_cart("iPhone"), (
        f"期望购物车中包含 iPhone，实际商品为：{cart_page.get_product_names()}"
    )

    assert cart_page.get_first_quantity() == "1", (
        "期望购物车中第一件商品数量为 1。"
    )

