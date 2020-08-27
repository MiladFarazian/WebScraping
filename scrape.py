from bs4 import BeautifulSoup
from selenium import webdriver

def get_twitter_stats():
    twitter_url = "https://twitter.com/MiladFarazian"
    driver = webdriver.Chrome()
    driver.get(twitter_url)
    content = driver.page_source.encode('utf-8').strip()
    twitter_soup = BeautifulSoup(content, "lxml")
    stats = twitter_soup.findAll("span", class_ ="css-901oao css-16my406 r-1qd0xha r-vw2c0b r-ad9z0x r-bcqeeo r-qvutc0")
    # for stat in stats:
    #     print(stat.text.strip())
    following = stats[0].text.strip()
    followers = stats[1].text.strip()
    print("Twitter Stats: {} following and {} followers".format(following, followers))

def get_instagram_stats():
    instagram_url = "https://www.instagram.com/MiladFarazian/"
    driver = webdriver.Chrome()
    driver.get(instagram_url)
    content = driver.page_source.encode('utf-8').strip()
    instagram_soup = BeautifulSoup(content, "lxml")
    stats = instagram_soup.findAll("span")
    # for stat in stats:
    #    print(stat.text.strip())
    following = stats[3].text.strip()
    followers = stats[2].text.strip()
    print("Instagram Stats: {} following and {} followers".format(following, followers))

""" def get_facebook_stats():
    facebook_url = "https://www.facebook.com/miladfarazian/"
    driver = webdriver.Chrome()
    driver.get(facebook_url)
    content = driver.page_source.encode('utf-8').strip()
    facebook_soup = BeautifulSoup(content, "lxml")
    stats = facebook_soup.findAll("span", class_ ="oi732d6d ik7dh3pa d2edcug0 qv66sw1b c1et5uql a8c37x1j muag1w35 enqfppq2 jq4qci2q a3bd9o3v lrazzd5p m9osqain")
    for stat in stats:
        print(stat.text.strip()) """


def get_social_media_stats():
    pass

#get_twitter_stats()
#get_instagram_stats()
#get_facebook_stats()