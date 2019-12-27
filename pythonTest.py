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
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget): #will contain all necessary code for buttons, grids, etc
	firstname = ObjectProperty(None)
	lastname = ObjectProperty(None)
	email = ObjectProperty(None)
	
	def btn(self):
		print("First Name: " + self.firstname.text + '\n' + "Last Name: " + self.lastname.text + '\n' + "Email: " + self.email.text)
		self.firstname.text = ""
		self.lastname.text = ""
		self.email.text = ""

class MyApp(App): #inheritance of all the features of "App" class from Kivy
	def build(self):
		return MyGrid()

if __name__ == "__main__":
	MyApp().run() #MyApp has run() method that allows you to run the application