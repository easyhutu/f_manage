FROM python:3.6

ENV TZ Asia/Shanghai
ENV PATH /usr/local/bin:$PATH
ENV LANG en_US.UTF-8
ENV PYTHONIOENCODING utf-8
ENV PYTHONPATH /work
ENV NOSE_NOCAPTURE 1

RUN apt-get update --no-install-recommends -y \
    && apt-get dist-upgrade -y \
    && apt-get install -y vim tree curl net-tools iputils-ping dstat htop \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /work
COPY . /work
RUN pip install -r /work/requirements.txt

WORKDIR /work
EXPOSE 5000
CMD ["/usr/bin/env", "python", "main.py"]