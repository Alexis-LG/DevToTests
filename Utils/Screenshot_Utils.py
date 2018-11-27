from datetime import datetime

date_stamp = str(datetime.now()).split('.')[0]
date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
path = '.\DevToTests'


def take_screenshot(browser):
    print('Creating image in path: ' + path)
    browser.save_screenshot('..\\Screenshots\\' + date_stamp + '.jpg')
