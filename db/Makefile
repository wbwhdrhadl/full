profile: /etc/profile
	source $^
	source ~/.source
start:
	lsnrctl start
	netstat -ntlp
stop:
	lsnrctl stop
	netstat -ntlp
status:
	lsnrctl status
	netstat -ntlp
