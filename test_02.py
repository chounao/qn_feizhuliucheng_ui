from selenium import webdriver
import random
import time

driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.maximize_window()
driver.get("https://localhost/main/#/v5/rate")
print("打开网页")
time.sleep(1)


class Automatic_evaluation():

    # 设置评价模式
    def Set_mode(self):
        box_arr = driver.find_elements_by_tag_name("li")  # 设置评价模式
        for box in box_arr:
            box.click()
            time.sleep(1)
            print("设置评价模式")
            print(box.text)

    #查看示例 选择示例，验证每次选择是否和页面一致
    def view_exa(self):
        View_examples = driver.find_element_by_xpath("//div[@id='main-container']//span[2]")  # 查看示例
        count = 0
        try:
            driver.find_element_by_class_name("ant-modal-content")  # 评价弹窗显示
            print("显示评价示例弹窗")

        except:
            View_examples.click()  # 点击显示示例按钮
            try:
                example = driver.find_elements_by_class_name("mb16")  # 找到使用示例范文
                print("定位示例范文")

                for i in example:
                    count = count+1
                    print("%d 次数"%count)
                    use_btn = i.find_element_by_class_name("pointer")  # 找到使用按钮
                    use_btn.click()
                    print("定位使用按钮正常")
                    print(i.text[:-3])  # 打印范文
                    View_examples.click()
                    time.sleep(1)

            except:
                print("获取到范文")



    #开关逻辑判断-取消一键评价操作

    def switch_one(self):
        """

        如果有待评价订单开启或者关闭的时候不去操作一键评价

        """
        switch = driver.find_element_by_class_name("ant-switch")  # 开关
        #当开关关闭，取消一键评论
        if switch.text == "关闭":
            switch.click()#去开启
            time.sleep(2)
            print("开启按钮")
            try:
                #判断是哪个弹窗
                popup = driver.find_element_by_class_name("ant-modal-confirm-body")
                print("定位第一个弹窗")
                one_popup_text = "因设置更改"
                #如果有暂未评价的订单去执行评价订单操作
                if one_popup_text in popup.text:
                    try:
                        close1_but = driver.find_element_by_class_name("ant-btn-default")
                        close1_but.click()
                        print("点击暂不评价按钮")
                        time.sleep(2)
                        try:
                            close2_but = driver.find_element_by_xpath("//body/div/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]")
                            close2_but.click()
                            time.sleep(2)
                            print("点击取消去按钮")
                            try:
                                close3_but = driver.find_element_by_class_name("ant-modal-close-x")
                                close3_but.click()
                                time.sleep(1)
                                print("点击X去按钮")
                            except:
                                print("无法定位到X按钮")
                        except:
                            print("无法定位取消按钮")
                    except:
                        print("无法定位暂不评价按钮")
            except:
                #没有待评价的直接开启按钮
                text = driver.find_element_by_class_name("ant-message").text
                print(text)
        elif switch.text == "开启":
            switch.click()
            time.sleep(1)
            try:
                text_close = driver.find_element_by_class_name("ant-modal-confirm-body-wrapper")
                if "确定要关闭自动评价吗？" in text_close.text:
                    close_btn = driver.find_element_by_xpath("//body//button[2]")#确认关闭
                    close_btn.click()
                    time.sleep(1)
                    try:
                        text = driver.find_element_by_class_name("ant-message").text
                        print(text)
                    except:
                        try:
                            driver.find_element_by_class_name("ant-modal-confirm-body-wrapper")
                            try:
                                but_close = driver.find_element_by_class_name("ant-btn-default")
                                but_close.click()
                                time.sleep(1)
                                print("暂不评价")
                                try:
                                    x_but = driver.find_element_by_class_name("ant-modal-close-x")
                                    x_but.click()
                                    time.sleep(1)
                                    print("点击X去按钮")
                                except:
                                    print("无法定位到X按钮")
                            except:
                                print("无法定暂不评价")
                        except:
                            print("无法定位一键评价弹窗")
            except:
                print("无法找到弹窗")


    def switch_two(self):
        """
           如果有待评价订单开启或者关闭的时候操作一键评价
           """
        switch = driver.find_element_by_class_name("ant-switch")  # 开关
        #当开关关闭，取消一键评论
        if switch.text == "关闭":
            switch.click()#去开启
            time.sleep(2)
            print("开启按钮")
            try:
                #判断是哪个弹窗
                popup = driver.find_element_by_class_name("ant-modal-confirm-body")
                print("定位第一个弹窗")
                one_popup_text = "因设置更改"
                #如果有暂未评价的订单去执行评价订单操作
                if one_popup_text in popup.text:
                    try:
                        eva_but = driver.find_element_by_xpath("//body//button[2]")
                        eva_but.click()
                        print("点击暂评价按钮")
                        time.sleep(3)
                        try:
                            driver.find_element_by_class_name("ant-modal-confirm-body")
                            print("评价成功")
                            try:
                                close3_but = driver.find_element_by_class_name("ant-modal-close-x")
                                close3_but.click()
                                time.sleep(1)
                                print("点击X去按钮")
                            except:
                                print("无法定位到X按钮")
                        except:
                            print("评价失败")
                    except:
                        print("无法定位暂不评价按钮")
            except:
                #没有待评价的直接开启按钮
                text = driver.find_element_by_class_name("ant-message").text
                print(text)
        elif switch.text == "开启":
            switch.click()
            time.sleep(1)
            try:
                text_close = driver.find_element_by_class_name("ant-modal-confirm-body-wrapper")
                if "确定要关闭自动评价吗？" in text_close.text:
                    close_btn = driver.find_element_by_xpath("//body//button[2]")#确认关闭
                    close_btn.click()
                    time.sleep(1)
                    try:
                        text = driver.find_element_by_class_name("ant-message").text
                        print(text)
                    except:
                        try:
                            driver.find_element_by_class_name("ant-modal-confirm-body-wrapper")
                            try:
                                but_eva = driver.find_element_by_xpath("//button[2]//span[1]")
                                but_eva.click()
                                time.sleep(3)
                                print("去评价")
                                try:
                                    driver.find_element_by_class_name("ant-modal-confirm-body")
                                    print("评价成功")
                                    x_but = driver.find_element_by_class_name("ant-modal-close-x")
                                    x_but.click()
                                    time.sleep(1)
                                    print("点击X去按钮")
                                except:
                                    print("无法定位到X按钮")
                            except:
                                print("无法定位去评价按钮评价")
                        except:
                            print("无法定位一键评价弹窗")
            except:
                print("无法找到弹窗")








if __name__ == '__main__':
    a = Automatic_evaluation()
    a.switch_two()