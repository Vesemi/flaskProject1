import configparser
import os
import sys


def create_nginx_and_gunicorn_files(domena, projekt):
    # Edytujemy plik nginx:
    plik_nginxa = ''
    plik_nginxa_template = open('/var/www/' + projekt + '/setup/nginx_file').readlines()

    plik_gunicorn = ''
    plik_gunicorn_template = open('/var/www/' + projekt + '/setup/gunicorn_file').readlines()

    for l in plik_nginxa_template:
        l = l.replace('NAZWA_STRONY', domena)
        l = l.replace('NAZWA_PROJEKTU', projekt)
        plik_nginxa += l

    # Zapisujemy plik nginx:
    with open("/etc/nginx/sites-available/{}".format(domena), "w") as file1:
        file1.write(plik_nginxa)

    # Robimy link do kopii pliku nginx:
    os.system('sudo ln -s /etc/nginx/sites-available/{} /etc/nginx/sites-enabled/'.format(domena))

    for l in plik_gunicorn_template:
        l = l.replace('NAZWA_PROJEKTU', projekt)
        plik_gunicorn +=l

    # Zapisujemy plik gunicorn
    with open("/etc/systemd/system/" + projekt + '.service') as file2:
        file2.write(plik_gunicorn)

    # Restartujemy startujemy serwis flagi, restartujemy nginxa.
    os.system('sudo systemctl start ' + projekt + '.service')
    os.system('sudo systemctl daemon-reload')
    os.system('sudo systemctl restart nginx')
    os.system('sudo systemctl restart' + projekt + '.service')


if __name__ == '__main__':
        domena = sys.argv[1]
        projekt = sys.argv[2]
        create_nginx_and_gunicorn_files(domena, projekt)
        print('Twoja domena to:', domena)
        print('Przygotowuje pliki serwerowe.')
