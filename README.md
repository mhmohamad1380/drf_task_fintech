<div  align="center">
<h1  align="center">Dockerized Django Rest Framework task</h1>
</div>

## Installation

1. first, You should clone this Repository.<br/>
2. delete the txt file exists in db folder
3. at the third step, go to the Cloned Directory, then Open in Terminal(CMD). <br/>
4. then, type ```docker-compose up --build ``` and Press Enter. (tip: make sure that Docker and Docker-Compose are Installed on Your Machine)
5. tip: username and password are ``` admin ```

## Routes

1. ```coinmarketcap/bitcoin``` to get bitcoin price <br/>
2. ```api/list``` to get last 5 bitcoin price record as api <br/>
3. ```api/logout``` to logout <br/>
4. ```api/coin/edit/<pk>``` to edit a bitcoin price record with pk=pk<br/>

## Note
<h3  align="center">this Project uses Celery Beat to get Bitcoin Price every 20 seconds</h3>

### Good Luck