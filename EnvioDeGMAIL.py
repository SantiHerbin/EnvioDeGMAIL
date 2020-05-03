#!/usr/bin/python
# -*- coding: utf-8 -*-
# SCRIPT ESCRITO POR SANTIAGO HERBIN
# Enviar correo Gmail con Python
 
import smtplib
 
fromaddr = 'TU_CORREO'
toaddrs  = 'CORREO_DEL_DESTINARIO'
msg = 'MENSAJE QUE QUIERAS ENVIAR'
 
 
# Datos
username = 'TU_CORREO'
password = 'TU_CONTRASEÑA'
 
# Enviando el correo
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()