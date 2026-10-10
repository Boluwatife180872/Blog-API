# FastAPI Blog API

This repository contains a blog application that I am building with **FastAPI and
Python**. The project is currently in development, so some of the features
described below are planned rather than complete.

## What this project is about

The finished application is intended to demonstrate how to build a
production-ready web application with FastAPI. It will provide both:

- A JSON API for programmatic access
- HTML pages that users can browse and interact with in a web browser

The project is being built incrementally, from the initial routes and database
models through authentication, testing, and deployment.

## Planned features

The completed application is expected to include:

- SQLAlchemy database integration
- Pydantic request and response validation
- Complete CRUD operations for blog content
- User registration and login
- Secure password hashing and JWT authentication
- Protected routes that verify the current user
- File uploads with image processing and validation
- Async application code
- A modular router-based project structure
- Frontend forms connected to the API with JavaScript
- Pagination
- Password reset flows with background email tasks
- Database migrations with Alembic
- PostgreSQL support alongside the initial SQLite setup
- AWS S3 file storage using Boto3
- Automated tests with Pytest
- Deployment with Nginx and SSL on a VPS
- Docker-based deployment to a serverless container platform

## Current status

This is an active learning and development project. The list above describes
the intended end result of the build, not a claim that every feature is
currently implemented. As development progresses, this README will be updated
to reflect the features that are available and the steps required to run the
application.

## Technology direction

- **Backend:** FastAPI, Python
- **Data validation:** Pydantic
- **ORM and migrations:** SQLAlchemy, Alembic
- **Databases:** SQLite during development, PostgreSQL for production
- **Authentication:** JWT and secure password hashing
- **Storage:** Local file storage during development, AWS S3 for production
- **Testing:** Pytest
- **Deployment:** Nginx, SSL, Docker, and a serverless container platform