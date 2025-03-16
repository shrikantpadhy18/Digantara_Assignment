### Steps to Set up the application ###

## Using Docker

**Note**  Make sure docker installed in your machine

Steps:
1. docker-compose up --build <!-- This will build the latest docker image of the application-->
2. Open the browser and hit the following URL: localhost:8000/docs it will open the swagger page for you where you can try all the available endpoints

## Using local machine

Steps:

1. Make sure python version >= 3.10 installed in your system
2. Go to the root directory of the project and enter
```python
  pip install -r requirements.txt
```
3. Open the terminal and hit the following command:  uvicorn main:app --reload
4. Open your browser and enter the url: localhost:8000/docs it will open the swagger page for you where you can try all the api endpoints available

5. Logs will be produced inside the logs folder.

### API Information ###

GET /health_check : By this endpoint will be able to check if application is in running state or not

POST /v1/binary_search : This endpoint deals with performing binary search in the given input

Body: 
```python
 {
  "array": [
    0
  ],
  "data": 0
}
```


POST /v1/quick_sort : This endpoint is responsible for performing quick sort on the given input

Body:

```python
{
  "array": [
    0
  ]
}

```


POST /v1/breadth_search_traversal : This endpoint is responsible for doing BFS on the given given graph

Body:

```python
{
  "graph": {
    "additionalProp1": [
      "string"
    ],
    "additionalProp2": [
      "string"
    ],
    "additionalProp3": [
      "string"
    ]
  },
  "root": "string"
}

```

### Request Schema ###

## Binary Search Algorithm ##

Following is the sample request

```python
{
  "array": [
    1,2,3,4,5
  ],
  "data": 5
}

```

We can modify the array values as needed , data is the value we want search in the array using binary search algorithm.

**Note**
The array should have integer value and data must also be an integer, swagger page contain the schema information too.

Following is the sample response

```python

{
  "response": "Data: 5 found at index 4",
  "status": "Processing Successful",
  "status_code": 200
}
```

## Quick Sort Algorithm ##


Following is the sample Request:

```python

{
  "array": [
    5,1,3,4,-400
  ]
}

```

Following is the response for the above request:

``` Python
{
  "response": " Following is the sorted array using Quick Sort Algorithm [-400, 1, 3, 4, 5]",
  "status": "Processing Successful",
  "status_code": 200
}
```


## BFS Traversal Algorithm

Following is the request for the BFS algorithm
We need to pass adjacency list as an input to our algorithm

```python

{
  "graph": {"0":["1","2"], "1":["3","4"],"2":["5","6"]},
  "root": "0"
}

```

**Note**

The Node values must be string
Root value represent the starting node of our traversal

Following is the response for the above input

```python


{
  "response": " Following is the output array using bfs traversal algorithm:  [['0'], ['1', '2'], ['3', '4', '5', '6']]",
  "status": "Processing Successful",
  "status_code": 200
}

```

## Deployment

Deployed the code into free tier vercel account

Steps Followed:

1. Created free account in vercel
2. Installed vercel cli using command 
**Note**: Ensure NPM is installed in your machine
```javascript
 npm i -g vercel
```

3. created vercel.json
4. deployed using following command : vercel .
5. live link : https://digantara-shrikant.vercel.app/docs