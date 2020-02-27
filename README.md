# hungry?

![screenshot](http://mchrh.me/img/hungry.png "Hompeage")


Django webapp that searches through a personal database of recipes (created with the admin/ part of django).
Clone the repo, fetch a database of recipes on the internet (or make your own) - it has my db by default, run the server and you should be good to go.

You can try it yourself [here.](https://lit-basin-64608.herokuapp.com/)

# How to add your own recipes?
After cloning the repo, and running your django server, head over to localhost:8000/admin and log in. 

![alt text](http://mchrh.me/img/1.png "1")


Click on add 

![alt text](http://mchrh.me/img/2.png "2")


The id attribute is not important, name is the name of the recipe you wanna add, and ING1 through ING5 are the ingredients the recipe contains (you could add more ING fields by tweaking the webapp/models.py file).

