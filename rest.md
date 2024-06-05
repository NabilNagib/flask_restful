
# REST (Representational State Transfer)

REST is a set of architectural constraints, not a protocol or a standard. API developers can implement REST in a variety of ways.

* It's a way to design communication between systems over the internet.
* Uses simple HTTP requests to interact with resources (like data or services).
* Anything you want to work with (e.g., users, photos, orders) is treated as a resource.
* Each resource has its own unique URL.

RESTful APIs use standard HTTP methods and are designed to be stateless, scalable, and simple to use

# RESTful APIs

RESTful: Means the API follows the principles of REST.

* Most common formats used for representing information are JSON (JavaScript Object Notation) and XML

## Key Concepts of RESTful APIs

### 1. Resources

Everything in REST is considered a resource, which can be a user, a book, an order, etc.
Resources are identified by URIs (Uniform Resource Identifiers).
HTTP Methods:

### 2. RESTful APIs use standard HTTP methods to perform actions on resources

GET: Retrieve a resource or a collection of resources.

POST: Create a new resource.

PUT: Update an existing resource.

DELETE: Remove a resource.

PATCH: Partially update an existing resource.

### 3. Statelessness

Each request from the client to the server must contain all the information needed to understand and process the request.
The server does not store any client context between requests, making each request independent.

### 4. Representations

Resources are represented in different formats such as JSON, XML, or HTML.
Clients can request a specific format via the Accept header, and servers respond with the appropriate representation using the Content-Type header.

### 5. Endpoints

Endpoints are URIs (Uniform Resource Identifier) that represent resources.

## Endpoints and HTTP Methods

### GET /newsletters

Retrieve a list of all newsletters.
Response: 200 OK with a JSON array of newsletters.

```bash
    curl -X GET <http://127.0.0.1:5000/newsletters>
```

### GET /newsletters/{id}

Retrieve a specific newsletter by its ID.
Response: 200 OK with a JSON object representing the newsletter.

```bash
    curl -X GET <http://127.0.0.1:5000/newsletters/1>
```

### POST /newsletters

Create a new newsletter.
Request Body: JSON object representing the new newsletter.
Response: 201 Created with a JSON object representing the newly created newsletter.

```bash
    curl -X POST <http://127.0.0.1:5000/newsletters> \
    -H "Content-Type: application/json" \
    -H "Filter: Tree" \
    -d '{
        "body": "The Kenya Wildlife Society has dispatched a special team to hunt down a lioness spotted in a residential area in Ongata Rongai's Nazarene area.",
        "published_at": "2024-06-05 07:15:01",
        "title": "Lioness on the loose"
    }'
```

### PUT /newsletters/{id}

Update an existing newsletter by its ID.
Request Body: JSON object with updated newsletter information.
Response: 200 OK with a JSON object representing the updated newsletter.

```bash
    curl -X PUT <http://127.0.0.1:5000/newsletters/1> \
    -H "Content-Type: application/json" \
    -d '{
        "title": "Tree Planting",
        "body": "Every Citizen is expected to plant at least one tree"
    }'
```

### DELETE /newsletters/{id}

Delete a newsletter by its ID.
Response: 200

```bash
    curl -X DELETE <http://127.0.0.1:5000/newsletters/50>
```

### HEADER /newsletters/filter

Retrieve newsletters based on a filter provided in the headers.
Response: 200 OK with a JSON array of filtered newsletters.

```bash
    curl -X GET <http://127.0.0.1:5000/newsletters/filter> \
    -H "Filter: plant"
```

## HTTP CODES

200: Successful request.

201: Successful creation of a new resource.

400: Bad request, usually due to missing or invalid data in the request.

404: Resource not found.

<https://www.dotcom-monitor.com/wiki/knowledge-base/http-status-codes-list/>
