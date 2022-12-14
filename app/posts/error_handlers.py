from flask import render_template


def handle_bad_request(e):
    return render_template('404.html'), 404


def internal_server_error(e):
    return render_template('500.html'), 500
