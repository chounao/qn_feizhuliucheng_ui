from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.maximize_window()
driver.get("https://localhost/main/#/v4/trades")
print("打开网页")
time.sleep(1)
# driver.find_element_by_id("details-button").click()#点击高级
# # time.sleep(0.5)
# print("点击高级")
# # driver.find_element_by_link_text("继续前往192.168.3.36（不安全）").click()#点击继续前往
# driver.find_element_by_id("proceed-link").click()
# time.sleep(1)
# print("点击继续")
# driver.execute_script('localStorage.API_HOST = "true"')#控制台输入
# print("控制台输入")
# driver.refresh()#刷新
# print("等待广告和公告")
# time.sleep(15)


#判断双11公告
#先判断公告是否存在
try:
    driver.find_element_by_id("systemNotice") #公告ID
    driver.find_element_by_id("systemNoticeConfirm").click()
    # ActionChains.move_by_offset(1,1).click().perform()      #点击空白位置
    print("操作公告")

except:
    print("没有公告")
time.sleep(1)

try:
    driver.find_element_by_class_name("ant-modal-root") #广告
    print("操作广告")
    driver.find_element_by_xpath("//span[@class='anticon anticon-close ant-modal-close-icon']").click()
except:
    print("没有广告")

time.sleep(1)


driver.find_element_by_xpath("//div[@class='layout-top']//div[4]").click()#订单管理
time.sleep(1)
print("订单管理")
driver.find_element_by_class_name("layout-left-menu-title").click()#订单列表按钮
time.sleep(1)
print("订单列表")


driver.find_element_by_xpath("//div[contains(@class,'layout-left-menu-list')]//div[2]//div[1]//span[1]").click()#店铺评价
time.sleep(1)
print("店铺评价")



driver.find_element_by_xpath("//div[contains(@class,'layout-left-menu-item-list')]//div[1]").click()#评价管理
print("评价管理")
driver.refresh()#刷新
time.sleep(5)



# #中评
# driver.find_element_by_id("rc-tabs-0-tab-1").click()#中评
# time.sleep(1)
# print("中评")
# #差评
# driver.find_element_by_id("rc-tabs-0-tab-2").click()
# time.sleep(1)
# print("差评")
# driver.find_element_by_id("rc-tabs-0-tab-3").click()#已改好评
# time.sleep(1)
# print("已改好评")
# driver.find_element_by_id("rc-tabs-0-tab-4").click()#好评
# time.sleep(1)
# print("好评")
# driver.find_element_by_id("rc-tabs-0-tab-5").click()#回复买家评论
# time.sleep(1)
# print("回复")





class Abc():
    # print("----------自动开启评价按钮——————————————")
    def open_eva(self):
        text = driver.find_element_by_xpath("//div[contains(@class,'automatic_switch')]//span[contains(@class,'ant-switch-inner')]").text
        print(text)
        if text == "已开启":
            driver.find_element_by_xpath("//div[contains(@class,'automatic_switch')]//span[contains(@class,'ant-switch-inner')]").click()
            try:
                driver.find_element_by_class_name("ant-modal-content")
                print("弹窗展示")
                try:
                    driver.find_element_by_xpath("//button[contains(@class,'ant-btn ant-btn-primary')]")
                    driver.find_element_by_xpath("//button[contains(@class,'ant-btn ant-btn-primary')]").click()
                    print("关闭自动评价")
                except:
                    print("无法定位确定按钮")
                    try:
                        driver.find_element_by_xpath("//div[contains(@class,'ant-modal-footer')]//button[1]//span[1]")
                        driver.find_element_by_xpath("//div[contains(@class,'ant-modal-footer')]//button[1]//span[1]").click()
                    except:
                        print("无法定位取消按钮")
            except:
                print("无法定位弹窗")
        else:
            driver.find_element_by_xpath(
                "//div[contains(@class,'automatic_switch')]//span[contains(@class,'ant-switch-inner')]").click()
            print("自动评价开启")


    # print("---------中差评——————————————————")
    # 中差评提醒
    def open_sss(self):
        text = driver.find_element_by_xpath(
            "//div[contains(@class,'automatic_switch')]//span[contains(@class,'ant-switch-inner')]").text
        text2= driver.find_element_by_xpath("//div[contains(@class,'remind_switch')]//span[contains(@class,'ant-switch-inner')]").text
        if text == "已关闭" and text2 == "已关闭":
            print("———————————一键开启操作——————————")
            driver.find_element_by_xpath("//div[contains(@class,'remind_switch')]//span[contains(@class,'ant-switch-inner')]").click()
            print("开启操作")
            try:
                driver.find_element_by_class_name("ant-modal-content")
                print("弹窗展示")
                try:
                    driver.find_element_by_class_name("allOpen")
                    driver.find_element_by_class_name("allOpen").click()
                    print("一键开启")

                except:
                    print("找不到一键开启")
                    try:
                        driver.find_element_by_class_name("badOpen")
                        driver.find_element_by_class_name("badOpen").click()
                        print("只开启中差评")

                    except:
                        print("找不到只开启中差评")
                        try:
                            driver.find_element_by_class_name("close")
                            driver.find_element_by_class_name("close").click()
                            print("取消")

                        except:
                            print("NO FOUND")
            except:
                print("找不到确认开启弹窗")
            print(text,text2)
        elif text2 == "已关闭":
            print("———————————只开启中差评操作——————————")
            try:
                driver.find_element_by_xpath("//div[contains(@class,'remind_switch')]//span[contains(@class,'ant-switch-inner')]")
                print("定位按钮")
                driver.find_element_by_xpath("//div[contains(@class,'remind_switch')]//span[contains(@class,'ant-switch-inner')]").click()
                print("只开启")

            except:
                print("无法定位")
            print(text,text2)
        elif text2 == "已开启":
            print("———————————关闭操作——————————")
            driver.find_element_by_xpath("//div[contains(@class,'remind_switch')]//span[contains(@class,'ant-switch-inner')]").click()
            try:
                driver.find_element_by_xpath("//span[contains(@class,'phoneEditModalInfo')]")
                print("定位弹窗")
                driver.find_element_by_xpath("//button[contains(@class,'ant-btn ant-btn-primary')]").click()

                print("操作关闭")

            except:
                print("无法定位按钮")

                try:
                    driver.find_element_by_xpath("//div[contains(@class,'ant-modal-footer')]//button[1]")
                    driver.find_element_by_xpath("//div[contains(@class,'ant-modal-footer')]//button[1]").click()
                    print("取消关闭")

                except:
                        print("无法定位到取消按钮")

            print(text,text2)



    #列表页面勾选，发送短信，卖家备注，
    def ssss(self):
        time.sleep(5)
        pro_list = driver.find_elements_by_tag_name("tr")
        rowCount = 0
        for i in pro_list:
            texts = i.find_elements_by_class_name("Info")
            input_arr = i.find_elements_by_class_name("ant-checkbox-input")
            massage_arr = i.find_elements_by_class_name("fhd-icon-button")
            wb_br = i.find_elements_by_class_name("wb-br")
            for input in input_arr:
                    rowCount = rowCount + 1
                    print("第%d次操作"%rowCount)
                    selected = input.is_selected()#判断是否勾选
                    if selected == False:
                        input.click()
                        print("1：勾选第%d 个勾选框"%rowCount)
                        driver.find_element_by_class_name("batch_send").click()
                        time.sleep(1)
                        driver.find_element_by_xpath("//button[@class='ant-btn']").click()  # 取消弹窗
                        time.sleep(1)
                        input.click()
                        time.sleep(1)
                        for m in massage_arr:
                            m.click()
                            time.sleep(1)
                            driver.find_element_by_xpath("//button[@class='ant-btn']").click()
                            time.sleep(1)
                            for text in texts:
                                print(text.text)
                                time.sleep(1)
                                for W in wb_br:
                                    W.click()
                                    allhandles = driver.window_handles  # 获取当前窗口句柄
                                    print(allhandles)
                                    if driver.current_window_handle == allhandles[1]:
                                        driver.close()
                                        print("+++++++++++++")

                    else:
                        print("%d个已经勾选，选无法勾选"%rowCount)










    #不勾选发送
    def send_mess(self):
        try:
            driver.find_element_by_class_name("batch_send")
            driver.find_element_by_class_name("batch_send").click()
            print("定位到批量发送短信按钮")
            time.sleep(1)
            try:
                driver.find_element_by_class_name("ant-message")
                print("定位到ICON")
            except:
                print("无法定位icon")
        except:
            print("无法定位批量发送按钮")




    # 单个发短信
    def send_one_mes(self):
        try:
            driver.find_element_by_xpath("//tr[1]//td[4]//p[1]")
            time.sleep(1)
            l_text = driver.find_element_by_xpath("//tr[1]//td[4]//p[1]").text
            print(l_text)
            print(l_text[-4:])
            print("执行人信息")
            time.sleep(1)
            try:
                driver.find_element_by_xpath("//tr[1]//td[6]//span[1]")
                driver.find_element_by_xpath("//tr[1]//td[6]//span[1]").click()
                print("定位短信按钮")
                time.sleep(1)
                try:
                    driver.find_element_by_class_name("ant-modal-content")
                    print("定位弹窗")
                    time.sleep(1.5)
                    try:
                        driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span[2]")
                        w_text = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span[2]").text
                        print(w_text)
                        print(w_text[-4:])
                        print("定位弹窗信息")
                        if l_text[-4:] == w_text[-4:]:
                            print("操作正常")
                            driver.find_element_by_xpath("//button[@class='ant-btn']").click()
                        else:
                            print("错误")
                    except:
                        print("无法定位弹窗用户信息")
                except:
                    print("无法定位弹窗")
            except:
                print("无法定位短信按钮")
        except:
            print("无法定位列表人员信息")



    #手动同步
    #手动同步 后等待0-11后是否有弹窗
    def saa(self):
        i= 11
        try:
            driver.find_element_by_class_name("synchro")
            print("找到手动同步按钮")
            driver.find_element_by_class_name("synchro").click()
            print("手动同步")
            time.sleep(i)
            driver.find_element_by_class_name("synchro").click()
            print("%d 秒后可以同步"%i)
        except:
            print("%d 秒内无法同步"%i)




if __name__ == '__main__':
    a= Abc()
