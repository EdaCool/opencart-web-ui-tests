# 缺陷记录样例

> 说明：以下缺陷为项目展示用样例，用于体现测试人员发现、记录、分析问题的能力。

---

## BUG001 OpenCart 官方 Demo 被 Cloudflare 拦截

| 字段 | 内容 |
|---|---|
| 缺陷编号 | BUG001 |
| 缺陷标题 | Selenium 访问 OpenCart 官方 Demo 时进入 Cloudflare 验证页 |
| 发现环境 | WSL2 + Chrome Headless + Selenium |
| 问题地址 | https://demo.opencart.com |
| 严重程度 | Major |
| 优先级 | Medium |
| 复现步骤 | 1. 使用 Selenium 打开官方 Demo；2. 获取页面标题 |
| 实际结果 | 页面标题为 `Just a moment...` |
| 预期结果 | 应进入 OpenCart 商城首页 |
| 初步分析 | 官方 Demo 存在 Cloudflare / 防机器人验证，自动化浏览器被识别 |
| 处理方案 | 不使用官方 Demo，改用 TutorialsNinja Demo 作为自动化练习环境 |

---

## BUG002 本地部署 OpenCart 出现 Twig 模板错误

| 字段 | 内容 |
|---|---|
| 缺陷编号 | BUG002 |
| 缺陷标题 | 本地访问 OpenCart 返回 Twig 模板错误 |
| 发现环境 | Windows 10 + WSL2 + Apache + PHP |
| 复现步骤 | 1. 本地部署 OpenCart；2. 执行 `curl http://localhost` |
| 实际结果 | 返回 OpenCart Twig 模板错误 |
| 预期结果 | 应正常进入安装页面或商城首页 |
| 初步分析 | Apache 和 PHP 已正常工作，但 OpenCart 安装或配置不完整 |
| 处理方案 | 本项目不继续投入本地部署，优先完成 Web UI 自动化测试主线 |

---

## BUG003 搜索结果页元素定位可能受页面结构变化影响

| 字段 | 内容 |
|---|---|
| 缺陷编号 | BUG003 |
| 缺陷标题 | 搜索结果页商品元素定位存在维护风险 |
| 发现环境 | TutorialsNinja Demo |
| 问题描述 | 如果页面 CSS 结构发生变化，`.product-layout .caption h4 a` 定位器可能失效 |
| 影响范围 | 商品搜索、商品详情、购物车流程 |
| 处理建议 | 将定位器集中维护在 Page Object 中，页面变化时只修改页面类，不修改测试用例 |

