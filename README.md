# Metal Supply

## Usage

To run the application, navigate to the project's root directory, then use
this command:

```bash
docker-compose -f sawtooth-default.yaml up
```

Stop the containers before every run with:
```bash
docker-compose -f sawtooth-default.yaml down
```

## Check contents of DB

```bash
docker exec -it <hash> sh
```

```bash
psql -U sawtooth metal-supply
```

write SQL