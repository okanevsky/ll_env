from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def logout_view(request):
    """Завершает сеанс работы с приложением."""
    logout(request)
    return redirect('learning_logs:index')

def register(request):
    """Регистрация нового пользователя."""
    if request.method != 'POST':
        # Отобразить пустую форму регистрации.
        form = UserCreationForm()
    else:
        # Обработать заполненную форму.
        form = UserCreationForm(data=request.POST)
 
        if form.is_valid():
            new_user = form.save()
            # Вход в систему, переход на дом.страницу.
            login(request, new_user)
            return redirect('learning_logs:index')
 
    # Отобразить пустую форму или сообщение об ошибке.
    context = {'form': form}
    return render(request, 'registration/register.html', context)