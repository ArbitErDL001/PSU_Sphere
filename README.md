# PSUSphere

A Django web application for managing student organizations at **Palawan State University (PSU)**. PSUSphere provides an administrative interface for managing colleges, academic programs, students, organizations, and organization memberships.

## Features

* College management
* Program management
* Student management
* Student organization management
* Organization membership tracking
* Student enrollment tracking
* Search and filtering through Django Admin
* Fake data generation using Faker

## Technologies Used

* Python
* Django
* SQLite
* Docker
* Faker
* Git
* GitHub

## Run with Docker

Docker Desktop is required. From the Django project directory:

```powershell
cd projectsite
docker compose up --build
```

Open [http://localhost:8000](http://localhost:8000) after the container starts.

To run in the background or stop the app:

```powershell
docker compose up --build -d
docker compose logs -f web
docker compose down
```

To publish the image, tag it with your Docker Hub repository and push it:

```powershell
docker build -t yourusername/psusphere:latest .
docker push yourusername/psusphere:latest
```

On another computer, replace `yourusername` in `projectsite/for_client/docker-compose.yml`, then run:

```powershell
cd projectsite/for_client
docker compose up -d
```

The client setup stores its SQLite database in a Docker volume and does not require the source code.

## About the Author

<img src="https://github.com/ArbitErDL001.png" width="150" alt="ΛΞDL">

**Name:** ΛΞDL

* <a href="mailto:202380330@psu.palawan.edu.ph"><img src="https://img.shields.io/badge/Email-202380330%40psu.palawan.edu.ph-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
* <a href="https://github.com/ArbitErDL001"><img src="https://img.shields.io/badge/GitHub-ArbitErDL001-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"></a>

<img src="https://github.com/Jezellemaetaneo.png" width="150" alt="Zelle">

**Name:** Jezellemaetaneo

* <a href="mailto:202380324@psu.palawan.edu.ph"><img src="https://img.shields.io/badge/Email-202380324%40psu.palawan.edu.ph-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
* <a href="https://github.com/Jezellemaetaneo"><img src="https://img.shields.io/badge/GitHub-Jezellemaetaneo-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"></a>

## Project

PSUSphere was developed as an academic project for **Palawan State University** to demonstrate the use of Django for managing student and organization-related data through a web-based administrative system.
