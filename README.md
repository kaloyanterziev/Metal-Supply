# Metal Supply

## Usage - Backend

To run the application, navigate to the project's root directory, make sure you have docker running, then use
this command to build the containers:

```bash
docker-compose -f sawtooth-default.yaml up
```

Stop the containers before every run with:
```bash
docker-compose -f sawtooth-default.yaml down
```

## Usage - Frontend
To run the frontend navigate to folder metal_supply_app and run:

```bash
npm run serve
```

## Check contents of DB

```bash
docker exec -it <hash> sh
```

```bash
psql -U sawtooth metal-supply
```

write SQL

