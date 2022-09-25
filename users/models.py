from flask import Flask, render_template, request
class User:
    def file(self):
        user = {
            "_id" : request.form.get('idno'),
            "name" : request.form.get('name'),
            "feedback" : request.form.get('feedback')
            }
        return user

