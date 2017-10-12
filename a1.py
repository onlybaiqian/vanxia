#coding:utf-8

from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
dr.implicitly_wait(15)
dr.maximize_window()
dr.get("http://zcj.hnaic.gov.cn/")
dr.find_element_by_xpath("//*[@id='mainLeft']/div[3]/div/ul/li[1]/div[2]/a/font").click()
# dr.find_element_by_link_text("名称核准").click()
dr.switch_to_window(dr.window_handles[-1])
imgurl =dr.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]").text
print(dr.find_element_by_xpath("/html/body/table/tbody/tr[3]/td[2]").text)
print(dr.find_element_by_xpath("/html/body/table/tbody/tr[4]/td[2]").text)
print(dr.find_element_by_xpath("/html/body/table/tbody/tr[5]/td[2]").text)
print(dr.find_element_by_xpath("/html/body/table/tbody/tr[6]/td[2]").text)
print(imgurl)

js='window.open("https://www.sogou.com")'
dr.execute_script(js)