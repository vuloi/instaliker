import requests

#	Lay ra danh sach cac user like mot media voi media_id
def get_likes_media(media_id, access_token):
	params = {
		'access_token' : access_token
	}
	api_url = "https://api.instagram.com/v1/media/" + str(media_id) + "/likes"
	
	#	Kiem tra cac loi co the xay ra trong qua trinh GET
	try:
		response = requests.get(api_url, params=params)
	except:
		print "Can not get from Instagram"
		return False
	
	print response.text
	if(response != None and response.status_code == 200):
		return True
	else:
		return False
	
#	Like mot media cua mot user voi media_id va access_token
def post_like_media(media_id, access_token):
	params = {
		'access_token' : access_token
	}
	api_url = "https://api.instagram.com/v1/media/" + str(media_id) + "/likes"
	
	#	Kiem tra cac loi co the xay ra trong qua trinh POST
	try:
		response = requests.post(api_url, params)
	except:
		print "Can not post to Instagram"
		return False
	
	print response.text
	if(response != None and response.status_code == 200):
		return True
	else:
		return False
	
#	Xoa di like cua user voi access_token va media_id
def del_like_media(media_id, access_token):
	api_url = "https://api.instagram.com/v1/media/" + str(media_id) + "/likes?access_token=" + access_token
	
	#	Kiem tra cac loi co the xay ra trong qua trinh DEL
	try:
		response = requests.delete(api_url)
	except:
		print "Can not delete to Instagram"
		return False
	
	print response.text
	if(response != None and response.status_code == 200):
		return True
	else:
		return False