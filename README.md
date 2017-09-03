# CTFd-Notify

A CTFd plugin to communicate with a [ThunderPush](https://github.com/thunderpush/thunderpush) server to send push notifications to users. 

It will also request browser notification permissions and fallback to an HTML based notification if the user doesn't grant the permission. 

```
docker run -d -p 8080:8080 \
    -e PUBLIC_KEY=<client_secret> \
    -e PRIVATE_KEY=<server_secret> \
    kjagiello/thunderpush
```
