#	Tao bang users
#	Bang nay chua cac truong thong tin: user_id, access_token, username, created_on. 3 truong du lieu dau tien chung ta
#	nhan duoc sau khi truy van de lay access_token. Moi user cua instragram co mot user_id duy nhat. Do do chung ta su
#	dung user_id lam khoa chinh cho bang users
CREATE TABLE users (
    user_id INT(15),
    access_token VARCHAR(100),
	username VARCHAR(100),
	created_on DATETIME,
    primary key (user_id)
);


#	Tao bang tags
#	Bang nay chua cac truong thon tin: user_id, tag_id, tag_detail. Doi voi moi user, sau khi user nhap vao mot tag de
#	thuc hien thao tac tim kiem, chung ta se luu tag nay vao co so du lieu. Do mot user co the nhap vao nhieu tag khac
#	nhau. Do do, tag co the coi la mot thuoc tinh da tri. Nguoc lai mot tag cung co the duoc tao ra boi nhieu nguoi(
#	chung ta co the coi moi quan he giua tag va user la moi quan he N * N). Trong truong hop nay, chung ta coi nhu su
#	dung moi quan he giua user va tag la 1 * N. Va do do, ta su dung cap (user_id, tag_id) lam khoa chinh cua bang
CREATE TABLE tags (
	user_id INT(15),
	tag_id	INT(15) AUTO_INCREMENT,
	tag_detail VARCHAR(255),
	primary key	(tag_id)
);
