# Tom Calculator

## Requirements

- docker
- docker-compose

## Run

```
docker-compose build
```
```
docker-compose run
```

Then go to URL: http://localhost:8080

## Test

```
docker-compose exec app python -m unittest -v test_*
```