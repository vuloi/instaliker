import requests


#	Ham cho phep thuc hien relationship api cua instagram voi cac action: approve,ignore,follow,block,unblock,unfollow
def change_relationship(user_id, access_token, action):
	api_url = "https://api.instagram.com/v1/users/" + str(user_id) + "/relationship"
	params = {
		'access_token' : access_token,
		'action' : action
	}
	#	Kiem tra cac loi co the xay ra trong qua trinh POST
	try:
		response = requests.post(api_url, params)
	except:
		print 'Can not post to Instagram.com'
		return False
		
	if(response.status_code == 200):
		return True
	else:
		return False
		
#	Ham cho phep lay ra cac user follow user voi user_id
def get_users_followed_by(user_id, access_token):
	params = {
		'access_token' : access_token
	}
	api_url = "https://api.instagram.com/v1/users/" + str(user_id) + "/followed-by"
	#	Kiem tra cac loi co the xay ra trong qua trinh GET
	try:
		response = requests.get(api_url, params=params)
	except:
		print "Can not get from Instagram"
		return False
	
	print response.text
	if(response.status_code == 200):
		return True
	else:
		return False
		
#	Ham cho phep lay ra cac user ma user nay follow
def	get_users_follow(user_id, access_token):
	params = {
		'access_token' : access_token
	}
	api_url = "https://api.instagram.com/v1/users/" + user_id + "/follows"
	#	Kiem tra cac loi co the xay ra trong qua trinh GET
	try:
		response = requests.get(api_url, params=params)
	except:
		print "Can not get from Instagram"
		return False
		
	print response.text
	if(response.status_code == 200):
		return True
	else:
		return False
