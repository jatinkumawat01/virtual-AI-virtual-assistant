import webbrowser as wb 
import time
import pyautogui as gui
from keyboard import press

def Whatsapp(number,msg):
    interval = 3
    position = 1023,230
    number={number}
    
    for i in number:
        url='https://wa.me/{}?text={}'.format(i,msg)
        wb.open(url)
        time.sleep(2)
        gui.click(position)
        time.sleep(2)
        gui.press('enter')
        press('enter')
        time.sleep(interval)
    

