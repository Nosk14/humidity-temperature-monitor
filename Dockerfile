FROM raspbian/stretch
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY humidity-temperature-monitor /usr/local/humidity-temperature-monitor/
CMD python3 /usr/local/humidity-temperature-monitor/monitor.py
