import justpy as jp


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Anlysis of course Reviews ", classes="text-h1 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text= "Graficos representativos")
    return wp

jp.justpy(app)