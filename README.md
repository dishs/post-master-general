# Post Master General (Auto-Blogger)
Jobs & Workers for Jollie & Co.
===

Python based.  Use pyenv and pipenv to not go insane.

blogger.py - primary jobs


Server Fresh install
```
> sudo yum install python37
> curl -O https://bootstrap.pypa.io/get-pip.py
> python3 get-pip.py --user
> pip install --user pipenv
> sudo yum install epel-release (will defer you to an aws package)
> sudo yum install redis
> sudo systemctl start redis
> https://ahmadalsajid.medium.com/daemonizing-celery-beat-with-systemd-97f1203e7b32
> sudo systemctl daemon-reload
> sudo systemctl enable celeryd
> sudo systemctl start celeryd
```

### Command to run worker via Celery:

`celery -A wheelcircuit_blogger worker -B -l INFO --concurrency 1 -Q blogger_worker_queue`

### on MAC, use this to prevent laptop from sleeping

`caffeinate -s celery -A wheelcircuit_blogger worker -B -l INFO --concurrency 1 -Q blogger_worker_queue`

### To force run, use:

`caffeinate -s python3 wheelcircuit_blogger.py --force_run`

### Start Redis (as a service):

`brew services start redis`
`brew services stop redis`


### Start Redis (manually - good for debugging):

`redis-server --loglevel verbose`
`redis-server --loglevel debug`

### MONGO

`/opt/homebrew/etc/mongod.conf`

LOG: `/opt/homebrew/var/log/mongodb/mongo.log`

DATA: `/opt/homebrew/var/mongodb`

### CLEAR ALL PENDING CELERY JOBS

`celery -A wheelcircuit_blogger purge --queues blogger_worker_queue`
`redis-cli KEYS "celery*" | xargs redis-cli DEL`

### BACKUP DB
mongodump --uri="mongodb://localhost:27017" --db powercompanidb --out /Users/dushyant/Workspace/pystuff/mongo/dump

### DB Indexes to speed up build
db.youtubeVideos.createIndex({ published: 1, owner: 1 })
db.youtubeVideos.createIndex({ createdAt: -1 })
db.youtubeVideos.createIndex({ published: 1, owner: 1, channel_name: 1 })
