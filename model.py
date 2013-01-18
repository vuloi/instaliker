import web, datetime

db = web.database(dbn='mysql', db='test', user='root', passwd='vuxuanloi')

#
#	Thuc hien cac truy van de CSDL voi users
#

#	Lay cac user
def get_users():
    return  db.select('users', order='user_id DESC')

#	Lay thong tin cua mot user voi user_id
def get_user_infor(user_id):
    try:
        return db.select('users', where='user_id=$user_id', vars=locals())[0]
    except IndexError:
        return None
        
#	Lay ra username
def get_username(user_id):
	try:
		user = db.select('users', where='user_id=$user_id', what='username', vars=locals())[0]
		if(user != None):
			return user['username']
		else:
			return None
	except IndexError:
		return None
		
#	Lay ra access_token
def get_access_token(user_id):
	try:
		token = db.select('users', what='access_token', where='user_id=$user_id', vars=locals())[0]
		if(token != None):
			return token['access_token']
		else:
			return None
	except IndexError:
		return None

#	Tao ra user moi voi user_id, access_token, username, va created_on dat mac dinh la ngay ma user do dang ki
#	co su dung Transaction
def create_new_user(user_id, access_token, username):
	transaction = db.transaction()
	try:
		db.insert('users', user_id=user_id, access_token=access_token, username=username, created_on=datetime.datetime.utcnow())
	except:
		transaction.rollback()
		return False
	else:
		transaction.commit()
		
	return True
	
#	Xoa user voi user_id
def del_user(user_id):
	transaction = db.transaction()
	try:
	    db.delete('users', where="user_id=$user_id", vars=locals())
	except:
		transaction.rollback()
		return False
	else:
		transaction.commit()
		
	return True
	
	
#
#	Thuc hien cac truy van CSDL voi tags
#

#	User tao ra mot tag su dung user_id
def create_new_tag_with_user_id(user_id, tag_detail):
	transaction = db.transaction()
	try:
		db.insert('tags', user_id=user_id, tag_detail=tag_detail)
	except:
		transaction.rollback()
		return False
	else:
		transaction.commit()
	
	return True
	
#	Xoa tag voi tag voi user_id, tag_id
def	del_tag(user_id, tag_id):
	transaction = db.transaction()
	try:
		db.delete('tags', where="user_id=$user_id and tag_id=$tag_id", vars=locals())
	except:
		transaction.rollback()
		return False
	else:
		transaction.commit()

	return True

#	Lay ra tag voi user_id
def	get_tags(user_id):
	tags = db.select('tags', where="user_id=$user_id", vars=locals())
	return tags

#	Sua tag cua mot user voi user_id va tag_id
def	update_tags(user_id, tag_id, tag_detail):
	transaction = db.transaction()
	try:
		db.update('tags', where="user_id=$user_id and tag_id=$tag_id", tag_detail=tag_detail, vars=locals())
	except:
		transaction.rollback()
		return False
	else:
		transaction.commit()
	
	return True
