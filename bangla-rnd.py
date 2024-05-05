# তানভীর = 106
# এমদাদুল_হক = 2000
#
#
#
# if এমদাদুল_হক > তানভীর:
#     print("এমদাদুল হক ভাই বেশি ধনি")
#


# unicode_string = "তানভীর আহম্মদেদ রাসেল"
# ansi_string = unicode_string.encode('ascii', 'ignore')
# print(ansi_string)

#
# from bijoytounicode import bijoy2unicode
# TEST_TEXT = "‡Kv‡bv †Kv‡bv w`b, AvKvk‡Rvov †gN K‡i, Kv‡R gb e‡m bv| †W‡¯‹i mvg‡bi Rvbvjvi c`©v Zz‡j w`B| w¯Œ‡b ZvKvB, †`wL bv, `‚ieZ©x AvKvk I Bgvi‡Z wKQz †LvuR _v‡K| Ggb me w`‡bi bvg †KvgjMvÜvi|"
# test_output = bijoy2unicode(TEST_TEXT)
# print(test_output)

#
# from bnunicode import UnicodeStreaming
#
# data = UnicodeStreaming()
# unicode_bangla_text = 'Avgvi ‡mvbvi evsjv, Avwg ‡Zvgvh় fv‡jvevwm| wPiw`b ‡Zvgvi AvKvk, ‡Zvgvi evZvm, Avgvi c«v‡Y evRvh় evuwk॥'
#
# print(unicode_bangla_text)
#
# result=data.convertBnUniCodeToDecode(unicode_bangla_text)
# print(result)
# # আমার সোনার বাংলা, আমি তোমায় ভালোবাসি। চিরদিন তোমার আকাশ, তোমার বাতাস, আমার প্রাণে বাজায় বাঁশি॥
# toPrint=convertBnUniCodeToDecode(result)
# print(toPrint)


import unicode2bijoy

test = unicode2bijoy.Unicode()

uni_text = 'উভয় পাশে ধানের শীষে বেষ্টিত পানিতে ভাসমান জাতীয় ফুল শাপলা। তার মাথায় পাটগাছের পরস্পর সংযুক্ত তিনটি পাতা এবং উভয পাশে দুটি করে তারকা।'
toPrint=test.convertUnicodeToBijoy(uni_text)
print(toPrint)



# import time
# import pyautogui
#
# # Wait for a few seconds to give time to switch to the application
# time.sleep(5)
#
# # Set the position where the form fields are located
# name_field_position = (100, 200)
# email_field_position = (100, 250)
# submit_button_position = (100, 300)
#
# # Click on the name field and type the name
# pyautogui.click(name_field_position)
# pyautogui.typewrite("John Doe")
#
# # Click on the email field and type the email
# pyautogui.click(email_field_position)
# pyautogui.typewrite("johndoe@example.com")
#
# # Click on the submit button
# pyautogui.click(submit_button_position)
#
# # Optional: Wait for a few seconds to see the result before the script exits
# time.sleep(5)
