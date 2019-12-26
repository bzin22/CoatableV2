#Preliminary App Structure: Faim, A Foodsharing Service
#Bryan Zin & Sparsh Gupta
#Cornell University
#Timetable: December 2019 - January 2020
#Stage: Pre-Spring 2020 

import kivy
from kivy.app import App #class from Kivy that allows you to build a window with graphics and all essential functions
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout #contains code for grids that you can put items into
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout): #will contain all necessary code for buttons, grids, etc
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs) #calling Grid Layout's constructor and giving it parameters to set it up
		self.cols = 1

		self.inside = GridLayout() #another grid layout inside this grid layout to hold the Submit Button
		self.inside.cols = 2 #number of columns, change accordingly

		self.inside.add_widget(Label(text = "First name: ")) #widget for Label added to screen
		self.firstName = TextInput(multiline = False) #defaults to have multiple lines in text input box, but only want one
		self.inside.add_widget(self.firstName) #widget for name added to screen

		self.inside.add_widget(Label(text = "Last name: "))
		self.lastName = TextInput(multiline = False)
		self.inside.add_widget(self.lastName)

		self.inside.add_widget(Label(text = "Email: "))
		self.email = TextInput(multiline = False)
		self.inside.add_widget(self.email)


		self.add_widget(self.inside)

		self.submit = Button(text = "Submit", font_size = 40)
		self.submit.bind(on_press = self.pressed) #links the definition of the pressed function to the physical clicking of Button on the screen
		self.add_widget(self.submit)

	def pressed(self, instance): #defines what Button does when it is "pressed"
		first_name = self.firstName.text
		last_name = self.lastName.text
		email = self.email.text

		print("First Name: ", first_name, "Last Name: ", last_name, "Email: ", email)
		self.firstName.text = "" #clears the first name, last name, and email fields after submission
		self.lastName.text = ""
		self.email.text = ""

class MyApp(App): #inheritance of all the features of "App" class from Kivy
	def build(self):
		return MyGrid()

if __name__ == '__main__':
	MyApp().run() #MyApp has run() method that allows you to run the application