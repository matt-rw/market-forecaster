.PHONY: cli

cli:
	docker compose down --remove-orphans > /dev/null 2>&1
	docker compose run cli

clean:
	docker compose down --remove-orphans
	docker rmi #image ID
