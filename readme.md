# Private Mongo DB for Cloud Run

How to provide Cloud Run access to a private, self-hosted MongoDB server (on Compute Engine) with no external IP address.  

# Technologies

Google Cloud Platform:
* Compute Engine (Self-hosted MongoDB)
* Cloud Run (REST API)
* Cloud VPC
* Private Google Access
* Cloud NAT
* Serverless VPC Access Connector (Access to Private, INTERNAL ONLY MongoDB)
* Cloud Build (Serverless CI / CD)
* Cloud Secret Manager (For sensitive data)

Google Cloud Libraries:
* Cloud Logging for Python

Python Libraries:
* FastAPI (Web server framework)
* Pydantic (Parsing and validation)
* Uvicorn / Gunicorn (Process hanagement and hosting)
* HTTPX (Asynchronous HTTP client)
* PyMongo (MongoDB client)
* Pipenv (Dependency management)

# Useful links:

* https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/
* https://www.mongodb.com/docs/manual/reference/configuration-options/
* https://www.mongodb.com/docs/manual/reference/configuration-options/#net-options