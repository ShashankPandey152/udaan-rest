# UDAAN REST API

<p align="center">
  <img width="300" height="200" src="images/my-logo.png">
  <img width="200" height="200" src="images/udaan-logo.jpg">
</p>

## This repo contains the code for hiring challenge posted by Udaan


### To run the code:

On a **Linux** distribution or **Mac OSX**:

```
$ ./run.sh
```

On a **Windows** system:

```
$ python app.py
```

**NOTE**: If the system does not have the dependencies required to run the script:

```
$ python install -r requirements.txt
```

**Endpoints**

- /add-asset (POST): To add an asset. Payload:

```json
{
  "asset": "Test Asset",
  "description": "Test Description"
}
```

- /add-task (POST): To add a task. Payload:

```json
{
  "task": "Test Task",
  "description": "Test Description"
}
```

- /add-worker (POST): To add a worker. Payload:

```json
{
  "worker": "Test Worker",
  "age": 10,
  "phone": 1234567890
}
```

- /assets/all (GET): To fetch all assets.
- /allocate-task/ (POST): To allocate task to a particular worker. Payload:

```json
{
  "assetId": 1,
  "taskId": 2,
  "workerId": 5,
  "timeOfAllocation": "2019-06-28T14:45:15",
  "taskToBePerfomedBy": "2019-06-30T14:45:15"
  "
}
```

- /get-tasks-for-worker/<workerId> (GET): To fetch task assigned to a worker with particular worker id.
