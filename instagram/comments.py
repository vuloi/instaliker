import requests

#   Lay ve danh sach tat ca cac comment doi voi mot media_id
def get_comments_media(media_id, access_token):
    params = {
        'access_token' : access_token
    }
    api_url = "https://api.instagram.com/v1/media/" + str(media_id) + "/comments"
    
    #   Kiem tra cac loi co the xay ra trong qua trinh GET
    try:
        response = requests.get(api_url, params=params)
    except:
        print "Can not get from instagram"
        return False
    
    print response.text
    if(response != None and response.status_code == 200):
        return True
    else:
        return False
    
#   Cho phep post mot comment doi voi mot media_id
def post_comments_media(media_id, access_token, text_comment):
    params = {
        'access_token' : access_token,
        'text' : text_comment
    }
    api_url = "https://api.instagram.com/v1/media/" + media_id + "/comments"
    
    #   Kiem tra cac loi co the xay ra trong qua trinh POST
    try:
        response = requests.post(api_url, params)
    except:
        print "Can not post to instagram"
        return False
    
    print response.text
    if(response != None and response.status_code == 200):
        return True
    else:
        return False