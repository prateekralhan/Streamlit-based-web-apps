
# Currency Converter WebApp

### Live Demo available [here.]()

## Installation:
Execute: ***pip install -r requirements.txt***

## Usage:
1. Execute: **streamlit run app.py**
2. Navigate to **http://localhost:8501** in your web-browser.

<kbd>
<img src="https://user-images.githubusercontent.com/29462447/115998983-8a49b400-a607-11eb-9e59-afa5c6a0a371.gif" data-canonical-src="https://user-images.githubusercontent.com/29462447/115998983-8a49b400-a607-11eb-9e59-afa5c6a0a371.gif"/> 
</kbd>
&nbsp;

### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
