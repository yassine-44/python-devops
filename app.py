from flask import Flask, render_template, request, redirect, url_for  
from flask_sqlalchemy import SQLAlchemy 

app=Flask(__name__)                 # this is juste to give our app a name 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.sqlite' ## don't understand it yet 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             ## to eleminate the worning that all 
db = SQLAlchemy(app)                  ## this is to create a db to this perticular app 

class Myapp(db.Model): 
    c_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(500))


@app.route('/')                     ## THIS INDICATE the path of this page this for example is juste localhost:5000/ 
def home():
    return('Yassine')



@app.route('/insert', methods=["POST"])                    
def home2():
    c_name = request.form.get("c_name")    ## this is to get what we put as input and associate it to the variable c_name
    new_c_name = Myapp(c_name=c_name)      ## this will define  the c_name variable from line 22 to the data base column c_name
    db.session.add(new_c_name)             ## this will add that to the data base  
    db.session.commit()
    return redirect(url_for("home1"))      ## this will rediract us to the home function 

@app.route('/delete/<int:c_id>')            ## the int:c_id is not clear                    
def delete(c_id):
    c_name= Myapp.query.get_or_404(c_id) ## the .first is not clear                
    db.session.delete(c_name)               
    db.session.commit()
    return redirect(url_for("home1")) 




@app.route('/base')
def home1():
    my_list = Myapp.query.all()                  ## to see all the content of the db 
    var="Hello this is a varible"                ## this is just a variable that we create in the python file and show in html page.
    return render_template("base.html", my_list=my_list) #here we just call it ## reder_template is use to call a html template or other page






if __name__=="__main__":        ## THIS PART IS JUST TO RUN THE APP 
    app.run()
    