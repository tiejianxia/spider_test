#用python3的pip安装selenium模块：py -3 -m pip install selenium
#下载chromedriver.exe，版本需要和chrome版本相对应，放在python安装目录下

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime

#使用chromedriver的无头模式
chrome_options = Options()
chrome_options.add_argument('--headless')
#chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(chrome_options=chrome_options)

#获取当前时间的字符串
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
nowTime = nowTime.replace(' ','_').replace(':','-')
#访问地址，截屏
#driver.get('https://www.douyu.com/directory/all')
driver.get('https://www.douyu.com/g_wzry')
driver.save_screenshot('E:\\script\\spider\\screenshot\\screenshot\\' + nowTime + '.png')
driver.quit()