# Trading App. 📈


## Description

This GitHub repository showcases a Trading App that was developed as part of a challenge for the Endava internship, in collaboration with a team. The application aims to track stock data for three companies in NASDAQ and three cryptocurrencies. The app, built using Flask, provides a user-friendly interface that displays the stock data in a table format. Additionally, it leverages an API to fetch the latest stock information. The backend of the application utilizes MongoDB as the database, allowing for efficient storage and retrieval of time series data. The app also includes a graphical representation of the data using a graph.

<img src="https://github.com/CristianAcostaDuarte/Trading-App/blob/main/images/ADA.png" width="800" height="500" alt="main page">


## Methodology: Scrum

Throughout the development process, the team utilized the Scrum methodology to ensure efficient project management and collaboration. The Scrum framework allowed for effective planning, task breakdown, and iterative development. User stories were defined to capture the requirements and expectations of the app's functionality. Tasks were assigned, and sprints were conducted to incrementally deliver working features. The Scrum approach facilitated close collaboration among team members and ensured the project's successful completion within the given timeframe.

## Deployment in AWS using Microservices Architecture

As a personal exercise, the application was deployed in AWS, leveraging the microservices architecture. Docker containers were utilized to encapsulate and deploy each component of the application independently. EC2 instances were provisioned to host the Docker containers, providing a scalable and reliable infrastructure. AWS Lambda functions were employed to implement serverless compute for specific functionalities. The microservices architecture allowed for easy scaling, flexibility, and fault tolerance, ensuring smooth operation of the Trading App. Along with AWS i configured a EC2 instance to serve as a Jenkins server to create a CI/CD pipeline that was connected to the project repository in order to trigger the test file when a push was done.

Here is the AWS architecture thati designed, the idea was to use a managed instance group to ensure availability to the service (thanks to auto healing if a zone is down then users will be redirect to the other zone thanks to the load balancer). Next i designed a VPC to enclose two subnets: one with a public IP to allow users around the world to connect to the application and a private subnet for the database backend that only communicate with the EC2 instances (i planned to use a nAT Gateway for the backend in order to fecth the data from the stock API).

<img src="https://github.com/CristianAcostaDuarte/Trading-App/blob/main/images/Arquitectura2.png" width="600" height="400" alt="main page">

In order to create a more robust application i configured an NGINX as a reverse proxy to redirect request to the application, the application as i said before was made in flask and gunicorn was used as Python WSGI HTTP Server. 

<img src="https://github.com/CristianAcostaDuarte/Trading-App/blob/main/images/App.png" width="600" height="400" alt="main page">

The last step was to decompose the monolithic application into microservices, so for that i used docker in order to create a container for each service in the application.

<img src="https://github.com/CristianAcostaDuarte/Trading-App/blob/main/images/Docker.png" width="600" height="400" alt="main page">


The GitHub repository serves as a comprehensive collection of the app's source code and resources, enabling others to explore and learn from the project's implementations. The deployment in AWS showcases the practical application of microservices architecture in a real-world scenario, demonstrating the use of Docker, EC2 instances, and AWS Lambda to achieve scalable and reliable deployment of the Trading App.
