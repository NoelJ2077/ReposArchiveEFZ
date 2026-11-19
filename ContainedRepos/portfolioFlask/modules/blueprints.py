from flask import Blueprint, request, render_template, current_app

# Define the blueprint
errors_bp = Blueprint('errors', __name__)
projects_bp = Blueprint('projects', __name__)

# Helper function for rendering errors
def render_err(error_code):
    """Base for rendering any error."""
    return render_template('error.html', error_code=error_code), error_code

# Error handling 404
@errors_bp.app_errorhandler(404)
def page_not_found(e):
    current_app.logger.error(f"Page not found: {request.url}")
    return render_err(404)

# Error handling 403
@errors_bp.app_errorhandler(403)
def forbidden(e):
    current_app.logger.error(f"Forbidden: {request.url}")
    return render_err(403)

# Error handling 500
@errors_bp.app_errorhandler(500)
def internal_server_error(e):
    current_app.logger.error(f"Internal Server Error: {request.url}")
    return render_err(500)

@projects_bp.route('/proj_1')
def proj_1():
    return render_template('project1.html')
@projects_bp.route('/proj_2')
def proj_2():
    return render_template('project2.html')
@projects_bp.route('/proj_3')
def proj_3():
    return render_template('project3.html')

