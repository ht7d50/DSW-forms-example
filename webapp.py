from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route('/login', methods=['POST', 'GET']) 
def login(): 
    error = None 
    if request.method == 'POST': 
        if valid_login(request.form['username'], request.form['password']): 
            return log_the_user_in(request.form['username']) 
        else: 
            error = 'Invalid username/password' 
    # the code below is executed if the request method was GET or the 
    #credentials were invalid 
    return render_template('response.html', error=error)
    
if __name__=="__main__":
    app.run(debug=False)
