# 常见问题排查

## 1. pytest 找不到测试用例

### 现象

执行：

```bash
pytest
```

显示 collected 0 items。

### 原因

pytest 默认只识别：

- `test_` 开头的文件；
    
- `test_` 开头的函数。
    

### 解决

确认文件名类似：

```text
test_search.py
```

确认函数名类似：

```python
def test_search_existing_product():
    pass
```

---

## 2. Selenium 无法启动 Chrome

### 现象

报错中出现：

```text
cannot find Chrome binary
```

或：

```text
session not created
```

### 可能原因

1. WSL2 中没有安装 Chrome；
    
2. Chrome 版本异常；
    
3. Selenium 无法匹配浏览器驱动。
    

### 解决

检查 Chrome：

```bash
google-chrome --version
```

如果没有安装，执行：

```bash
cd /tmp
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt update
sudo apt install -y ./google-chrome-stable_current_amd64.deb
```

---

## 3. 页面标题是 Just a moment...

### 现象

访问 OpenCart 官方 Demo 时，页面标题变成：

```text
Just a moment...
```

### 原因

页面进入 Cloudflare / 防机器人验证。

### 解决

不要使用：

```text
https://demo.opencart.com
```

改用：

```text
https://tutorialsninja.com/demo/
```

---

## 4. 元素定位失败

### 现象

报错类似：

```text
TimeoutException
```

### 原因

1. 页面加载慢；
    
2. 元素定位器写错；
    
3. 页面结构变化；
    
4. 被测网站返回了异常页面。
    

### 解决

1. 先手动打开网页确认页面是否正常；
    
2. 使用浏览器开发者工具检查元素；
    
3. 修改 `pages/` 目录中的定位器；
    
4. 不要直接在测试用例里乱改定位器。
    

---

## 5. Allure 命令不可用

### 现象

执行：

```bash
allure
```

提示 command not found。

### 解决

使用 npx：

```bash
sudo apt install -y default-jre nodejs npm
npx allure-commandline generate reports/allure-results -o reports/allure-report --clean
```

---

## 6. GitHub push 失败

### 现象

HTTPS 连接 GitHub 失败。

### 解决

使用 SSH：

```bash
git remote set-url origin git@github.com:你的GitHub用户名/opencart-web-ui-tests.git
ssh -T git@github.com
git push
```
## 7.点击 Add to Cart 后等待 `.alert-success` 超时  
  
### 现象  
  
购物车用例失败，日志显示：  
  
```text  
Click element: ('id', 'button-cart')  
Wait visible: ('css selector', '.alert-success')  
TimeoutException
```
### 原因分析

该问题说明 Selenium 已经成功点击了 Add to Cart 按钮，但脚本没有在指定时间内等到 `.alert-success` 成功提示。

这不一定代表加入购物车失败，也可能是：

1. 成功提示出现较慢；
2. 成功提示 DOM 结构发生变化；
3. 商品已经加入购物车，但提示没有及时出现；
4. 页面通过 AJAX 更新购物车数量，但没有弹出明显提示；
5. headless Chrome 下页面行为和普通浏览器略有差异。

### 解决方案

不要只依赖 `.alert-success` 作为唯一成功标准。

更稳健的判断方式是：

1. 点击 Add to Cart 前，先记录右上角购物车汇总信息；
2. 点击 Add to Cart；
3. 优先等待 `.alert-success`；
4. 如果成功提示没有出现，再判断右上角购物车数量或金额是否变化；
5. 最后进入购物车页面，校验商品名称和数量。

### 总结

Web UI 自动化中，弹窗提示属于辅助校验，最终业务结果才是更关键的校验点。

对于加入购物车流程，最终校验应以购物车页面中的商品名称和数量为准。


