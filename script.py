from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

s = 1
num = 1
browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.demirramon.com/generators/undertale_overworld_mockup_generator')
char_strarter = browser.find_element_by_xpath('//*[@id="charactersButton"]').click()
sleep(0.5)
choose_char = browser.find_element_by_xpath('//*[@id="charButton-1"]').click()
sleep(0.5)
enble_char = browser.find_element_by_xpath('//*[@id="charDisplayCheckBox-1"]').click()
sleep(0.5)
browser.find_element_by_xpath('//*[@id="charX-1"]').clear()
sleep(0.5)
x_char = browser.find_element_by_xpath('//*[@id="charX-1"]').send_keys("148")
sleep(0.5)
browser.find_element_by_xpath('//*[@id="charY-1"]').clear()
sleep(0.5)
y_char = browser.find_element_by_xpath('//*[@id="charY-1"]').send_keys("164")
sleep(0.5)
style = '//*[@id="charSpriteSelect-1"]/option[4]'
style_2 = '//*[@id="charSpriteSelect-1"]/option[5]'
walk_s = browser.find_element_by_xpath(style).click()
sleep(0.5)
bg_page = browser.find_element_by_xpath('//*[@id="backgroundButton"]').click()
sleep(0.5)
choose_bg = browser.find_element_by_xpath('//*[@id="zoneSelect"]/option[3]').click()
sleep(0.5)
choose_room = browser.find_element_by_xpath('//*[@id="roomSelect"]/option[2]').click()
sleep(0.5)


while True:
    if num % 4 == 0:
        char_page = browser.find_element_by_xpath('//*[@id="charactersButton"]').click()
        sleep(0.5)
        if s % 2:
            walk_s = browser.find_element_by_xpath(style_2).click()
            sleep(0.5)
            s += 1
        else:
            walk_s = browser.find_element_by_xpath(style).click()
            sleep(0.5)
            s += 1
        sleep(0.5)
        down1 = browser.find_element_by_xpath('//*[@id="downloadButton"]').click()
        sleep(0.5)
        download1 = browser.find_element_by_xpath('//*[@id="downloadButtons"]/button[2]').click()
    else:
        for i in range(4):
            bg_page = browser.find_element_by_xpath('//*[@id="backgroundButton"]').click()
            sleep(0.5)
            walk_char = browser.find_element_by_xpath('//*[@id="bgMovementButtons"]/div[2]/button[1]').click()
            sleep(0.5)
            down2 = browser.find_element_by_xpath('//*[@id="downloadButton"]').click()
            sleep(0.5)
            download2 = browser.find_element_by_xpath('//*[@id="downloadButtons"]/button[2]').click()
            sleep(0.5)
    num += 1
    sleep(0.8)