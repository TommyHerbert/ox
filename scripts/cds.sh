#!/bin/bash
echo `date` 'activity detected in NewKnowledge folder' >> /home/oxadmin/ox/cds.log
source /home/oxadmin/ox/venv/bin/activate
python /home/oxadmin/ox/scripts/cds1.py $DIGITAL_OCEAN_TOKEN $LOAD_BALANCER_ID $DROPLET_ID
echo `date` 'called cds1.py' >> /home/oxadmin/ox/cds.log
python /home/oxadmin/ox/scripts/cds2.py
rm -r /home/oxadmin/ox/knowledge
rm -r /home/oxamin/ox/new_knowledge/knowledge
mv /tmp/ox/knowledge /home/oxadmin/ox
