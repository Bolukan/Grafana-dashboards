# Grafana-dashboards
Grafana dashboards


## Installation Instructions

# Docker
Pull the image `grafana/grafana-oss:latest`  
Start the stack with the compose configuration (**insert link**) 

# First run
Login using `admin` and `admin` and set a new password.  

### JSON API
Choose *Administration*, *Plugins and data*, *Plugins* and install "JSON API" by Marcus Olsson. (current version 1.3.20)  
  
Choose *Connections*, *Add new connection*, *JSON API*, *Add new data source*
- Name: `marcusolsson-json-datasource`
- URL: `http://192.168.3.58/`

and choose 'Save & test'

### InfluxDB
Choose *Connections*, *Add new connection*, *InfluxDB*, *Add new data source*
- Name: `influxdb`
- Query language: `Flux`
- URL: `http://192.168.1.224:8086`
- Basic auth: `off`
- Organization: `your_name`
- Token: `<insert token>`
- Default Bucket: `Residence`

and choose 'Save & test'

# Install Dashboards
Use the script [prepare_dashboard.py](prepare_dashboard.py) to:
- Change to `"version": 1,`
- Check all to `"datasource": { "type": "marcusolsson-json-datasource", "uid": "<the right uid>" }`
- Check all to `"datasource": { "type": "influxdb", "uid": "<the right uid>" }`

Choose *New*, *Import* and load the Dashboards
