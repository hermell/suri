from login_app.models import User

# Create your tests here.
def confirm_registered_user(user_email):
    user = User.objects.filter(email=user_email).count()

    #기존 사용자가 없다면(사용 가능한 이메일 주소라면)
    if user == 0:
        return True
    #기존 사용자가 있다면(사용 불가능한 이메일 주소라면)
    else:
        return False