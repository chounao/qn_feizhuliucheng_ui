from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
import time
"""
电子面单相关
"""

class Express_order():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        self.driver.maximize_window()



    def add_order(self):
        """
          常见问题 申请菜鸟面单 共享他人面单 添加网点账号
          """
        self.driver.get("https://localhost/main/#/v5/waybillAccount/accountManage")
        time.sleep(5)
        one =self.driver.find_element_by_class_name("waybill-account-manage")
        two = one.find_element_by_class_name("top")
        btn = two.find_elements_by_tag_name("button")

        for i in btn:
            if "电子面单常见问题？" in i.text:
                i.click()
                winds = self.driver.window_handles  # 获取当前窗口句柄
                self.driver.switch_to.window(winds[1])
                url = self.driver.current_url
                print(url)
                self.driver.close()
                self.driver.switch_to.window(winds[0])
                time.sleep(2)
                print("电子面单常见问题成功")
            if "申请菜鸟面单" in i.text:
                i.click()
                winds = self.driver.window_handles  # 获取当前窗口句柄
                self.driver.switch_to.window(winds[1])
                url = self.driver.current_url
                print(url)
                self.driver.close()
                self.driver.switch_to.window(winds[0])
                time.sleep(2)
                print("申请菜鸟面单")
            if "共享他人面单" in i.text:
                i.click()
                eavr = self.driver.find_element_by_class_name("ant-modal-confirm-btns")
                text_btn = eavr.find_element_by_class_name("ant-btn-primary")
                text_btn.click()
                time.sleep(0.5)
                text = self.driver.find_element_by_class_name("ant-message").text
                tell_text = "登录风火递，进入电子面单-面单账号-【共享面单管理】，右上角点击【分享他人面单】后输入我的旺旺ID，我就能使用你的电子面单了。"
                copy_text = self.driver.find_element_by_class_name("ant-btn-primary").send_keys(Keys.CONTROL,'c')

                if "文案已复制至剪切板" == text :
                    print("共享操作成功")
                else:
                    print("共享操作失败")
                time.sleep(1)
            if "添加网点账号" in i.text:
                i.click()
                try:
                    text = self.driver.find_element_by_class_name("ant-modal-title").text
                    time.sleep(1)
                    close_btn = self.driver.find_element_by_class_name("ant-modal-close-x")
                    close_btn.click()
                    print("添加网点成功")
                except:
                    print("添加网点无法操作")
            if "操作记录" in i.text:
                i.click()
                try:
                    text= self.driver.find_element_by_class_name("ant-modal-title").text
                    time.sleep(1)
                    close_btn = self.driver.find_element_by_class_name("ant-modal-close-x")
                    close_btn.click()
                    print("操作记录成功")
                except:
                    print("操作记录不正常")



    def share_order(self):
        """
        分享操作
        """
        self.driver.get("https://localhost/main/#/v5/waybillAccount/shareManage")
        time.sleep(5)
        name = int(time.time())
        try:
            #找到分享按钮
            one = self.driver.find_element_by_class_name("waybill-account-share-manage")
            two = one.find_element_by_class_name("top")
            share_btn = two.find_elements_by_tag_name("button")
            for i in share_btn:
                if "分享他人面单" == i.text:
                    i.click()
                    time.sleep(2)
                    print("定位分享按钮和点击正常")
                    try:
                        #定位输入旺旺弹窗
                        self.driver.find_element_by_class_name("ant-modal")
                        print("定位输入框弹窗正常")
                        try:
                            input_evar = self.driver.find_element_by_class_name("ant-modal")
                            evar = input_evar.find_element_by_class_name("ant-modal-content")
                            evar.find_element_by_class_name("ant-input").send_keys(name)
                            time.sleep(0.5)
                            print("成功输入内容")
                            evar.find_element_by_class_name("ant-btn-primary").click()
                            time.sleep(0.5)
                            try:
                                s_evar = self.driver.find_element_by_class_name("ant-modal-content")
                                print("定位同意弹窗")
                                s_evar.find_element_by_class_name("ant-btn-primary").click()
                                print("同意按钮")
                                time.sleep(2)
                                print("同意")
                                try:
                                    set_page = self.driver.find_element_by_class_name("ant-modal-body")
                                    li = set_page.find_element_by_tag_name("li")
                                    li.find_element_by_class_name("ant-checkbox-wrapper").click()
                                    print("选择网点成功")
                                    time.sleep(1)
                                    save_footer = self.driver.find_element_by_class_name("ant-modal-footer")
                                    save_btn = save_footer.find_element_by_class_name("ant-btn-primary")
                                    save_btn.click()
                                    print("点击保存按钮")
                                    time.sleep(2)
                                    try:
                                        #分享成功窗口
                                        top = self.driver.find_element_by_class_name("ant-modal-content")
                                        print("找到分享成功界面")
                                        textss = top.find_element_by_class_name("ant-modal-confirm-body")
                                        print(textss.text)
                                        iknow_but =top.find_element_by_class_name("ant-btn-primary")
                                        iknow_but.click()
                                        print("界面关闭")
                                    except:
                                        print("找不到分享成功弹窗")

                                except:
                                    print("无法保存网点元素")
                            except:
                                print("无法定位同意弹窗")

                        except:
                            print("无法定位输入框")
                    except:
                        print("无法定位输入框弹窗")
                        self.driver.close()


        except:
            print("无法找到分享按钮")

        return name

    def Unbind(self):
        """
        解绑操作
        """
        # name = self.share_order()
        self.driver.get("https://localhost/main/#/v5/waybillAccount/shareManage")
        time.sleep(3)
        top = self.driver.find_element_by_class_name("ant-table-content")
        cell = top.find_elements_by_class_name("ant-table-row")
        print(len(cell))
        for c in cell:
            operation = c.find_elements_by_tag_name("td")
            print(len(operation))
            btns = operation[-1]
            btn = btns.find_elements_by_class_name("ant-btn-link")
            for i in btn:
                if "解除共享" == i.text:
                    i.click()
                    time.sleep(1)
                    footer = self.driver.find_element_by_class_name("ant-modal-footer")
                    bt = footer.find_element_by_class_name("ant-btn-primary")
                    print("33333333333333333333333")
                    bt.click()
                    time.sleep(1)













if __name__ == '__main__':
    a = Express_order()
    # a.add_order()
    # a.share_order()
    a.Unbind()