from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render_to_response

def detail(request):
    dict_values = {'fav_color': 'blue'}
    template_string = "My favorite color is {{ fav_color }}."
    c = Context(dict_values)
    t = Template(template_string)
    rendered_template = t.render(c)
    return HttpResponse(rendered_template)




def test(request):
    return render_to_response('ueTest.html')