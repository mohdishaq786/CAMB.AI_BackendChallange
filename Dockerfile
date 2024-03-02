FROM python:3.11-alpine3.17
#RUN apt update && apt upgrade -y
#RUN apt get libgl1-mesa-dev libglfw3-dev libglu1-mesa libssl-dev libx11-dev libxcursor-dev libxt-dev libx11-xcb1 libxcb-render0 libxcb-shm0 libxcb-xfixes0 libxcb1 libxi6 libsm6 libegl1 libxkbcommon0 pip chrpath libxft-dev libgl1-mesa-glx libfreetype6 libfreetype6-dev -y
#RUN apt install lsb-release -y 
# RUN apt install curl -y 
# RUN apt install gpg -y 
#RUN curl -fsSL https://packages.redis.io/gpg | gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

#RUN echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

# RUN apt-get update
# RUN apt-get install redis -y
COPY . .
RUN pip install -r requirements.txt

EXPOSE 8080
RUN chmod +x run.sh

# CMD ["python3", "main.py"]
CMD ["/bin/sh", "-c", "./run.sh"]
