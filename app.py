# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request

from model import get_phd_comics

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/comicResults', methods=['GET', 'POST'])
def comicResults():
    if request.method == 'POST':
        user_totalSubmission = request.form
        theKeys = list(user_totalSubmission.keys())
        if theKeys[0] == "submitRandom":   # user pressed "random" submit button
            user_keyword = "____random____"
            myImgList = get_phd_comics(user_keyword)
            return render_template("comicResults3.html", myImgList=myImgList)
        else:
            user_keyword = user_totalSubmission["userWord"]
            if user_keyword == "":
                user_keyword = "____random____"
            myImgList = get_phd_comics(user_keyword)
            if len(myImgList) == 3:
                return render_template("comicResults3.html", myImgList=myImgList)
            elif len(myImgList) == 2:
                return render_template("comicResults2.html", myImgList=myImgList)
            else:
                return render_template("comicResults1.html", myImgList=myImgList)
    else:
        return "Error, because you 'cheated' and got to this page by bypassing the form"



