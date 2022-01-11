# movie-recommender-system


## Download these files into `assets/` directory:
1. [encodedData](https://drive.google.com/file/d/1-69IKtAcVIt3eJ0To1jNEHK1YADcGSQ5/view?usp=sharing)
2. [the Knn model](https://drive.google.com/file/d/1-7XnYs4ByeC_mcWUnW6LTR6hNUUTEw6E/view?usp=sharing)
3. [data](https://drive.google.com/file/d/19zX2mSpumn8BNeYkTvfxgqaPyXR3RrzV/view?usp=sharing)


## install the requirements:
1. windows `pip install -r requrements.txt`
2. mac or linux `pip3 install -r requirements.txt`


## finally run main.py
`python main.py1`

## how to get recommendations:

#### make post request to ``BASE_URL/recommend/{{favMovies}}``
  {favMovies} is list of movies that the user has liked before to make predictions on
  
  
### the response should be a json object
