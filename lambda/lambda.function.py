# list of names

names = ["Abraham Kenn", "Joe Fred","Alfred James", "Alex Tom","Benn Hans", "Shawn Pieere", "George Klus", "McKinsey Gong", "Greff Jaf", "Mike Lijn", "Zul Oret", "Yankie Weeyn", "Xing Yug", "Ting Luix"]


#The function returns the last name of the given string
def sort_lastname(name_val):
	return name_val.split()[-1]
	
#sort names by last name
results = sorted(names,key=sort_lastname)
print results


#The same above example using lambda functions. Lambda functions are anonymous functions 
#here no return keyword is required
fn = lambda name: name.split()[-1]

results = sorted(names, key=fn)

print results


#difference between a lambda and function
#- lambda is an expression which evluates to a function
#- Lambdas are anonymous
#- arguments list separated by colon and separated by commas
#- zero or more args supported. Example: 
#	lambda: 1+1
#- can only contain expression and NOT statements unlike a def function
#- No return keyword allowed, as the value of the expression will be the return
#- Lambdas cannot have docstrings
#- cannot be unit tested the expression alone, as these are anonymous.