# OpenNET Message Brokers

OpenNET Message Brokers by Nuttaphat

## Description

OpenNET Message Brokers (Home test - python engineer (SNR)) by Nuttaphat

## Project Directory Structure

```raw
opennet-message-broker/
├── app/
│   ├── main.py
├── README.md
└── requirements.txt
```

## How to use

### Run RabbitMQ using Docker

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management
```

### Send a message to queue

```bash
cd app
python main send
```

### Receive a message to queue

```bash
cd app
python main
```
