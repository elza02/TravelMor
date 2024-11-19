# TravelMor: Travel Agency Management System

## Overview

**TravelMor** is a dynamic web application developed to streamline the management of a travel agency. The app is built with Django for the backend and utilizes HTML, CSS, and JavaScript for the frontend. This platform allows users to browse, search, and filter various travel packages, as well as securely book and pay for their trips through Stripe integration.

The core goal of TravelMor is to provide an intuitive interface for users while offering powerful backend functionality for efficient travel management. This project is designed to improve the overall customer experience and simplify the operational tasks of travel agencies.

## Key Features

- **Travel Package Search and Filtering**: Allows users to search for available travel packages based on various criteria like destination, price, and duration.
- **Secure Online Payments**: Integrated with Stripe to process payments, ensuring secure and seamless transactions.
- **User-Friendly Interface**: Built with HTML, CSS, and JavaScript for a responsive and engaging frontend experience.
- **Django Backend**: Robust backend system using Django to manage and serve travel data, ensuring efficient and secure handling of requests.

## Technologies Used

- **Django**: A Python-based web framework for building the backend and managing database models, user authentication, and routing.
- **HTML/CSS/JavaScript**: Frontend technologies to create a responsive, interactive, and visually appealing user interface.
- **Stripe**: A payment processing platform integrated for secure online transactions.
- **SQLite/PostgreSQL (depending on environment)**: Database to store travel data, bookings, and user details.

## Project Architecture

- **Frontend**: 
  - Developed using HTML, CSS, and JavaScript to provide an intuitive and interactive user experience.
  - The frontend communicates with the Django backend via API endpoints, enabling dynamic content updates and seamless interaction.
  
- **Backend**:
  - Built using Django, which serves as the primary backend framework for handling business logic, data management, and authentication.
  - The backend processes user requests, manages the database, and integrates third-party services like Stripe for payments.

- **Database**:
  - SQLite for development and PostgreSQL for production (or as per environment setup) to store information such as travel packages, user data, and booking records.

- **Payment Integration**:
  - Stripe API is integrated to allow users to securely process payments for their travel bookings.

## How to Run the Application

### Prerequisites:
- Python 3.x
- Django
- Stripe Account (for payment integration)
- Node.js (if using JavaScript libraries for frontend)
