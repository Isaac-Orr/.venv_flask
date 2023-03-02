from flask import Flask
from flask import render_template, request, redirect, url_for
from dbManager import PostManager
from models import Post

app = Flask(__name__)




@app.route("/update/<int:indexID>", methods=["GET","POST"])
def update(indexID):
    aPost = Post.populate(request.form)
    aPost.name = "Isaac Orr"
    aPost.id = indexID
#
    Pmanager = PostManager()
    Pmanager.updatePost(indexID, aPost)
    return redirect(url_for('list'))

@app.route("/delete/<int:indexID>", methods=["GET"])
def delete(indexID):
    Pmanager = PostManager()
    Pmanager.deletePost(indexID)
    return redirect(url_for("list"))

@app.route("/")
@app.route("/list")
def list():
    PManager = PostManager()
    posts = PManager.getPosts()
    return render_template("list.html", posts=posts)

@app.route("/detail/<int:indexID>")
def detail(indexID):
    PManager = PostManager()
    aPost = PManager.getPost(indexID)
    if  aPost is not None:
        return render_template("detail.html", post=aPost)
    
    return redirect(url_for("list"))


@app.route("/form")
@app.route("/form/<int:indexID>")
def form(indexID=None):
    aPost = None
    if indexID is not None:
        PManager = PostManager()
        aPost = PManager.getPost(indexID)
    return render_template('form.html', indexid=indexID,post= aPost)


@app.route("/save", methods=["POST"])
def save():
    aPost = Post.populate(request.form)
    aPost.name = "Isaac Orr"

    PManager = PostManager()
    PManager.insertPost(aPost)
    return redirect((url_for("list")))



# @app.route("/index")
# def index():
#     #users= [{"name":"Isaac", "role": "student"}, {"name":"Akshaya", "role": "tutor"}, {"name":"Gareth", "role": "student"}]
    

#     return render_template('index.html', title= "Home", posts= posts)

if __name__ == "__main__":
    app.run(debug=True)