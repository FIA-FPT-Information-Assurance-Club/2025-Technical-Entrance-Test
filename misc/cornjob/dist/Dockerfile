FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends sudo openssh-server cron nano dos2unix acl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd && \
    echo 'Port 3979' >> /etc/ssh/sshd_config && \
    echo 'PermitRootLogin no' >> /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config

RUN adduser --disabled-password --gecos "" shiba && \
    adduser --disabled-password --gecos "" eagle

RUN echo 'shiba:shiba' | chpasswd && \
    echo 'eagle:-daylapassw0rdkhongthecrack-heheh!@#$#@!' | chpasswd

COPY flag/p@rt1.txt /home/shiba/p@rt1.txt
RUN mkdir -p /etc/s/e/c/r/e/t/
COPY flag/s3cond.txt /etc/s/e/c/s3cond.txt
COPY flag/f1nal.txt /home/eagle/f1nal.txt

RUN chmod 444 /home/shiba/p@rt1.txt && \
    chmod 444 /etc/s/e/c/s3cond.txt && \
    chmod 600 /home/eagle/f1nal.txt && \
    chown root:root /home/shiba/p@rt1.txt /etc/s/e/c/s3cond.txt /home/eagle/f1nal.txt

RUN chown -R eagle:eagle /home/eagle && \
    chmod -R 700 /home/eagle && \
    chmod 700 /home/eagle/f1nal.txt

RUN mkdir -p /var/radiohead/nirvana/muse/ && \
    chmod 777 /var/radiohead/nirvana/muse/

COPY assets/eagle_cronjob.sh /usr/bin/eagle_cronjob.sh

RUN dos2unix /usr/bin/eagle_cronjob.sh

RUN chmod 755 /usr/bin/eagle_cronjob.sh && \
    chown eagle:eagle /usr/bin/eagle_cronjob.sh

RUN echo '@reboot eagle /usr/bin/eagle_cronjob.sh &> /dev/null' > /etc/cron.d/eagle_cronjob && \
    echo '* * * * * eagle /usr/bin/eagle_cronjob.sh &> /dev/null' >> /etc/cron.d/eagle_cronjob && \
    chmod 644 /etc/cron.d/eagle_cronjob && \
    crontab -u eagle /etc/cron.d/eagle_cronjob

RUN touch /var/s3cond.txt /opt/s3cond.txt /boot/s3cond.txt \
         /root/s3cond.txt /tmp/s3cond.txt /usr/local/s3cond.txt \
         /mnt/s3cond.txt /lib/s3cond.txt /srv/s3cond.txt \
         /etc/s3cond.txt /etc/s/s3cond.txt /etc/s/e/s3cond.txt \
         /etc/s/e/c/s3cond.txt /etc/s/e/c/r/s3cond.txt \
         /etc/s/e/c/r/e/s3cond.txt /etc/s/e/c/r/e/t/s3cond.txt && \
    chmod 444 /var/s3cond.txt /opt/s3cond.txt /boot/s3cond.txt \
              /root/s3cond.txt /tmp/s3cond.txt /usr/local/s3cond.txt \
              /mnt/s3cond.txt /lib/s3cond.txt /srv/s3cond.txt \
              /etc/s3cond.txt /etc/s/s3cond.txt /etc/s/e/s3cond.txt \
              /etc/s/e/c/r/s3cond.txt \
              /etc/s/e/c/r/e/s3cond.txt /etc/s/e/c/r/e/t/s3cond.txt

RUN find / -type d -not -path "/tmp" -exec setfacl -m u:shiba:r-x {} + 2>/dev/null
RUN chmod 555 /home/shiba
RUN chmod 777 /var/radiohead/nirvana/muse/

EXPOSE 3979
ENTRYPOINT service cron start && /usr/sbin/sshd -D
