from flask import Flask,render_template,request,session,redirect


app= Flask(__name__)

carousal={
    'img1':"https://images.unsplash.com/photo-1577774438656-768f1e5d9ed6?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    'img2':'https://th.bing.com/th/id/OIG4.dWhT9sXy0hknqjXvA8mn?pid=ImgGn',
    'img3':"https://th.bing.com/th/id/OIG4.KVL6JaHZqTWGsNrFiXsf?pid=ImgGn"
}
@app.route('/logout') 
def logout():
    session.pop('username',None)
    return redirect('/')    

@app.route('/')
def index():
    alt=list(carousal.keys())
    imgs=list(carousal.values())
    ln=len(imgs)
    enumerated=enumerate(imgs)
    return render_template('index.html',imgs=imgs,len=ln,enumerate=enumerated,alt=alt)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        return "<h1>LOGGED IN</h1>"
        
@app.route('/register',methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template('register.html')
    elif request.method=='POST':
        return render_template('verification.html')
if __name__ == "__main__":
    app.run(debug=True)