from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main(request, *args, **kwargs):
	# Whether used is logged in
	user = request.user
	user_context = None
	if user and user.is_authenticated:
		user_context = {'u': user}
	return HttpResponse(render(request, 'index.html', {'u_ctx': user_context}))
