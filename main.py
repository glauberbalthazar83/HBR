from fastapi import FastAPI, Form
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

app_web = FastAPI()
paginas = Jinja2Templates(directory='HBR/paginas')

#acrescentando um comentário para atualizar o GitHub

@app_web.get('/')
async def index(request: Request):
    context = {
        "request": request,
        "resultado":0
    }
    return paginas.TemplateResponse('calculadora.html', context=context)

@app_web.post('/calcular')
async def login(request: Request):
   
   form = await request.form()
   valor1 = float(form.get('valor1'))
   operador = form.get('operador')
   valor2 = float(form.get('valor2'))
   resultado = 0.0

   if(operador=="+"):
       resultado = valor1 + valor2

   if(operador=="-"):
       resultado = valor1 - valor2

   if(operador=="*"):
       resultado = valor1 * valor2

   if(operador=="/"):
       resultado = valor1 / valor2     

   contexto = {
        "request": request,
        "resultado": resultado
    }
   return paginas.TemplateResponse("calculadora.html", contexto)