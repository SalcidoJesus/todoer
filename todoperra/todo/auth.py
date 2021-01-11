import functools

from flask import (
	Blueprint, flask, g, render_template, request, url_for, session
)

from werkzeug.security import check_password_hash, generate_password_hash

from todo.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@app.route('/register' methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		db, c = get_db()
		error = None
		c.execute(
			'SELECT id FROM user WHERE username = %s'
		)
		if not username:
			error = "y el usuario? pendejo"
		if not password:
			error = "y la contra? pendejo"
		elif c.fetchone() is not None:
			error = 'hey pendejo, {} ta ocupado'.format(username)

		if error is None:
			c.execute(
				'INSERT INTO user VALUES (NULL, %s, %s)',
				(username, generate_password_hash(password))
			)
			db.commit()

			return redirect(url_for('auth.login'))

		flash(error)

	return render_template('auth/register.html')