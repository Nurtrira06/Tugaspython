# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:10:08 2021

@author: win10
"""

from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    html="""
    <style type="text/css">
    h1 {
	color: DeepSkyBlue;
    }
    h3{
       color: Blue;
       }
    p{
      color: Red;
      }
    </style>
    <center><h1><b>LATIHAN PYTHON DHANTI</b></h1></center> 
    <center><h3><b>Hallo semua ! Ini adalah latihan dasar Python pada Flask <br>
    oleh Nur Tri Ramadhanti Adiningrum NPM 1204061 Kelas 2C D4 Teknik Informatika <br>
    POLITEKNIK POS INDONESIA.</b></h3></center>
    <p align="center"><b>Terima kasih banyak !</b></p>
    """
    return html





