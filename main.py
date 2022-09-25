import flask

app = flask.Flask(__name__)

# route to the root url


@app.route('/')
@app.route('/index.html')
def root():
    # root template will render index.html
    return flask.render_template('index.html', page_title='Index')


@app.route('/me')
@app.route('/about-me.html')
def about():
    return flask.render_template('about-me.html', page_title='About ME')


@app.route('/project')
@app.route('/about-project.html')
def project():
    return flask.render_template('about-project.html', page_title='My PROJECT')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
