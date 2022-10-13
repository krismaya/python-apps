from flask import request, redirect, Flask, render_template
from PyDictionary import PyDictionary


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.args.get('keyword'):
        str_to_search = request.args.get('keyword')
        dictionary = PyDictionary()
        # print("Helo", str_to_search)
        result = dictionary.meaning(str_to_search)
        try:
            print(result.values())
        except Exception as e:
            result = "Unable to find your search"
        return render_template("index.html", meaning = result,str_to_search=str_to_search)
    else:
        return render_template("index.html")


if __name__=='__main__':
   app.run()
