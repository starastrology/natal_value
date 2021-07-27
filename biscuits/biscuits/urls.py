from django.http import HttpResponse
from django.views import View

class B(View):
    def get(self, request):
        html = "<!DOCTYPE html><head><link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC' crossorigin='anonymous'><script src='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js' integrity='sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM' crossorigin='anonymous'></script>"
        html += "<link rel='shortcut icon' href='/favicon.ico'/><title>Star Astrology!</title></head>"
        html += "<body style='background-color: maroon; color: white;'><div class='container'><h1>Value of Natal Chart</h1>"
        html += "<form action='/estimate' method=GET><div class='mb-3'><label class='form-label' for='month'>Month</label><input required class='form-control' type=number name=month id='month' /></div><div class='mb-3'><label class='form-label' for='day'>Day</label><input class='form-control' required type=number name=day id='day' /></div><div class='mb-3'><label for='year' class='form-label'>Year</label><input class='form-control' required type=number name=year id='year' /></div><button type=submit class='btn btn-primary'>Submit</button><div class='form-text'>This website uses <a href='https://www.astro.com/astrowiki/en/Domicile' target=_blank>domiciles</a> to determine the value of your natal chart.</div></form>"
        html += "</div></body></html>"
        return HttpResponse(html)

    def do_some_stuff(request):
        import astro
        html = "<!DOCTYPE html><head><link rel='shortcut icon' href='/favicon.ico'/><title>" + request.GET['month'] + "/" + request.GET['day'] + "/" + request.GET['year'] + "</title><style> body{background-color: #80f; text-align: center;} table{text-align:center;} tr{background-color: #c328b1;} tr:nth-child(odd){background-color: pink;} th{background-color: cyan !important;} a{color: white;} a:visited{color: black;} h3{background-color: white; font-size: 35px;} div{margin: auto; text-align: center;}</style></head>"
        html += "<body><h1>Estimated Value</h1>"
        estimated_value = astro.get_estimated_value(request.GET['year'], request.GET['month'], request.GET['day'])[0]
        planets = astro.get_estimated_value(request.GET['year'], request.GET['month'], request.GET['day'])[1]
        summa_cumma_latte = astro.get_estimated_value(request.GET['year'], request.GET['month'], request.GET['day'])[2]
        html += "<h3>" + str(estimated_value) + "</h3>"
        html += "<div><table border=1 align=center><tr><th>Planet</th><th>Sign</th><th>Value</th></tr><tr><td>Sun</td><td>" + planets[0] + "</td><td>" + str(summa_cumma_latte[0]) + "</td></tr>"
        html += "<tr><td>Moon</td><td>" + planets[1] + "</td><td>" + str(summa_cumma_latte[1]) + "</td></tr>"
        html += "<tr><td>Mercury</td><td>" + planets[2] + "</td><td>" + str(summa_cumma_latte[2]) + "</td></tr>"
        html += "<tr><td>Venus</td><td>" + planets[3] + "</td><td>" + str(summa_cumma_latte[3]) + "</td></tr>"
        html += "<tr><td>Mars</td><td>" + planets[4] + "</td><td>" + str(summa_cumma_latte[4]) + "</td></tr>"
        html += "<tr><td>Jupiter</td><td>" + planets[5] + "</td><td>" + str(summa_cumma_latte[5]) + "</td></tr>"
        html += "<tr><td>Saturn</td><td>" + planets[6] + "</td><td>" + str(summa_cumma_latte[6]) + "</td></tr></table></div>"
        html += "</br><a href='/'>Back</a>"
        html += "</body></html>"
        return HttpResponse(html)
    
from django.conf.urls import url

urlpatterns = [
    url(r'^$', B.as_view(), name='b'),
    url(r'^estimate', B.do_some_stuff, name='estimate'),
]
