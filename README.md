# interactiveBrokers
###Setup Headless gateway
```
# start ec2 instance
# ssh with port forwarding
Xvfb :1 -ac -screen 0 1024x768x24 &
export DISPLAY=:1
x11vnc -ncache 10 -ncache_cr -display :1 -forever -shared -logappend /var/log/x11vnc.log -bg -noipv6
Display=:1 ./ibgateway

```
