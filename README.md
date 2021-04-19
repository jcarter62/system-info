# system-info

Application to be used by IT staff for typical sys admin activities.

---
Environment variables used:

<pre>
APP_HOST: ip to listen, if not provided listens to 0.0.0.0
APP_PORT: port number to listen, if not provided listens to port 5000
APP_ADMIN_NET: administrative network allowed access.
This is either a network (i.e. 192.168.1.) or a file name listing 
networks one per line.
</pre>
---
APP_ADMIN_NET example file:<br>
<pre>
10.100.20.
192.168.50.40
</pre>
The first network will match any host with ip prefix of 10.100.20, 
and the second line "192.168.50.40" will match only the specific address of 192.168.50.40.

