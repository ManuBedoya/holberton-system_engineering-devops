# POSTMORTEM
## ISSUE SUMARY
In a date of august 22 of 2021 one container that have server nginx keep a problem with the port 80 that is the default listen the server when I made a request curl the server returned 

`curl: (7) Failed to connect to 0 port 80: Connection refused`

## TIMELINE TO 22/08/2021
**3:20:** After when I made the request with curl to server then returning the curl error where there is a problem in the port 80

**3:22:** the configurations files of nginx are reviwed

**3:23:** Find an innusual configuration in the file `/etc/nginx/sites-enabled/default` where found differents port and restrictions that aren't necessaries

**3:26:** Continuing to check the other files everuthing looked fine

**3:27:** the solution was to delete the file `/etc/nginx/sites-enabled/default` and redo the file with the file's configuration of `/etc/nginx/sites-available/default`

**3:30:** Restart the server and when I made the request with curl everything worked

## Root cause and resolution
The root cause of this outage was a bad configuration in the ports in the file `/etc/nginx/sites-enabled/default` in which the port 80 didn't listened that provocated a connection refused and the solution was change that configuration with the content of the file `/etc/nginx/sites-available/default` quicly, 10 minutes of the outage

## Corrective and preventive measures must contain
To prevent the issue is don't change the ports of the configurations files in the Nginx in case that is neccesary, do the necessary changes in both files `/etc/nginx/sites-enabled/default` and `/etc/nginx/sites-available/default` for don't have confussions in the connection