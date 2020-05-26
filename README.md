# FastAPI example

You can build the application by using the provided Dockerfile

```
$ podman build -t fastapi .
```

To run the application in the container image

```
$ podman run --rm -v $PWD:/srv:z -p 8000:8000 --name fastapi -d fastapi
```

To stop the application

```
podman stop fastapi
```

To access the logs

```
podman logs fastapi
```

To test the application, first generate an history.txt file

```
$ dnf history | tail --lines=+3 > history.txt
```

then access the '/' endpoint

```
$ curl http://127.0.0.1:8000 | python -m json.tool
```
