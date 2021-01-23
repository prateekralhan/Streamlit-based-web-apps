# DNA BioInformatics WebApp

### Live Demo available [here.](https://dna-bioinformatics-webapp.herokuapp.com/)

## Installation:
Execute: ***pip install -r requirements.txt***

## Usage:
1. Execute: **streamlit run app.py**
2. Navigate to **http://localhost:8501** in your web-browser.
<kbd>
<img src="https://user-images.githubusercontent.com/29462447/104076227-77b79480-523b-11eb-8e04-7a9b1f3885da.gif" data-canonical-src="https://user-images.githubusercontent.com/29462447/104076227-77b79480-523b-11eb-8e04-7a9b1f3885da.gif"/> 
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
