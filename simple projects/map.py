from gmplot import gmplot
latitude = 20.89
longitude = 77.74

# Creating the plot object
gmap = gmplot.GoogleMapPlotter(latitude, longitude, 13)

# Adding a marker at the location
gmap.marker(latitude, longitude)

# Saving the map as an HTML file
gmap.draw("mymap.html")