# google_geocoding

The focus of this project is to create Django app that utilizes the Geocoding API from google maps.

## Setup

#### virtual environment

Create a virtual environment by using the command line tool `virtualenv` , if you are not familiar with this tool here is a handy link on more information : https://virtualenv.pypa.io/en/latest/

1) in the root of the folder with this repo run: 
    `virtualenv venv` (venv is just a variable name  for the folder being created by virtualenv. you can name it anything you like)
2) next find the requirements.text file in this repository and run:
    `pip install -r requirements.txt `
3) After all packages are install you can move on to the next step.
      
#### update django settings file
To use this django app you need to update the `google_geocoding/settings.py` file. Opening the file then scrolling to the end of the file look for the "API_KEY" settings variable. This is where you can type in the API key for your google apis. 



## Usage

There are 3 pages/views for this project :

`localhost/geocoding/` - A form with a single text box for an address.
`localhost/reverse_geocoding` - A form with two text boxes for the longitude and latitude of a specific location.

After inserting the values for either page, hitting the submit button will get the geocoding data straight from google using their api.
The geocode data is printed onto the webpage in a json format.

 The third page is :
 
 `localhost/calculate_distance` - Another form with 4 variables, 2 sets of longitude and latitude coordinates. These values are then calculated to determine how far the two valeus are in miles. This distance is then printed onto the page.
 
 
 