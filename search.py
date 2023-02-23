import webbrowser
import pyautogui as pt
import time


words = ['antiestablishmentarianism', 'sesquipedalian', 'supercalifragilisticexpialidocious', 'onomatopoeia', 'hippopotomonstrosesquipedaliophobia', 'floccinaucinihilipilification', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'xylopyrography', 'abibliophobia', 'brouhaha', 'callipygian', 'cacophony', 'deipnosophist', 'epistemology', 'gobbledygook', 'jentacular', 'kerfuffle', 'logorrhea', 'malfeasance', 'nudiustertian', 'obsequious', 'paralipomenon', 'quidnunc', 'ratoon', 'salmagundi', 'tmesis', 'unctuous', 'vexillology', 'weltschmerz', 'xerophthalmia', 'yokel']
words2 = ['amazing', 'blissful', 'charming', 'delightful', 'elegant', 'fascinating', 'gorgeous', 'hilarious', 'intriguing', 'jubilant', 'kindhearted', 'luminous', 'magnificent', 'nostalgic', 'optimistic']



# Replace with the path to your Chrome executable
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
edge        = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s";

# Open a new Chrome window with the specified URL
for i in range(0,5):
    url = "https://bing.com/news/search?q="+words[i]
    url2 = "https://bing.com/news/search?q="+words2[i]
    webbrowser.get(chrome_path).open_new_tab(url)
    time.sleep(5)
    webbrowser.get(chrome_path).open_new_tab(url2)
    time.sleep(5)
    pt.click
    pt.hotkey("ctrl","w")
    pt.hotkey("ctrl","w")
    time.sleep(3)
    webbrowser.get(edge).open_new_tab(url)
    time.sleep(5)
    webbrowser.get(edge).open_new_tab(url2)
    pt.hotkey("ctrl","w")
    pt.hotkey("ctrl","w")


