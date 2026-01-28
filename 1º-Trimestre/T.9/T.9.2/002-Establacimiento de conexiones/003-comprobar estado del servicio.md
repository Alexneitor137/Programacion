AlexCS@Ubuntu:~$ systemctl status mongod
● mongod.service - MongoDB Database Server
     Loaded: loaded (/usr/lib/systemd/system/mongod.service; disabled; preset: >
     Active: active (running) since Wed 2026-01-28 08:58:55 UTC; 12s ago
       Docs: https://docs.mongodb.org/manual
   Main PID: 7456 (mongod)
     Memory: 99.8M (peak: 100.1M)
        CPU: 265ms
     CGroup: /system.slice/mongod.service
             └─7456 /usr/bin/mongod --config /etc/mongod.conf
lines 1-9/9 (END)
