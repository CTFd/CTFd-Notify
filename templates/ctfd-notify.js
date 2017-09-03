//http://stackoverflow.com/a/2648463 - wizardry!
String.prototype.format = String.prototype.f = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};

var push_status = Push.Permission.get();
var notification_wrapper = '' +
'<div id="notification_wrapper" class="row" role="alert" style="top: 0px; right: 0px; position: fixed; margin: 5px; z-index: 1050; max-width: 30%;">' +
'</div>' ;
var html = ''+
'<div class="alert alert-info alert-dismissible" role="alert">' +
    '<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>' +
    '<strong>{0}</strong>' +
    '<p>{1}</p>' +
'</div>';

if ( push_status === Push.Permission.DEFAULT ) {
    Push.Permission.request();
} else if ( push_status === Push.Permission.GRANTED ) {
    Thunder.connect("{{ url }}:{{ port }}", "{{ secret }}", ["all_teams"], {log: true});
    Thunder.listen(function(message) {
        Push.create(message.title, {
            body: message.msg,
            timeout: 10000,
            onClick: function () {
                window.focus();
                this.close();
            }
        });
    });
} else {
    $('html').append(notification_wrapper);
    Thunder.connect("{{ url }}:{{ port }}", "{{ secret }}", ["all_teams"], {log: true});
    Thunder.listen(function(message) {
        console.log(message);
        var message = html.format(message.title, message.msg);
        $('#notification_wrapper').append(message);

    });
}