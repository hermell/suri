from login_app.models import User

# Create your tests here.
def confirm_registered_info(col_name, usr_info) :
    chk_result = None

    if col_name == "email":
        chk_result = User.objects.filter(email=usr_info).exists()
    elif col_name == "nickname":
        chk_result = User.objects.filter(nickname=usr_info).exists()

#  기존 사용자가 있다면(등록 불가능한 정보라면)
    if chk_result:
        return False
    # 기존 사용자가 없다면(등록 가능한 정보라면)
    else:
        return True
