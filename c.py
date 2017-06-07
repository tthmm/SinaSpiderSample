import os
import time
from selenium import webdriver

def main():
    """
        web
    """
    information = ""

    try:
        driver = webdriver.PhantomJS()
        # driver = webdriver.PhantomJS(executable_path=os.getcwd() + \
        # '/node_modules/phantomjs-prebuilt/bin/phantomjs')

        driver.set_window_size(1024, 768) # optional
        driver.get('http://vip.stock.finance.sina.com.cn/mkt/#hs_a')

        time.sleep(5)

        table = driver.find_element_by_id("tbl_wrap") \
        .find_element_by_css_selector('table')

        titles = table.find_element_by_css_selector('thead') \
        .find_element_by_css_selector('tr')

        head = titles.find_elements_by_css_selector('th')
        information += head[0].find_element_by_css_selector('a').text + ' '
        information += head[1].text

        content = titles.find_elements_by_css_selector('td')
        for title in content:
            information += title.text + ' '
        information += '\n'

        lists = table.find_element_by_css_selector('tbody') \
        .find_elements_by_css_selector('tr')

        for item in lists:
            head = item.find_elements_by_css_selector('th')
            information += head[0].find_element_by_css_selector('a').text + ' '
            information += head[1].find_element_by_css_selector('a').text

            content = item.find_elements_by_css_selector('td')
            for num in content:
                information += num.text + ' '
            information += '\n'
        print information
    except Exception as error:
        print error
    finally:
        data = open('data.txt', 'w')
        data.write(information.encode('GBK'))
        data.close()
        driver.quit()

if __name__ == '__main__':
    main()


