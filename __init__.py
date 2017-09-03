from flask import (
    abort,
    request,
    render_template,
    redirect,
    jsonify,
    Blueprint,
    url_for,
    Response
)

from CTFd.models import db
from CTFd.utils import admins_only, get_config, set_config
from CTFd import utils

from thunderclient import Thunder

def load(app):
    notify = Blueprint('notify', __name__, template_folder='templates')
    notify_static = Blueprint('notify_static', __name__, static_folder='static')

    @notify.route('/admin/plugins/notify/send', methods=['GET', 'POST'])
    @admins_only
    def notify_send():
        if request.method == 'GET':
            return render_template('notify.html')
        elif request.method == 'POST':
            msg = request.form.get('msg')
            title = request.form.get('title')
            client_secret = get_config('thunderpush_client_secret')
            server_secret = get_config('thunderpush_server_secret')
            thunderpush_url = get_config('thunderpush_url')
            thunderpush_port = get_config('thunderpush_port')
            t = Thunder(apikey=client_secret, apisecret=server_secret, host=thunderpush_url, port=thunderpush_port)
            t.send_message_to_channel(channel='all_teams', message={'title': title, 'msg': msg})
            return '', 200

    @notify.route('/notify/static/ctfd-notify.js', methods=['GET'])
    def notify_static_generator():
        client_secret = get_config('thunderpush_client_secret')
        thunderpush_url = get_config('thunderpush_url')
        thunderpush_port = get_config('thunderpush_port')
        js = render_template('ctfd-notify.js', url=thunderpush_url, port=thunderpush_port, secret=client_secret)
        return Response(js, mimetype='application/javascript')

    app.register_blueprint(notify)
    app.register_blueprint(notify_static, url_prefix='/notify')
    scripts = [
        "/notify/static/sockjs-0.3.4.min.js",
        "/notify/static/thunderpush.js",
        "/notify/static/push.min.js",
        "/notify/static/ctfd-notify.js"
    ]
    for s in scripts:
        utils.register_plugin_script(s)