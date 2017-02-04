from login_app.models import User

# Create your tests here.
def confirm_registered_info(col_name, usr_info):
    user = User.objects.values_list(col_name).filter(email=usr_info).count()

    #기존 사용 정보가 없다면(등록 가능한 정보라면)
    if user == 0:
        return True
    #기존 사용 정보가 있다면(등록 불가능한 정보라면)
    else:
        return False