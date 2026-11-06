# Alasmaa | Arabic Names Explorer

A web application for exploring Arabic names and their meanings, built with Python, FastAPI, and MySQL.

The project makes it easy to browse a database of over 1,000 Arabic names using optional search filters.

## Features

- Filter names by gender.
- Filter by the number of letters in a name.
- Find names containing a specific letter.
- Combine filters or browse without applying any.
- View names alongside their meanings.

### Technologies

- **Python** – Backend development
- **FastAPI** – REST API
- **MySQL** – Local database development
- **TiDB Cloud** – Cloud database (MySQL-compatible)
- **Render** – Backend hosting and deployment
- **HTML, CSS & JavaScript** – Web interface

## How It Works

The web interface sends selected filters to the FastAPI `/names` endpoint. The backend builds a parameterized SQL query using the provided filters, queries the MySQL database, and returns matching names for display.

## Live Demo

[Visit Alasmaa](https://alasmaa.onrender.com/)

## Why I Built It

I built Alasmaa to practice Python, SQL, database design, and backend development while creating a useful, publicly accessible application.
