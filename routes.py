from app import app
from flask import render_template, request, redirect, session
import areas, users, chains, db, message, adminmode


#loginpage
@app.route("/", methods=["GET", "POST"])
def loginpage():
    if request.method == "GET":
        return render_template("loginpage.html")
    if request.method == "POST":
        username = request.form["username"]
        pword = request.form["password"]
        if users.login(username, pword) == True:
            return redirect("/index")
        else:
            return render_template("loginerror.html", message="Tarkista käyttäjätunnus ja salasana!")


#Registerpage
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["newusername"]
        pword = request.form["newpassword"]
        if len(pword) < 4 or len(pword) > 20:
            return render_template("loginerror.html", message="Käyttäjätunnuksen ja salasanan tulee olla vähintään 4 merkkiä ja enintään 20 merkkiä pitkiä.")
        elif len(username) < 4 or len(username) > 20:
            return render_template("loginerror.html", message="Käyttäjätunnuksen ja salasanan tulee olla vähintään 4 merkkiä ja enintään 20 merkkiä pitkiä.")
        else:
            users.register(username, pword)
            return redirect("/index")
        

#Index
@app.route("/index", methods=["GET"])
def index():
    if request.method == "GET":
        arealist = areas.showname()
        return render_template("index.html", arealist=arealist)

#Area of discussionS
@app.route("/area/<area_id>")
def area(area_id):
    if request.method == "GET":
        chainlist = chains.showchains(area_id)
    
        chainlist_with_count = []
        for chain in chainlist:
            chain_id = chain[0] 
            message_count = message.get_message_count(chain_id)
            chain_with_count = (chain[0], chain[1], message_count) 
            chainlist_with_count.append(chain_with_count)
        return render_template("area.html", chainlist=chainlist_with_count, area_id=area_id)


#Log out
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


#Area for admins, work in progress
@app.route("/adminarea", methods=["GET", "POST"])
def adminarea():
    if request.method == "GET":
        user_id = users.id()
        if users.checkadmin(user_id) == True:

            chainlist = adminmode.showchains()

            return render_template("adminarea.html", chainlist=chainlist)
        else:
            return render_template("error.html", message="Sinulla ei ole ylläpitäjän oikeuksia!")
    if request.method == "POST":
        chain_id = request.form["chain_number"]
        adminmode.deletechain(chain_id)
        return redirect("/index")


#New chain creation
@app.route("/newchain/<area_id>", methods=["GET", "POST"])
def newchain(area_id):
    if request.method == "GET":
        return render_template("newchain.html", area_id=area_id)
    if request.method == "POST":
        title = request.form["title"]
        chains.add_chain(title, area_id)
        return redirect("/newtitle/<area_id>")


#Content for the new chain
@app.route("/newtitle/<area_id>", methods=["GET", "POST"])
def newtitle(area_id):
    if request.method == "GET":
        return render_template("newtitle.html", area_id=area_id)
    if request.method == "POST":
        chain_id = chains.get_id()
        content = request.form["content"]
        user_id = session.get("user_id")
        message.add_message(content, user_id, chain_id)
        return redirect("/index")
    
#Show messages in chain
@app.route("/chain/<chain_id>")
def chain(chain_id):
    if request.method == "GET":
        messagelist = message.showmessages(chain_id)

        return render_template("chain.html", messagelist=messagelist, chain_id=chain_id)
    
#New messages
@app.route("/newmessage/<chain_id>", methods=["GET", "POST"])
def newmessage(chain_id):
    if request.method == "GET":
        return render_template("newmessage.html", chain_id=chain_id)
    if request.method == "POST":
        content = request.form["content"]
        user_id = session.get("user_id")
        message.add_message(content, user_id, chain_id)
        return redirect("/chain/" + chain_id)