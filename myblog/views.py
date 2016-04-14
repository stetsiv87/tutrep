from django.shortcuts import render

def post_list(request):
    return render(request, 'myblog2/post_list.html', {})
