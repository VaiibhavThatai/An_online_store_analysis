# Data Engineering project : From data extraction to analysis

The project uses various Data Engineering Techniques in Python and AWS to analyze an online stores data.

## Data Flow Diagram
![Screenshot 2022-06-14 225045](https://user-images.githubusercontent.com/85902487/173640336-f4b1f7c8-f995-4f03-9c77-b75b721f6d72.jpg)
 
The dataset is generated using a fake data generator written in python. 
The dataset comprises of the cutomers data, orders data and the customer risk scores which is then extracted, transformed and loaded and a pipeline is formed.
The database is stored in SQL files which is uploaded into AWS S3 bucket.
Docker is used for containerization and managing the applications. 

## Data Orchestration and Automation
Dagster is used for data orchestration and automation. The Dagster UI runs on http://localhost:3000/
![Screenshot 2022-06-14 225013](https://user-images.githubusercontent.com/85902487/173643835-e52b73e2-fb55-4dc9-8835-786a1b892d4f.jpg)

## Data Analysis
Next, the data is analysed using metabase which runs on http://localhost:3001/

Before analysing the data, let dagster run a few times. 
In Metbase, the Online Store Overview takes us to the dashboard fed with the tranformed data from the data pipeline. 
![Screenshot 2022-06-14 224950](https://user-images.githubusercontent.com/85902487/173644018-cb6e61a9-48bc-44a0-9d46-fcddc4795d36.jpg)

## Program Execution

To execute the program run the following commands:
The docker container is built using the following command

```bash
docker-compose up --build -d
docker ps
```

Log into the Dagster UI and Metabase UI

Once done, the containers can be tore down 
```bash
docker-compose down
```

