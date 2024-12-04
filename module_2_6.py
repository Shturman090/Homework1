def generate_password(n):
    password = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                twin = str(i) + str(j)
                password.append(twin)
                password_str = " "
                for X in password:
                    password_str += str(X)
    return password_str

for n in range(3, 21):
    n = int(input('Введите Ваше число от 3 до 20: '))
    password_str = generate_password(n)
    print('Ваш пароль:', password_str)
    break