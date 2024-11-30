
Installing instructions

1. create a virtual environment
2. clone this project: git clone https://github.com/adikele/ship-route-plotter
3. Using the terminal: move into the same directory that contains the file "manage.py"
   (this is the inner ship-route-plotter-master directory)
4. install dependencies: pip install -r requirements.txt
5. run the program: python manage.py runserver

To check if the program works successfully:
--> when the program is run, visit the page http://127.0.0.1:8000/helsintalinn/bargraphs/
--> choose one of the two radio options 
--> a partial map of Finland with two routes will appear; these are the partial routes of two ships

TODO:

1. leaflet frontend that will:
   (i) show map and routes as currently appear
   (ii) for the PART OF THE ROUTE with non zero "S_BEND" column values, the route will be marked in a different colour
