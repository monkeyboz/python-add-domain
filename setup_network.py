#!/usr/bin/python

import subprocess

class layout:
	def layout():
		subprocess.call("echo testing", shell=True)
		print "something"
	def something(self):
		print "testing"
	def options(self):
		return "something else"
	def otherthings(self,something):
		something += " else"
		return something
	def somethingelse(self):
		testing = self.otherthings("testing for something")
		return testing +" "+ self.options()
