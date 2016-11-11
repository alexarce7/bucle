import web
render = web.template.render('views/')
urls = ('/bucle(.*)', 'bucle')
class bucle:
    def GET(self, datos):
        datos = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
        return render.bucle(datos)
if __name__=='__main__':
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()