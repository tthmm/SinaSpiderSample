from __future__ import unicode_literals

import urllib2
import json
import os

from selenium import webdriver

# u = this.QUOTESURL + 'rn=' + Math.round(Math.random() * 60466176).toString(36) + '&' + s + 'list=' + a.join(',');
# http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=90000000&sort=symbol&asc=1&node=hs_a&symbol=&_s_r_a=init

def main():
    """
        fecth data
    """

    urlrequest = urllib2.Request('http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?' \
    + 'page=1' \
    + '&num=1000&sort=symbol' \
    + '&asc=1&node=hs_a&symbol=&_s_r_a=init')

    try:
        urlresponse = urllib2.urlopen(urlrequest)
    except urllib2.URLError as error:
        if hasattr(error,"code"):
            print error.code
        if hasattr(error,"reason"):
            print error.reason
    else:
        data = urlresponse.read().decode('gbk')

        driver = webdriver.PhantomJS()
#        driver = webdriver.PhantomJS(executable_path=os.getcwd() + \
#        '/node_modules/phantomjs-prebuilt/bin/phantomjs')
        jsonobject = driver.execute_script('var d = ' + data + '; return d;')
        driver.quit()

        for obj in jsonobject:
            obj[u'name'] = obj[u'name'].encode('utf-8')

        f = open('api-data.txt', 'w')
        json.dump(jsonobject, fp=f, indent=4, sort_keys=False, ensure_ascii=False, encoding='utf-8')
        f.close()


if __name__ == '__main__':
    main()










