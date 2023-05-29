# Trading App. 📈


## Description

This GitHub repository showcases a Trading App that was developed as part of a challenge for the Endava internship, in collaboration with a team. The application aims to track stock data for three companies in NASDAQ and three cryptocurrencies. The app, built using Flask, provides a user-friendly interface that displays the stock data in a table format. Additionally, it leverages an API to fetch the latest stock information. The backend of the application utilizes MongoDB as the database, allowing for efficient storage and retrieval of time series data. The app also includes a graphical representation of the data using a graph.

## Methodology: Scrum

Throughout the development process, the team utilized the Scrum methodology to ensure efficient project management and collaboration. The Scrum framework allowed for effective planning, task breakdown, and iterative development. User stories were defined to capture the requirements and expectations of the app's functionality. Tasks were assigned, and sprints were conducted to incrementally deliver working features. The Scrum approach facilitated close collaboration among team members and ensured the project's successful completion within the given timeframe.

## Deployment in AWS using Microservices Architecture

As a personal exercise, the application was deployed in AWS, leveraging the microservices architecture. Docker containers were utilized to encapsulate and deploy each component of the application independently. EC2 instances were provisioned to host the Docker containers, providing a scalable and reliable infrastructure. AWS Lambda functions were employed to implement serverless compute for specific functionalities. The microservices architecture allowed for easy scaling, flexibility, and fault tolerance, ensuring smooth operation of the Trading App. Along eith AWS i configured a EC2 instance to serve as a Jenkins server to create a CI/CD pipeline that was connected to the project repository in order to trigger the test file when a push was done.

The GitHub repository serves as a comprehensive collection of the app's source code and resources, enabling others to explore and learn from the project's implementations. The deployment in AWS showcases the practical application of microservices architecture in a real-world scenario, demonstrating the use of Docker, EC2 instances, and AWS Lambda to achieve scalable and reliable deployment of the Trading App.
