
1. Create a django run configuration as follows:
	-> Project: django01
	-> MainModule: ${workspace_loc:django01/manage.py}
	-> arguments: runserver 0.0.0.0:4444
	-> save the new configuration (ex: django01 server)
	-> Run the new configuration

2. Testing (open URL in any browser):
	-> Basic: http://127.0.0.1:4444/
	-> Admin page: http://127.0.0.1:4444/admin
	-> A static welcome page: http://127.0.0.1:4444/static/html/welcome.html
	
