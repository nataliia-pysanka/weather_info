## Weather parser API

Web service receives information about the weather in Kyiv for today and 5 days ahead.every day at 09:00.
The hour of schedule could be changed.

#### The following requirements are being developed:
* The received information is stored in Django table. 
* If the day was not previously in the database - new day is added, if it was, the information is updated.
* Website for parsing: https://pogoda.meta.ua/
* Weather information could be viewed through the admin panel.
* When removing a director, the movie should NOT be removed, instead director = 'unknown' should be set.
* Endpoint to get weather information through the Django Rest Framework was implemented. 
* Information about weather could be update manually. 
* The schedule could be changed manually by endpoint (only hour). 
* The project deployed through docker-compose

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
git@github.com:nataliia-pysanka/weather_info.git
# Change directory
sudo cd weather_info
# Build the container
make up
# Navigate to http://localhost/api
# Use POST.json for filling database
```

### Destroy

```bash
make stop
```
