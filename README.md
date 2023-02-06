# AutoTaskList
AutoTaskList by peaky2222

1. install qinglong

# this is the latest version qinglong dashborad, before you install it, you must need docker 

docker run -dit \
--name ql \
--hostname ql \
--restart always \
-p 5700:5700 \
-v $PWD/ql/config:/ql/config \
-v $PWD/ql/log:/ql/log \
-v $PWD/ql/db:/ql/db \
-v $PWD/ql/scripts:/ql/scripts \
-v $PWD/ql/jbot:/ql/jbot \
whyour/qinglong:latest

2. ql repo #this git
3. create a new AutoConfig.py in script manage according to model AutoConfig.py and input your cookies
4. done
