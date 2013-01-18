import web
import urllib
import model

urls = (
    '/', 'Index',
    '/authorize', 'Authorize'
)

render = web.template.render('templates')

class Authorize:
    def GET(self):
    	i = web.input()
    	if(hasattr(i, 'code')):
    		code = getattr(i, 'code')
    		params = {}
    		params['client_id'] = '41036b378e53412688f2e4520eb6ed7e'
    		params['client_secret'] = '38ff3837ec9e4670939241a3936606ed'
    		params['redirect_uri'] = 'http://instaliker.luxcer.com:8080/authorize'
    		params['grant_type'] = 'authorization_code'
    		params['code'] = code
    		params = urllib.urlencode(params)
    		api_url = "https://api.instagram.com/oauth/access_token"
    		stream = urllib.urlopen(api_url, params)
    		return stream.read()
    	else:
	    	api_url = "https://api.instagram.com/oauth/authorize/?client_id=%s&redirect_uri=%s&response_type=code&scope=%s" \
    			%(client_id, redirect_uri, scope)
	    	raise web.seeother(api_url)

class Index:
	def GET(self):
		return render.index()
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
