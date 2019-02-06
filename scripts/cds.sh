#!/bin/bash
echo `date` 'activity detected in NewKnowledge folder' >> /home/oxadmin/ox/cds.log # TODO: put in logs directory
source /home/oxadmin/ox/venv/bin/activate # TODO: Do I need this?
python /home/oxadmin/ox/scripts/cds1.py $DIGITAL_OCEAN_TOKEN $LOAD_BALANCER_ID $DROPLET_ID &>> /home/oxadmin/ox/logs/cds1.log
echo `date` 'called cds1.py' >> /home/oxadmin/ox/cds.log
supervisorctl stop ox &>> /home/oxadmin/ox/cds.log
echo `date` 'stopped the app server' >> /home/oxadmin/ox/cds.log
python /home/oxadmin/ox/scripts/cds2.py &>> /home/oxadmin/ox/logs/cds2.log
echo `date` 'called cds2.py' >> /home/oxadmin/ox/cds.log
supervisorctl start ox &>> /home/oxadmin/ox/cds.log
echo `date` 'started the app server' >> /home/oxadmin/ox/cds.log
python /home/oxadmin/ox/scripts/cds3.py $DIGITAL_OCEAN_TOKEN $LOAD_BALANCER_ID $DROPLET_ID &>> /home/oxadmin/ox/logs/cds3.log
echo `date` 'called cds3.py' >> /home/oxadmin/ox/cds.log

