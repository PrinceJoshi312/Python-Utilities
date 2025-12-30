from selenium import webdriver
class webtrain:
    def __init__(self):
         text = input("enter search string  ")
         driver = webdriver.Firefox()
         resp=driver.get("https://www.tensorflow.org/"+text)
         print(resp)
         
def contacts():
    print("feel free to contact to us from given link: nklsncklsafnaleif ")
    
def poll():
    inp = input("Enter the question for poll")
    options =[]
    options = input("enter your polls")
    