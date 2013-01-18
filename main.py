import web
import requests
import json
import model

urls = (
    '/', 'Index',
    '/authorize', 'Authorize'
)

client_id = 'e8dfbc263b67491581aae2070354fa77'
client_secret = '313d6b3e73554f7dbc6ecd4bf8d03896'
redirect_uri = 'http://localhost:8080/authorize'
scope = 'likes+comments+basic+relationships'
code = ''
grant_type='authorization_code'

render = web.template.render('templates')

class Authorize:
    def GET(self):
    	i = web.input()
    	if(hasattr(i, 'code')):
    		code = getattr(i, 'code')
    		params = {
    			'client_id' : client_id,
    			'client_secret' : client_secret,
    			'redirect_uri' : redirect_uri,
    			'grant_type' : grant_type,
    			'code' : code
    		}
    		
    		instagram = "https://api.instagram.com/oauth/access_token"
	    	print instagram
    		response = requests.post(instagram, params)
    		response_infor = response.json()
    		user = response_infor['user']
    		
    		user_id = user['id']
    		username = user['username']
    		access_token = str(response_infor['access_token'])
    		
    		create_status = model.create_new_user(user_id, access_token, username)
    		if(create_status == True):
    			print	"Create user success"
    		else:
    			print	"Create user fail"
    		    		
    		return render.success(username)
    		
    	else:
	    	instagram = "https://api.instagram.com/oauth/authorize/?client_id=%s&redirect_uri=%s&response_type=code&scope=%s" \
    			%(client_id, redirect_uri, scope)
	    	raise web.seeother(instagram)

class Index:
	def GET(self):
		return render.index()
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
