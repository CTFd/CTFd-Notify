# CTFd-Notify

A CTFd plugin to communicate with a [ThunderPush](https://github.com/thunderpush/thunderpush) server to send push notifications to users. 

It will also request browser notification permissions and fallback to an HTML based notification if the user doesn't grant the permission. 

# Install

1. Setup a ThunderPush Server and make note of the url, port, client\_secret, and server\_secret. 

    The following Docker command can help you:

    ```
    docker run -d -p 8080:8080 \
        -e PUBLIC_KEY=<client_secret> \
        -e PRIVATE_KEY=<server_secret> \
        kjagiello/thunderpush
    ```

2. Copy or clone this repository into CTFd/plugins with the folder name `notify`:

    `git clone https://github.com/CTFd/CTFd-Notify.git notify`
    
3. Configure the plugin in the Admin Panel and specify the url, port, client\_secret, and server\_secret for Thunderpush. 
