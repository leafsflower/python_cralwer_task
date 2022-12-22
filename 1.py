import csv
import pprint
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(options=option)
web.get('https://passport.ctrip.com/user/login')

start_time = time.perf_counter()
##等待30秒，
time.sleep(30)
# data-ubt-key="PC_head_logo_click"
web.find_element(By.CSS_SELECTOR,'[data-ubt-key="PC_head_logo_click"]').click()
# id="hotels-destination"
input_search = web.find_element(By.ID,"hotels-destination")
input_search.clear()
time.sleep(2)
input_search.send_keys("青岛")
# class="hs_text_kq4fu"
time.sleep(1)
web.find_element(By.CSS_SELECTOR,'[class="hs_text_kq4fu"]').click()
time.sleep(3)
web.find_element(By.CSS_SELECTOR,'[aria-label="崂山区"]').click()
print("请在30秒内完成关于需要爬取网站的操作")
time.sleep(30)
comment_lists = web.find_elements(By.CSS_SELECTOR,'[class="list-item-target"]')
pprint.pprint(len(comment_lists))


header = ['房型','入住时间','入住类型','评分','评论','评论时间']

data = ['1','2','3','4','5','6']
data1 = ['1','2','3','4','5','6']
with open('comment_data/demo.csv','w',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)


for page_comment in range(len(comment_lists)):
    time.sleep(2)

    try:

        comment_lists[page_comment].find_element(By.CSS_SELECTOR,'[class="count"]').click()
    except:
        continue
    time.sleep(10)
    print("到这了")
    # l = web.window_handles
    # print(l)
    # class="detail-headreview_all"

    windows = web.window_handles
    web.switch_to.window(windows[-1])

    web.find_element(By.CSS_SELECTOR,'[class="detail-headreview_all"]').click()
    time.sleep(2)
    # class="m-reviewCard-item"

    list_all = web.find_elements(By.CSS_SELECTOR,'[class="m_num"]')
    try:

        all_pages = list_all[5].text
    except:
        print("列表超范围")
        continue

    print("链接的总页数为：",list_all[5].text)
    for i in range(len(list_all)):
        print(list_all[i].text)

    for i in range(int(all_pages)):   ##每个链接只爬取一半
        time.sleep(1)


        comment_lists_all = web.find_elements(By.CSS_SELECTOR,'[class="m-reviewCard-item"]')
        comment_len = len(comment_lists_all)
        for j in range(comment_len):
        # 房型、入住时间、入住类型、评分、评论、评论时间
            span_list = comment_lists_all[j].find_elements(By.CSS_SELECTOR,'span')
            list_coment = []
            for span in span_list[:3]:
                list_coment.append(span.text)
                print(span.text)
            strong_text = comment_lists_all[j].find_element(By.CSS_SELECTOR,"strong")
            print(strong_text.text)
            list_coment.append(strong_text.text)
            # class="comment"
            comment_text = comment_lists_all[j].find_element(By.CSS_SELECTOR,'[class="comment"]').find_element(By.CSS_SELECTOR,"p").text

            comment_date = comment_lists_all[j].find_element(By.CSS_SELECTOR,'[class="reviewDate"]').text

            list_coment.append(comment_text)
            list_coment.append(comment_date)

            # print(list_coment)
            if list_coment[0] == '':
                continue


            with open('comment_data/demo.csv', 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)

                writer.writerow(list_coment)
        # type = "arrowRight"
        # class ="forward active"
        time.sleep(1)
        try:
            web.find_element(By.CSS_SELECTOR,'[class="forward active"]').click()
        except:
            print("爬取链接已结束")
            break


    web.close()
    web.switch_to.window(windows[0])

end_time = time.perf_counter()

print("结束的时间为：",end_time-start_time)




time.sleep(400000)