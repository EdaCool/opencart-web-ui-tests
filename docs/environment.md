# 环境配置文档

## 1. 本机环境

| 项目 | 配置 |
|---|---|
| 操作系统 | Windows 10 |
| Linux 环境 | WSL2 Ubuntu |
| Python | Python 3 |
| 浏览器 | Google Chrome |
| 版本管理 | Git |
| 远程仓库 | GitHub SSH |

---

## 2. 为什么使用 WSL2？

使用 WSL2 的原因：

1. Linux 环境更接近真实服务器和 CI 环境；
2. Python 虚拟环境管理更方便；
3. Git、pytest、Selenium 等工具链更稳定；
4. 方便后续扩展到 CI/CD。

---

## 3. 为什么使用虚拟环境？

Python 虚拟环境的作用：

1. 隔离当前项目依赖；
2. 避免污染系统 Python；
3. 避免多个项目之间依赖冲突；
4. 方便别人根据 requirements.txt 复现项目。

---

## 4. 为什么使用 SSH 连接 GitHub？

当前网络环境下，WSL2 无法稳定通过 HTTPS 连接 GitHub，因此改用 SSH 协议进行 pull / push。

SSH 的好处：

1. 不需要每次输入账号密码；
2. 适合长期开发；
3. 配置成功后推送更稳定。

---

## 5. 被测环境说明

被测地址：

```text
https://tutorialsninja.com/demo/
```

选择原因：

1. 页面结构类似 OpenCart；
    
2. 包含典型电商流程；
    
3. 不需要本地部署；
    
4. 更适合 Selenium 自动化练习；
    
5. 避免 OpenCart 官方 Demo 的 Cloudflare 拦截问题。  

