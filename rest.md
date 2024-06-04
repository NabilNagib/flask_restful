
# REST
REST is a set of architectural constraints, not a protocol or a standard. API developers can implement REST in a variety of ways.

RESTful APIs use standard HTTP methods and are designed to be stateless, scalable, and simple to use

When a client request is made via a RESTful API, it transfers a representation of the state of the resource to the requester or endpoint. This information, or representation, is delivered in one of several formats via HTTP: JSON (Javascript Object Notation), HTML, XLT, Python, PHP, or plain text.


## Key Concepts of RESTful APIs
### 1. Resources:

Everything in REST is considered a resource, which can be a user, a book, an order, etc.
Resources are identified by URIs (Uniform Resource Identifiers).
HTTP Methods:

### 2. RESTful APIs use standard HTTP methods to perform actions on resources:
GET: Retrieve a resource or a collection of resources.
POST: Create a new resource.
PUT: Update an existing resource.
DELETE: Remove a resource.
PATCH: Partially update an existing resource.

### 3. Statelessness:

Each request from the client to the server must contain all the information needed to understand and process the request.
The server does not store any client context between requests, making each request independent.

### 4. Representations:

Resources are represented in different formats such as JSON, XML, or HTML.
Clients can request a specific format via the Accept header, and servers respond with the appropriate representation using the Content-Type header.
### 5. Endpoints:

Endpoints are URIs (Uniform Resource Identifier) that represent resources.
For example, https://api.example.com/users might represent a collection of users, while https://api.example.com/users/123 represents a specific user with the ID 123.



## Example of a RESTful API Interaction

## Endpoints and HTTP Methods
### GET /books:
* Retrieve a list of all books.
* Response: 200 OK with a JSON array of books.
### GET /books/{id}:
* Retrieve a specific book by its ID.
* Response: 200 OK with a JSON object representing the book.
### POST /books:
* Create a new book.
* Request Body: JSON object representing the new book.
* Response: 201 Created with a JSON object representing the newly created book.
### PUT /books/{id}:
* Update an existing book by its ID.
* Request Body: JSON object with updated book information.
* Response: 200 OK with a JSON object representing the updated book.
### DELETE /books/{id}:
* Delete a book by its ID.
* Response: 204 No Content.

