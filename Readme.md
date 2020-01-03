# Direct Line Software Engineer Test

This sample application returns the sum of a list of numbers at the /total endpoint. 

Because it is expected to be replaced later, the list is generated in a separate module (services/number_list_provider.py). This can be swapped out for the real implementation later. 

Given the specification, this aims to be a very small easy to understand application. There is no need for a model to hold the state, or views implemented as templates. I aim to keep things as small as possible. 

There are basic unit tests. 

For real deployment, it would be better for security to hide flask behind an nginx reverse proxy, or trust amazon lambda to do it for us. 

## Set Up

1.  To create a virtual environment, on a terminal run 

> virtualenv --python=python3 env

2.  To work in the vnv run: 

> source ./env/bin/activate

3.  To install dependencies run: 

> pip install -r requirements.txt

## Usage

1.  To run the app itself run: 

> python app.py

2. To get a json containing the list total from the total endpoint, access:

> http://localhost:5000/total
