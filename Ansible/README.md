#This file is developed by Team 28 of COMP90024 of The University of Melbourne
#YING DU : 925566
#XINHUI LU : 965246
#MINCHENG LI : 889903
#MIAN WANG : 948291
#MINGZE XIA : 948737

- To create VMs ( For here, create two VMs at once )
	- put your openstack-rc file (download from Unimelb Research Cloud) to createVM file folder and rename to openrc.sh
	- put your key file under Ansible folder and rename it to mykey.key
	- run command line :
		./run-nectar.sh

- To deploy tweets_harvester server
	- open tweets_harvester.yaml and replace hosts to one of the ip address of your remote VMs
	- run command line :
		./run-harvester.sh

- To deploy web_server.yml
	- open web_server.yml and replace hosts to one of the ip address of your remote VMs
	- run command line :
		-./run-server.sh

- To Create Database Server
	- open hosts file and paste your ip address of VMs into the file
	- run command line :
 		- ./run-couchdb.sh