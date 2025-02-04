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
COPY flag/s3cond_101.txt /etc/s/e/c/s3cond_101.txt
COPY flag/f1nal.txt /home/eagle/f1nal.txt

RUN chmod 444 /home/shiba/p@rt1.txt && \
    chmod 444 /etc/s/e/c/s3cond_101.txt && \
    chmod 600 /home/eagle/f1nal.txt && \
    chown root:root /home/shiba/p@rt1.txt /etc/s/e/c/s3cond_101.txt /home/eagle/f1nal.txt

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

RUN for i in $(seq 1 100); do \
        touch /var/s3cond_$i.txt /opt/s3cond_$i.txt /boot/s3cond_$i.txt \
              /root/s3cond_$i.txt /tmp/s3cond_$i.txt /usr/local/s3cond_$i.txt \
              /mnt/s3cond_$i.txt /lib/s3cond_$i.txt /srv/s3cond_$i.txt \
              /etc/s3cond_$i.txt /etc/s/s3cond_$i.txt /etc/s/e/s3cond_$i.txt \
              /etc/s/e/c/r/s3cond_$i.txt /etc/s/e/c/r/e/s3cond_$i.txt \
              /etc/s/e/c/r/e/t/s3cond_$i.txt; \
    done && \
    chmod 444 /var/s3cond_*.txt /opt/s3cond_*.txt /boot/s3cond_*.txt \
              /root/s3cond_*.txt /tmp/s3cond_*.txt /usr/local/s3cond_*.txt \
              /mnt/s3cond_*.txt /lib/s3cond_*.txt /srv/s3cond_*.txt \
              /etc/s3cond_*.txt /etc/s/s3cond_*.txt /etc/s/e/s3cond_*.txt \
              /etc/s/e/c/r/s3cond_*.txt /etc/s/e/c/r/e/s3cond_*.txt \
              /etc/s/e/c/r/e/t/s3cond_*.txt



RUN find / -type d -not -path "/tmp" -exec setfacl -m u:shiba:r-x {} + 2>/dev/null
RUN find / -type d -not -path "/tmp" -exec setfacl -m u:eagle:r-x {} + 2>/dev/null

RUN chmod 555 /home/shiba
RUN chmod 555 /home/eagle
RUN chmod 777 /var/radiohead/nirvana/muse/

RUN echo '*/3 * * * * root rm -rf /tmp/* &> /dev/null' > /etc/cron.d/clean_tmp && \
    chmod 644 /etc/cron.d/clean_tmp && \
    crontab /etc/cron.d/clean_tmp

EXPOSE 3979
ENTRYPOINT service cron start && /usr/sbin/sshd -D
