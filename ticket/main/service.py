from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'На ваш вопрос ответили',
        'ChristophorColumb12@gmail.com',
        [user_email],
        fail_silently=False
    )
