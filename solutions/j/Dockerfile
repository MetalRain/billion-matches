FROM debian:11.6

WORKDIR /app/

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "wget"]
RUN ["wget", "-O", "j.tar.gz", "https://www.jsoftware.com/download/j9.4/install/j9.4_linux64.tar.gz"]
RUN ["tar", "-xvf", "j.tar.gz"]
RUN ["chmod", "+x", "/app/j9.4/bin/jconsole"]

COPY install.j ./install.j
RUN ["/app/j9.4/bin/jconsole", "/app/install.j"]

COPY main.j ./main.j
CMD ["/app/j9.4/bin/jconsole", "/app/main.j"]