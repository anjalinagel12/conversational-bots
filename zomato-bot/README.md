1. Zomato bot git location:**https://github.com/anjalinagel12/conversational-bots/tree/master/zomato-bot
**
2. It has Dockerfile as well, please use this command for installing rasa (image)
**docker build -t ras_1.10.0 .**

3. create your docker container at any port using the same docker image from above step.
**sudo docker run -itd -p 6200:5002  --restart unless-stopped --name zomato_bot <docker_image>
**​ 
4. clone the git repo, and run it using this command: 
  **rasa run actions & rasa shell
**  (you can also train the model, command: rasa train)
