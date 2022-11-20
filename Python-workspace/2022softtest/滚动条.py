from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# 访问网址
driver.get('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%86%AC%E5%A5%A5%E4%BC%9A&fenlei=256&rsv_pq=c61031d20000416d&rsv_t=34329gsBNwKJFQ%2Bmyc957YqRGPTtQjrdzsvJ%2Fpfwl4Dta6B4YxTZjnzxVE8&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=13&rsv_sug1=15&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=4248&rsv_sug4=4635')
# 等待3秒
sleep(3)
# 滚动到底部
driver.execute_script("document.documentElement.scrollTop=10000")
# 等待1秒
sleep(3)
driver.execute_script("document.documentElement.scrollTop=0")
sleep(3)
# 关闭所有页面
driver.quit()
