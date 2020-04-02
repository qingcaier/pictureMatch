# -*- coding=utf-8 -*-
from src.api import api
from flask import request
from flask import Flask, render_template, jsonify
import os
import json
import importlib
import sys
importlib.reload(sys)
# from datetime import timedelta
# from adminend.manager import AdminFacade
# from flask_cors import *
# from flask_pymongo import PyMongo


app = Flask(__name__)
# ,
#             static_folder = "./admindist/dist/static",
#             template_folder = "./admindist/dist")
# CORS(app, supports_credentials=True)

# app.config['SECRET_KEY'] = "BBT1234567890adminBBT"
# app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=3)
# app.config['MONGO_DBNAME'] = 'spiderData'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/spiderData'

app.url_map.strict_slashes = False
# mongo = PyMongo(app)
# Manager.add_command('runserver', Server(host='0.0.0.0',port=5000,))


# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
# 	return render_template("index.html")


# Admin End
# app.add_url_rule('/api/showChart', view_func=api.showChart, methods=['GET'])
# app.add_url_rule('/api/initChart', view_func=api.initChart, methods=['GET'])
# app.add_url_rule('/api/initTable', view_func=api.initTable, methods=['GET'])

app.add_url_rule('/pictureMatch_ssim',
                 view_func=api.pictureMatch_ssim, methods=['POST'])
app.add_url_rule('/pictureMatch_cosin',
                 view_func=api.pictureMatch_cosin, methods=['POST'])
app.add_url_rule('/normalCompare',
                 view_func=api.normalCompare, methods=['POST'])
app.add_url_rule('/hashCompare',
                 view_func=api.hashCompare, methods=['POST'])
# app.add_url_rule(
#     '/admin/login', view_func=AdminFacade.admin_login, methods=['POST'])
# app.add_url_rule('/admin/scanall',
#                  view_func=AdminFacade.admin_scanall, methods=['POST', 'GET'])
# app.add_url_rule(
#     '/admin/scan', view_func=AdminFacade.admin_scan, methods=['POST'])
# app.add_url_rule('/admin/register',
#                  view_func=AdminFacade.admin_register, methods=['POST'])
# app.add_url_rule(
#     '/admin/revise', view_func=AdminFacade.admin_revise, methods=['POST'])
# app.add_url_rule('/admin/initpwd',
#                  view_func=AdminFacade.admin_initpwd, methods=['POST'])
# app.add_url_rule(
#     '/admin/logout', view_func=AdminFacade.admin_logout, methods=['POST', 'GET'])


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5001)
