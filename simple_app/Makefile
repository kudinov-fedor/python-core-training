dev_up:
	docker-compose up -d --build
	docker-compose exec web python manage.py create_db
	docker-compose exec web python manage.py seed_db
	@echo "Running on http://127.0.0.1:5000"


dev_down:
	docker-compose down -v


prod_up:
	docker-compose -f docker-compose.prod.yml up -d --build
	docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
	docker-compose -f docker-compose.prod.yml exec web python manage.py seed_db
	@echo "Running on http://127.0.0.1:1337"


prod_down:
	docker-compose -f docker-compose.prod.yml down -v
