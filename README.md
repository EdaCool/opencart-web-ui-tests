# OpenCart 电商系统 Web 自动化回归测试

## 1. 项目简介

本项目基于 TutorialsNinja OpenCart Demo 电商系统，使用 Python + Selenium + pytest + Page Object + Allure 搭建 Web UI 自动化测试框架。

项目围绕电商系统核心业务流程进行自动化回归测试，包括：

- 首页访问；
- 商品搜索；
- 商品详情校验；
- 加入购物车；
- 购物车商品校验；
- 登录失败提示校验。

项目目标不是简单录制脚本，而是按照真实测试项目的方式组织代码和文档，体现从测试计划、测试用例设计、自动化脚本开发、测试执行、报告生成到缺陷记录的完整流程。

---

## 2. 技术栈

| 技术 | 用途 |
|---|---|
| Python | 自动化脚本开发语言 |
| Selenium | 浏览器自动化 |
| pytest | 测试用例组织与执行 |
| Page Object | 页面对象封装，降低代码重复 |
| Allure | 测试报告生成 |
| Git / GitHub | 版本管理与项目展示 |
| WSL2 | Linux 开发测试环境 |

---

## 3. 被测系统

本项目使用 TutorialsNinja OpenCart Demo：

```text
https://tutorialsninja.com/demo/
```

说明：

最初尝试过本地部署 OpenCart 和 OpenCart 官方 Demo，但本地部署出现 OpenCart Twig 模板错误，官方 Demo 又会对自动化浏览器返回 Cloudflare 验证页 `Just a moment...`。

因此，最终选择 TutorialsNinja Demo 作为更稳定、更适合自动化练习的 OpenCart 测试环境。

---

## 4. 项目结构

```text
opencart-web-ui-tests/
├── README.md
├── requirements.txt
├── pytest.ini
├── docs/
├── pages/
├── tests/
├── reports/
└── logs/
```

---

## 5. 自动化测试范围

|模块|测试内容|
|---|---|
|首页|打开首页，验证页面可访问|
|商品搜索|搜索存在商品、搜索不存在商品|
|商品详情|校验商品名称、商品价格|
|购物车|加入购物车、校验商品名称和数量|
|登录|错误账号密码登录提示|

---

## 6. 环境准备

### 6.1 创建虚拟环境

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 6.2 安装依赖

```bash
pip install -r requirements.txt
```

### 6.3 确认 Chrome

```bash
google-chrome --version
```

---

## 7. 运行测试

运行全部测试：

```bash
pytest
```

生成 Allure 原始结果：

```bash
pytest --alluredir=reports/allure-results
```

生成 Allure HTML 报告：

```bash
npx allure-commandline generate reports/allure-results -o reports/allure-report --clean
```

打开 Allure 报告：

```bash
npx allure-commandline open reports/allure-report
```

---

## 8. 测试报告与截图

测试失败时，框架会自动保存截图到：

```text
reports/screenshots/
```

执行日志保存在：

```text
logs/test_execution.log
```

---

## 9. 项目亮点

1. 使用 Page Object 模式封装页面对象；
    
2. 使用 pytest fixture 管理浏览器生命周期；
    
3. 使用显式等待提升自动化稳定性；
    
4. 针对加入购物车流程，不仅校验成功提示，还结合购物车数量变化和购物车页面最终数据进行验证，提升了自动化用例稳定性。

5. 测试失败时自动截图；
    
6. 使用 Allure 生成可视化测试报告；
    
7. 包含测试计划、测试用例、缺陷记录等完整测试文档；
    
8. 适合作为软件测试求职作品集项目。
    

---

## 10. 后续优化方向

1. 增加用户注册流程测试；
    
2. 增加参数化测试数据；
    
3. 增加多浏览器执行；
    
4. 接入 GitHub Actions；
    
5. 增加 HTML / JUnit 测试报告；
    
6. 增加失败重试机制；
    
7. 增加更多购物车和结算流程测试。  

