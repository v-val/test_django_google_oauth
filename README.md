# test_django_google_oauth
Example of Django project with failing Google OAuth

Present example follows [this guide](https://whizzoe.medium.com/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5),
but doesn't work as expected producing following error:

{'provider_id': 'google', 'error': 'unknown', 'exception': 'Error retrieving access token: b\'{\\n  "error": "invalid_request",\\n  "error_description": "Credentials in post body and basic Authorization header do not match"\\n}\'', 'extra_context': {}}

