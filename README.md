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

The application sends user-selected filters to a FastAPI backend hosted on Render. The backend executes parameterized SQL queries against a TiDB Cloud database and returns matching Arabic names and their meanings.

The database was initially developed locally using MySQL before being deployed to TiDB Cloud..

## Live Demo

[Visit Alasmaa](https://alasmaa.onrender.com/)

## Why I Built It

I built Alasmaa to practice Python, SQL, database design, and backend development while creating a useful, publicly accessible application.
