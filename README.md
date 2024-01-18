# setup

This configuration runs on superset version `2.1.0` I found it more stable at the time in my initial commit. 

Edit the `superset_config_docker.py` for custom modifications

This config is ready for prod but remember the psql db is on docker and you should manually handle the backup,
else you can change the values of in the `.env`:

```
# database configurations (do not modify)
DATABASE_DB=superset
DATABASE_HOST=db
DATABASE_PASSWORD=superset
DATABASE_USER=superset
DATABASE_PORT=5432
DATABASE_DIALECT=postgresql
```

Also added `requirements.txt` file in the `docker/` folder edit this for more custom python packages
