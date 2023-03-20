from django.contrib.auth.models import User
from django.db import models


class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.TextField(max_length=400)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

# STEP1: Definim un model nou pentru a stoca token in momentul in care salvam un user (makemigrations, migrate)
# STEP2: In fisierul views.py din aplicatia userextend am generat noul token pe care l-am salvat in
# tabela userextend_usertoken
#    get_token = uuid.uuid4().hex
#    UserToken.objects.create(token=get_token, user_id=new_user.id, created_at=datetime.datetime.now())

# STEP3: Token a fost adaugat in dictionarul details_user pe valoarea cheii url   'url': f'http://127.0.0.1:8000/activate_user/{new_user.id}/{get_token_user}/'
# STEP4: in fisierul urls.py am adaugat la prefix si <str:token> pentru ca in url se va regasi token generat
#    path('activate_user/<int:pk>/<str:token>/', views.activate_user, name='activate-user')

# STEP5: In fisierul views.py unde am definit def activate_user am trimit id-ul userului respectv token generat.
# Cautam in tabela userextend_usertoken daca exista token  pentru userul respectiv si vom lua din acea tabela id-ul userului
# pe care il vom cauta in tabela auth_user si vom actualiza coloana is_active din False in True