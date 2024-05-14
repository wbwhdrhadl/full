# Base image
FROM ubuntu:latest

# RUN command
RUN apt -y update && apt -y upgrade

# server execution
ENTRYPOINT [ "top" ]
CMD ["-d", "10"]
