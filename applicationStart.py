
from flask import Flask,request,render_template
import requests



app=Flask(__name__)

@app.route('/')
def index():
    return render_template("template.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
    #Fectching input data by name attribute
    search_data = request.form['searchBox']
    html_url,full_name,last_commit,avatar_url,created_date=([] for i in range(5))

   #if the user has input any data then it search for that repo in github api
    #if the user has not entered any text then it will redirect back to home screen
    if search_data:
        #passing the input data to github api
        url="https://api.github.com/search/repositories?q="+search_data+"&sort=author-date&order=asc"

        #stroring the resources received by visting above url
        r = requests.get(url=url)

        r=r.json()

        #traversing through received to fetch specific detail
        for x in range(0,5):
            full_name.append(r['items'][x]['full_name'])
            avatar_url.append(r['items'][x]['owner']['avatar_url'])
            created_date.append(r['items'][x]['created_at'])
            last_commit.append(r['items'][x]['updated_at'])
            html_url.append(r['items'][x]['html_url'])


        #merging all the list created above
        complete_data = list(zip(full_name, avatar_url, created_date, last_commit, html_url))

        #passing the resultant to the template to render on the page
        return render_template("template.html",complete_data=complete_data)


    else:
        return render_template("template.html")





if __name__ == "__main__":
    app.run(debug=True)
