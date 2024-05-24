build:
	cd django-ninja && make restart
	cd front-end-angular && make restart

up:
	cd django-ninja && make up
	cd front-end-angular && make up

ps:
	docker ps -a
clear:
	cd django-ninja && make limpar
	cd front-end-angular && make celar