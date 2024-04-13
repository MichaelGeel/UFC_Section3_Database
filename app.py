# First we import the Flask class from flask:
from flask import Flask, jsonify, request, url_for, redirect, session, render_template

# Instantiating the Flask class that we've imported, __name__ references the name of the module you're working in,
# in this case: app.py
app = Flask(__name__) 

# Adding our configuration values here, starting with debug mode:
app.config['DEBUG'] = True
# Adding a secret key to enable flask to sign cookies so that sessions can be implemented.
app.config['SECRET_KEY'] = 'Thisisasecret'

# Creating a route using the Flask object.
# <name> is not html, it's a placeholder.
#Will remove the name placeholder for now.
@app.route('/')# <name>')
# Defining the function tied to the route.
# Added the name parameter to match the <name> placeholder.
def index(): # name):
        # Removing the name from the session.
        session.pop('name', None)
        # For now we'll just return the below HTML code.
        # Have now added a name variable using the placeholer and format.
        return '<h1>Hello, World!</h1>' # {}!</h1>'.format(name)

# Creating a home route:
# Added the parameter specifying the methods in which this route can be called with.
# Added the name parameter to allow the route to take in data via the url call.
# Adding the default home route decoator above the home route:
@app.route('/home', methods=['GET', 'POST'], defaults={'name': 'Default'})
# Setting the name parameter to be locked as a string data type:
@app.route('/home/<string:name>', methods=['GET', 'POST'])
def home(name):
        # Adding name to the session dictionary.
        session['name'] = name
        # Refactoring the return to use the home.html template instead and feeding it the name variable.
        # Adding a boolean variable to pass for demonstrating conditional statements inside a template.
        # Adding a list and list of dictionaries to demonstrate the use of for loops in a template.
        return render_template('home.html', name=name, display=True, my_list=['one', 'two', 'three', 'four'],
                                listofdicts=[{'name': 'zack'}, {'name': 'zoe'}])

# Creating a route to return a jsonified version of python data structures.
@app.route('/json')
def json():
        # Retrieving name from the session dictionary.
        if 'name' in session:
                name = session['name']
        else:
                name = 'NotInSession'
        return jsonify({'key': 'value', 'key2': [1, 2, 3], 'name': name})

# Creating a new route as an example for query strings:
@app.route('/query')
def query():
        # creating the 2 variables that'll house the query string data.
        name = request.args.get('name')
        location = request.args.get('location')

        # Amending the output to utilize the data we've received.
        return '<h1>Hi {}, you are from {} and are on the query page.</h1>'.format(name, location)
        

# Creating a new route for lesson 9: Request form data:
# Adding both GET and POST request method permissions for the combine:
@app.route('/theform')# , methods=['POST', 'GET'])
def theform():
        # Adding the if statement to test for request type:
        # Reverting to original formatting for the GET POST route split.
        #if request.method == "GET":
                # Creating the form and the relevant inputs to be filled in in the form alongside the submit.
        # Porting the html to the form.html file and calling that file in the return here.
        return render_template('form.html')
#Commenting out the else for historic formatting evidence.
#        else:

#Adding the POST route decorator for the split methodology:
@app.route('/theform', methods=['POST'])
def process():
        # Retrieving the data passed in from the form:
        # Taking these 2 variables out (pretend saved to a db)
        # Readding name for passing the variable.
        # Readding locaton to show it can be passed to the home route 
        name = request.form['name']
        location = request.form['location']

        # Also removing the return statemnt.
        # return '<h1>Hello {} from {}. You have submitted the form.</h1>'.format(name, location)
        # Building the return statement redirect:
        # Including the location variable.
        return redirect(url_for('home', name=name, location=location))


# Adding the process route that will consume the data populated within the theform route:
# Because we're only getting data from the form, this route will only accept post requests.
# Commenting out for records of original work instead of deleting the route.
#@app.route('/process', methods=['POST'])
#def process():
#        # Retrieving the data passed in from the form:
#        name = request.form['name']
#        location = request.form['location']
#
#        return '<h1>Hello {} from {}. You have submitted the form.</h1>'.format(name, location)

# Route for handling JSON data:
@app.route('/processjson', methods=['POST'])
def processjson():

        # Fetch the json payload sent to this route:
        data = request.get_json()

        # Extracting the data from the payload:
        name = data['name']
        location = data['location']
        rand_list = data['randomlist']

        return jsonify({'result': 'success', 'name': name, 'location': location, 'Rand_list_key': rand_list[2]})

# Removing debug=True for the new configuration method.
if __name__ == '__main__':
        app.run()