# OpenCart Web 自动化测试用例

## TC001 搜索存在的商品

| 字段 | 内容 |
|---|---|
| 用例编号 | TC001 |
| 用例标题 | 搜索存在的商品 iPhone |
| 前置条件 | 被测网站可访问 |
| 测试数据 | iPhone |
| 测试步骤 | 1. 打开首页；2. 输入 iPhone；3. 点击搜索 |
| 预期结果 | 搜索结果中出现 iPhone 商品 |
| 自动化脚本 | `tests/test_search.py::test_search_existing_product` |

---

## TC002 搜索不存在的商品

| 字段 | 内容 |
|---|---|
| 用例编号 | TC002 |
| 用例标题 | 搜索不存在的商品 |
| 前置条件 | 被测网站可访问 |
| 测试数据 | not-exist-product-xyz |
| 测试步骤 | 1. 打开首页；2. 输入不存在商品名；3. 点击搜索 |
| 预期结果 | 页面提示没有匹配商品 |
| 自动化脚本 | `tests/test_search.py::test_search_non_existing_product` |

---

## TC003 商品详情校验

| 字段 | 内容 |
|---|---|
| 用例编号 | TC003 |
| 用例标题 | 搜索 iPhone 后进入商品详情页 |
| 前置条件 | 被测网站可访问 |
| 测试数据 | iPhone |
| 测试步骤 | 1. 搜索 iPhone；2. 点击 iPhone 商品；3. 查看商品详情 |
| 预期结果 | 商品详情页标题包含 iPhone，价格不为空 |
| 自动化脚本 | `tests/test_product_cart.py::test_add_product_to_cart_and_verify` |

---

## TC004 加入购物车

|字段|内容|
|---|---|
|用例编号|TC004|
|用例标题|将 iPhone 加入购物车|
|前置条件|已进入 iPhone 商品详情页|
|测试数据|商品：iPhone；数量：1|
|测试步骤|1. 记录加入购物车前的购物车汇总信息；2. 输入数量 1；3. 点击 Add to Cart；4. 等待加入购物车成功信号|
|预期结果|页面出现加入购物车成功提示，或右上角购物车数量 / 金额发生变化|
|自动化脚本|`tests/test_product_cart.py::test_add_product_to_cart_and_verify`|
|备注|由于 Demo 页面成功提示可能存在加载延迟，因此自动化脚本不只依赖 `.alert-success`，还会结合购物车汇总信息变化进行判断。|

---

## TC005 购物车商品校验

|字段|内容|
|---|---|
|用例编号|TC005|
|用例标题|校验购物车中的商品名称和数量|
|前置条件|iPhone 已加入购物车|
|测试数据|商品：iPhone；数量：1|
|测试步骤|1. 打开购物车页面；2. 获取购物车中的商品名称；3. 获取商品数量；4. 校验商品名称和数量|
|预期结果|购物车中包含 iPhone，且商品数量为 1|
|自动化脚本|`tests/test_product_cart.py::test_add_product_to_cart_and_verify`|
|备注|购物车页面中的最终商品数据是本用例最关键的业务校验点。|

---

## TC006 错误账号密码登录

| 字段 | 内容 |
|---|---|
| 用例编号 | TC006 |
| 用例标题 | 使用错误账号密码登录 |
| 前置条件 | 被测网站可访问 |
| 测试数据 | not_exist_user@example.com / wrong_password_123 |
| 测试步骤 | 1. 打开登录页；2. 输入错误邮箱；3. 输入错误密码；4. 点击登录 |
| 预期结果 | 页面出现 Warning 登录失败提示 |
| 自动化脚本 | `tests/test_login.py::test_login_with_invalid_credentials` |
