
def whats_send_file(mob_no,path,caption):
    import pyautogui
    import time
    pyautogui.press('win')
    time.sleep(0.5)  # Wait for the start menu to open
    pyautogui.write('chrome')
    time.sleep(0.5)  # Wait before pressing enter
    pyautogui.press('enter')
    time.sleep(5)  # Wait for Chrome to open
    pyautogui.click(x=997, y=257)  # Close start menu if it's open
    time.sleep(1)
    pyautogui.click(x=800, y=77)  # Click on the address bar
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')  # Select the existing address
    pyautogui.press('delete')  # Delete the existing address
    time.sleep(0.5)
    pyautogui.write('https://web.whatsapp.com/')
    pyautogui.press('enter')
    time.sleep(20)  # Wait for WhatsApp Web to load
    pyautogui.click(x=458, y=192)  # Click on new chat
    time.sleep(1)
    pyautogui.click(x=203, y=240)  # Click on search bar
    time.sleep(0.5)
    pyautogui.write(mob_no)
    pyautogui.press('enter')
    time.sleep(2)  # Wait for chat to load
    pyautogui.click(x=684, y=987)  # Click on attachment button
    time.sleep(0.5)
    pyautogui.click(x=693, y=628)  # Click on document option
    time.sleep(1)
    pyautogui.write(path)
    pyautogui.press('enter')
    time.sleep(2)  # Wait for file to upload
    pyautogui.write(caption)
    pyautogui.press('enter')