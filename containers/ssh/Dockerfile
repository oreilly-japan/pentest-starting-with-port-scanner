FROM ubuntu:22.04

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install necessary packages
RUN apt update \
    && apt -y install \
        iputils-ping \
        net-tools \
        openssh-server

RUN mkdir /var/run/sshd
RUN mkdir ~/Documents

RUN echo 'example_secret' > ~/Documents/credential.txt
RUN echo 'root:password' | chpasswd

# Settings to allow password login
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
