# Assignment 2: Plottings

This assignment is about plotting.

## How to hand in

The assignment is expected to be published on GitHub, but the actual hand-in is on peergrade and should contain only a link to a MyBinder. See the notebook 12-Assignments if you don't know what that means.

## Task

Create data visualizations comparing different groups of Copenhagen citizens. For example:

- Create a bar plot that shows distribution of german and british citizens in terms of age.
- How many French are there compared to Germans and how are they distributed over various neighbourhoods?
- Create a pie chart showing the 5 major citizen groups of age between 20-65
- (red assignment) Try to add the markers that you get from the GeoJson response exercise 2 to the map.

## Hints

Hint: Make use of https://www.dst.dk/da/Statistik/dokumentation/Times/forebyggelsesregistret/statkode.aspx to find the citizenship category numbers.

For exercise 4 make use of:

folium.Marker(
[12.578995447902946, 55.713167699503515],
popup='some text here'
).add_to(map_osm)
and follow the documentation at http://folium.readthedocs.io/en/latest/quickstart.html
