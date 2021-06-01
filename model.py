def get_phd_comics(word):

    import requests
    import random
    from bs4 import BeautifulSoup    # in cloudshell, had to first install BeautifulSoup:  pip3 install beautifulsoup4

    phd_URL = "http://phdcomics.com/comics/archive_list.php"    
    htmlPage = requests.get(phd_URL)
    
    theSoup = BeautifulSoup(htmlPage.content, 'html.parser')    # parsing URL via BeautifulSoup

    font_elems = theSoup.find_all('font', size="2")   # finding all <font></font> elements in the HTML page
    nComics = int(len(font_elems)/2)

    myHrefList = []
    myTitleList = []
    for index in range(0, len(font_elems)):
        if index % 2 == 0:
            theHref = font_elems[index].a.get('href')
            lenHref = len(theHref)
            lenID = lenHref - 52  # determing only the part after = (i.e. actual id number itself)
            myHrefList.append(theHref[52:(52+lenID)])
            #myHrefList.append(theHref)
        else:
            theTitle = font_elems[index].get_text()
            myTitleList.append(theTitle)             

    myComicList = []
    for index in range(0, nComics):
        myComicList.append([myHrefList[index], myTitleList[index]])

    myString = word
    myString = myString.lower()
    myImgList = []

    if word == "____random____":
        myRandom3 = random.sample(myComicList, 3)
        for index in range(0, 3):
            htmlPage = requests.get("http://phdcomics.com/comics/archive_print.php?comicid=" + myRandom3[index][0])
            theSoup = BeautifulSoup(htmlPage.content, 'html.parser')
            img_elem = theSoup.find('img')
            myImgList.append([myRandom3[index][1], img_elem.get('src')])
    else:
        for index in range(0, nComics):
            if myString in myTitleList[index].lower():
                htmlPage = requests.get("http://phdcomics.com/comics/archive_print.php?comicid=" + myHrefList[index])
                theSoup = BeautifulSoup(htmlPage.content, 'html.parser')
                img_elem = theSoup.find('img')
                myImgList.append([myTitleList[index], img_elem.get('src')])

        if len(myImgList) == 0:   # if no comics were found with user's keyword
            myRandom3 = random.sample(myComicList, 3)
            for index in range(0, 3):
                htmlPage = requests.get("http://phdcomics.com/comics/archive_print.php?comicid=" + myRandom3[index][0])
                theSoup = BeautifulSoup(htmlPage.content, 'html.parser')
                img_elem = theSoup.find('img')
                myImgList.append([myRandom3[index][1], img_elem.get('src')])


    if len(myImgList) >= 3:
        return(random.sample(myImgList, 3))    # randomly selecting 3 elements from the list
    else:
        return(myImgList)
    


