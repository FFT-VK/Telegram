# from urllib.parse import urlparse
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from PIL import Image
# import time
# from django.conf import settings
# import os
# from selenium.common.exceptions import NoSuchElementException

# class TelegramScraper:
#     def __init__(self,Default):
#         self.options = Options()
#         # self.options.add_argument("--headless")
#         self.options.add_argument("user-data-dir=C:\\Users\\Sachin\\AppData\\Local\\Google\\Chrome\\User Data\\{Default}")
#         self.driver = None

#     def start_driver(self):
#         self.driver = webdriver.Chrome(options=self.options)

#     def stop_driver(self):
#         if self.driver:
#             self.driver.quit()

#     def crop_screenshot(self, screenshot_file, x, y, width, height):
#         image = Image.open(screenshot_file)
#         cropped_image = image.crop((x, y, x + width, y + height))
#         cropped_image.save(screenshot_file)

#     def scrape_telegram_user(self, phone_numbers):
#         screenshot_width = 1200
#         screenshot_height = 900
#         top_crop = 100
#         right_crop = 30
#         bottom_crop = 480
#         left_crop = 800
#         crop_x = left_crop
#         crop_y = top_crop
#         crop_width = screenshot_width - left_crop - right_crop
#         crop_height = screenshot_height - top_crop - bottom_crop

#         self.start_driver()

#         # all_user_info = []
#         user_info = {}
#         try:
#             width = 1200
#             height = 900
#             self.driver.set_window_size(width, height)
#             self.driver.get(f"https://t.me/+91{phone_numbers}")
#             # time.sleep(100)
#             time.sleep(3)
#             urls = self.driver.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div/div[4]/a")
#             for user in urls:
#                 print(user.text)
#                 button_url = user.get_attribute("href")
#             self.driver.get(button_url)
#             time.sleep(5)
#             a = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/div/span")
#             a.click()
            
#             screenshot_file = (f"E:\\django - Copy\\django - Copy\\storefront\\static\\admin\\img\\{phone_numbers}_tg.png")
#             get_url = self.driver.current_url
#             parsed_url = urlparse(get_url)
#             print(1)
#             user_id = parsed_url.fragment
#             user_info['User ID'] = user_id
#             try:
#                 print(2)
#                 time.sleep(5)
#                 try:
#                     profile = self.driver.find_element(By.CSS_SELECTOR,'.search-empty')
#                     print(profile.get_attribute('outerHTML'))

#                 except NoSuchElementException:
#                     profile = self.driver.find_element(By.CSS_SELECTOR,'.profile-content')
#                     print(profile.get_attribute('outerHTML'))
                        
#                 try:
#                     print(20)
#                     profile_name = profile.find_element(By.CSS_SELECTOR,".profile-name")
#                     print(f"{profile_name.text} ---- name")
#                     user_info["Name"] = profile_name.text
#                     # user_info = {'Name': profile_name.text}
#                 except:  
#                     pass
#                 try:
#                     profile_subtitle = profile.find_element(By.CSS_SELECTOR,".profile-subtitle")
#                     if profile_subtitle.text.startswith("last seen"):
#                         print(f"{profile_subtitle.text} ---- last")
#                         user_info["Last Seen"] = profile_subtitle.text
#                         # user_info = {'Last Seen': profile_subtitle.text}
#                 except:
#                     pass
#                 try:
#                     profile_photo = profile.find_elements(By.CSS_SELECTOR,".row.row-with-icon.row-with-padding ")
#                     print(f"{len(profile_photo)} --- photo")
#                     for i in profile_photo:
#                         if "Phone" in i.text:
#                             phone = i.find_element(By.CSS_SELECTOR,".row-title")
#                             print(f"{phone.text} ---- Phone")
#                             user_info['Phone Number'] = phone.text
#                             # user_info = {'Phone Number': phone.text}
#                         if "Username" in i.text:
#                             Username = i.find_element(By.CSS_SELECTOR,".row-title")
#                             print(f"{Username.text} ---- Username")
#                             user_info['Username'] = Username.text
#                             # user_info = {'Username': Username.text}
#                         if "Bio" in i.text:
#                             bio = i.find_element(By.CSS_SELECTOR,".row-title")
#                             print(f"{bio.text} ---- bio")
#                             user_info['Bio'] = bio.text
#                             # user_info = {'Bio': bio.text}
#                     print(5)
#                     time.sleep(7)
#                     self.driver.save_screenshot(screenshot_file)

#                     self.crop_screenshot(screenshot_file, crop_x, crop_y, crop_width, crop_height)

#                     user_info['Photo'] = f'http://192.168.1.22:8000/firstapp/display-image/{phone_numbers}/tg/'
#                 except:
#                     pass
#             except:
#                 pass
#             # all_user_info.append(user_info)
#             return user_info
#         except:
#             print(15)
#             print(f"User with phone number +91{phone_numbers} not present on Telegram")
#             return user_info
#         finally:
#             self.stop_driver()

# if __name__ == "__main__":
#     phone_numbers_input = "9315034300"
#     scraper = TelegramScraper("Default")
#     all_user_info = scraper.scrape_telegram_user(phone_numbers_input)
#     print(all_user_info)
































from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image
import time
from django.conf import settings
import os
from selenium.common.exceptions import NoSuchElementException

class TelegramScraper:
    def __init__(self,drivepath):
        self.options = Options()
        # self.options.add_argument("--headless")
        self.options.add_argument(f"user-data-dir=C:\\Users\\Sachin\\AppData\\Local\\Google\\Chrome\\User Data\\{drivepath}")
        self.driver = None

    def start_driver(self):
        self.driver = webdriver.Chrome(options=self.options)

    def stop_driver(self):
        if self.driver:
            self.driver.quit()

    def crop_screenshot(self, screenshot_file, x, y, width, height):
        image = Image.open(screenshot_file)
        cropped_image = image.crop((x, y, x + width, y + height))
        cropped_image.save(screenshot_file)

    def scrape_telegram_user(self, phone_numbers):
        screenshot_width = 1200
        screenshot_height = 900
        top_crop = 100
        right_crop = 30
        bottom_crop = 480
        left_crop = 800
        crop_x = left_crop
        crop_y = top_crop
        crop_width = screenshot_width - left_crop - right_crop
        crop_height = screenshot_height - top_crop - bottom_crop

        self.start_driver()

        # all_user_info = []
        user_info = {}
        try:
            width = 1200
            height = 900
            self.driver.set_window_size(width, height)
            self.driver.get(f"https://t.me/+91{phone_numbers}")
            # time.sleep(100)
            time.sleep(3)
            urls = self.driver.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div/div[4]/a")
            for user in urls:
                print(user.text)
                button_url = user.get_attribute("href")
            self.driver.get(button_url)
            time.sleep(5)
            a = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/div/span")
            a.click()
            
            screenshot_file = f"D:\\django - Copy\\storefront\\static\\admin\\img\\{phone_numbers}_tg.png"
            get_url = self.driver.current_url
            parsed_url = urlparse(get_url)
            print(1)
            user_id = parsed_url.fragment
            user_info['User ID'] = user_id
            try:
                print(2)
                time.sleep(5)
                try:
                    profile = self.driver.find_element(By.CSS_SELECTOR,'.search-empty')

                except NoSuchElementException:
                        print('a')
                try:
                    print(20)
                    profile_name = profile.find_element(By.CSS_SELECTOR,".profile-name")
                    print(f"{profile_name.text} ---- name")
                    user_info["Name"] = profile_name.text
                    # user_info = {'Name': profile_name.text}
                except:  
                    pass
                try:
                    profile_subtitle = profile.find_element(By.CSS_SELECTOR,".profile-subtitle")
                    if profile_subtitle.text.startswith("last seen"):
                        print(f"{profile_subtitle.text} ---- last")
                        user_info["Last Seen"] = profile_subtitle.text
                        # user_info = {'Last Seen': profile_subtitle.text}
                except:
                    pass
                try:
                    profile_photo = profile.find_elements(By.CSS_SELECTOR,".row.row-with-icon.row-with-padding ")
                    print(f"{len(profile_photo)} --- photo")
                    for i in profile_photo:
                        if "Phone" in i.text:
                            phone = i.find_element(By.CSS_SELECTOR,".row-title")
                            print(f"{phone.text} ---- Phone")
                            user_info['Phone Number'] = phone.text
                            # user_info = {'Phone Number': phone.text}
                        if "Username" in i.text:
                            Username = i.find_element(By.CSS_SELECTOR,".row-title")
                            print(f"{Username.text} ---- Username")
                            user_info['Username'] = Username.text
                            # user_info = {'Username': Username.text}
                        if "Bio" in i.text:
                            bio = i.find_element(By.CSS_SELECTOR,".row-title")
                            print(f"{bio.text} ---- bio")
                            user_info['Bio'] = bio.text
                            # user_info = {'Bio': bio.text}
                    print(5)
                    time.sleep(7)
                    self.driver.save_screenshot(screenshot_file)

                    self.crop_screenshot(screenshot_file, crop_x, crop_y, crop_width, crop_height)

                    user_info['Photo'] = f'http://192.168.1.70:8000/firstapp/display-image/{phone_numbers}/tg/'
                except:
                    pass
            except:
                pass
            # all_user_info.append(user_info)
            return user_info
        except:
            print(15)
            print(f"User with phone number +91{phone_numbers} not present on Telegram")
            return user_info
        finally:
            self.stop_driver()


if __name__ == "__main__":
    phone_numbers_input = "8447957401"
    scraper = TelegramScraper("Default")
    all_user_info = scraper.scrape_telegram_user(phone_numbers_input)
    print(all_user_info)
# 7011802396 MULUK
# 8810333320 HARSHITA
# 9205957789 AMAN














# from urllib.parse import urlparse
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from PIL import Image
# import time
# from django.conf import settings
# import os

# class TelegramScraper:
#     def __init__(self):
#         self.options = Options()
#         # self.options.add_argument("--headless")
#         self.options.add_argument("user-data-dir=C:\\Users\\Sachin\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
#         self.driver = None

#     def start_driver(self):
#         self.driver = webdriver.Chrome(options=self.options)

#     def stop_driver(self):
#         if self.driver:
#             self.driver.quit()

#     def crop_screenshot(self, screenshot_file, x, y, width, height):
#         image = Image.open(screenshot_file)
#         cropped_image = image.crop((x, y, x + width, y + height))
#         cropped_image.save(screenshot_file)

#     def scrape_telegram_user(self, phone_numbers):
#         screenshot_width = 1200
#         screenshot_height = 900
#         top_crop = 100
#         right_crop = 30
#         bottom_crop = 480
#         left_crop = 800
#         crop_x = left_crop
#         crop_y = top_crop
#         crop_width = screenshot_width - left_crop - right_crop
#         crop_height = screenshot_height - top_crop - bottom_crop

#         self.start_driver()

#         # all_user_info = []
#         user_info = {}
#         try:
#             width = 1200
#             height = 900
#             self.driver.set_window_size(width, height)
#             self.driver.get(f"https://t.me/+91{phone_numbers}")
#             time.sleep(5)
#             urls = self.driver.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div/div[4]/a")
#             for user in urls:
#                 button_url = user.get_attribute("href")
#             self.driver.get(button_url)
#             time.sleep(5)
#             a = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/div/span")
#             user_info['Name'] =a.text
#             l = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/span')
#             user_info['Last Seen'] = l.text
#             a.click()
#             screenshot_file = (f"D:\\django - Copy\\storefront\\static\\admin\\img\\{phone_numbers}_tg.png")
#             get_url = self.driver.current_url
#             parsed_url = urlparse(get_url)
#             user_id = parsed_url.fragment
#             user_info['User ID'] = user_id
#             # relative_path = phone_numbers + '_tg.png'
#             # screenshot_file = os.path.join(settings.MEDIA_ROOT, relative_path)
#             try:
#                 time.sleep(5)
#                 photo = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div/div/div[1]/span')
#                 try:
#                     z = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div/div/div[3]/div[2]/span")
#                     if z.text == "Phone":
#                         phone = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div/div/div[3]/div[3]")
#                         user_info['Phone Number'] = phone.text                    
#                     else:
#                         pass
#                     x = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div/div/div[4]/div[2]/span')
#                     if x.text == "Username":
#                         username = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div/div/div[4]/div[3]")
#                         user_info['Username'] = username.text
#                     else:
#                         pass
#                 except:
#                     pass       
#             except:
#                 time.sleep(7)
#                 self.driver.save_screenshot(screenshot_file)
#                 self.crop_screenshot(screenshot_file, crop_x, crop_y, crop_width, crop_height)

#                 user_info['Photo'] = f'http://192.168.1.70:8000/firstapp/display-image/{phone_numbers}/tg/'
#                 try:
#                     z = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[2]/span")
#                     if z.text == "Username":
#                         username = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[3]")
#                         user_info['Username'] = username.text
#                     elif z.text == "Phone":
#                         phone = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[3]")
#                         user_info['Phone Number'] = phone.text                    
#                     elif z.text == "Bio":
#                         bio = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[3]")
#                         user_info['Bio'] = bio.text
#                     else:
#                         pass
#                 except:
#                     pass
#                 try:
#                     z = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/span")
#                     if z.text == "Username":
#                         username = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[3]")
#                         user_info['Username'] = username.text        
#                     elif z.text == "Phone":
#                         phone = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[3]")
#                         user_info['Phone Number'] = phone.text                    
#                     elif z.text == "Bio":
#                         bio = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[3]")
#                         user_info['Bio'] = bio.text
#                     else:
#                         pass
#                 except:
#                     pass
#                 try:
#                     z = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/span")
#                     if z.text == "Username":
#                         username = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[3]")
#                         user_info['Username'] = username.text
#                     elif z.text == "Phone":
#                         phone = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[3]")
#                         user_info['Phone Number'] = phone.text                    
#                     elif z.text == "Bio":
#                         bio = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[3]")
#                         user_info['Bio'] = bio.text
#                     else:
#                         pass    
#                 except:
#                     pass

#             # all_user_info.append(user_info)
#             return user_info
#         except:
#             print(f"User with phone number +91{phone_numbers} not present on Telegram")
#             # return user_info
#         finally:
#             self.stop_driver()


# if __name__ == "__main__":
#     phone_numbers_input = "9026406818"
#     scraper = TelegramScraper()
#     all_user_info = scraper.scrape_telegram_user(phone_numbers_input)
#     print(all_user_info)
