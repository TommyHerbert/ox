#!/bin/bash
echo `date` 'activity detected in NewKnowledge folder' >> /home/oxadmin/ox/cds.log
source /home/oxadmin/ox/venv/bin/activate
python /home/oxadmin/ox/scripts/cds1.py $DIGITAL_OCEAN_TOKEN $LOAD_BALANCER_ID $DROPLET_ID
echo `date` 'called cds1.py' >> /home/oxadmin/ox/cds.log
python /home/oxadmin/ox/scripts/cds2.py
echo `date` 'called cds2.py' >> /home/oxadmin/ox/cds.log
