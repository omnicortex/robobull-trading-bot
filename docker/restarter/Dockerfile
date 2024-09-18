FROM docker:cli

#Start checking for user id, create if not exist. Run everyday at 12:30am
RUN echo "20 0 * * * docker restart robobull" >> /var/spool/cron/crontabs/root
RUN echo "40 0 * * * docker restart firefox" >> /var/spool/cron/crontabs/root

RUN echo "0 1 * * * docker stop robobull" >> /var/spool/cron/crontabs/root
RUN echo "50 0 * * * docker stop firefox" >> /var/spool/cron/crontabs/root

#Start trading at 9:40am on weekdays
RUN echo "45 9 * * 1-5 docker restart robobull" >> /var/spool/cron/crontabs/root
RUN echo "0 17 * * * docker stop robobull" >> /var/spool/cron/crontabs/root