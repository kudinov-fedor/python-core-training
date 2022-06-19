dev_up:
	docker-compose up -d --build
	docker-compose exec web python manage.py create_db
	docker-compose exec web python manage.py seed_db
	@echo "Running on http://127.0.0.1:1337"


dev_down:
	docker-compose down -v


dev_logs:
	docker-compose logs -f


prod_up:
	docker-compose -f docker-compose.prod.yml up -d --build
	docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
	docker-compose -f docker-compose.prod.yml exec web python manage.py seed_db
	@echo "Running on http://127.0.0.1:1337"


prod_down:
	docker-compose -f docker-compose.prod.yml down -v


prod_logs:
	docker-compose -f docker-compose.prod.yml logs -f


run_test:
	locust -H http://127.0.0.1:1337 -u 1000 -r 5 -t 300s --autostart -P 8089
