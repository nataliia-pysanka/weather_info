Web service parses forecast for Kyiv for today and next 5 days. 
Service starts the scrap-task by schedule every day at 9am. 
The hour of schedule could be changed.

### Routes:
```bash
{URI}/api/
{URI}/schedule
```

## Installation

### Requirements

Docker-compose (https://docs.docker.com/compose/)

### Deploy

```bash
# Clone this repository using git
sudo cd weather_info
# Build the container
make up
# Navigate to http://localhost/api
```

### Destroy

```bash
make stop
```
