import flet as ft


def sumar(text_field, text_field2, page):
    primer =int(text_field.value)
    segundo =int(text_field2.value)
    resul=primer+segundo
    dialog= ft.AlertDialog(
        title=ft.Text("resultado"),
        content=ft.Text(f"el resultado es:{resul}"),
        actions=[
            ft.TextButton("Da click para salir", on_click=lambda e: close_dialog(page))]
    )

def restar(text_field, text_field2, page):
    primer =int(text_field.value)
    segundo =int(text_field2.value)
    resul=primer-segundo
    dialog= ft.AlertDialog(
        title=ft.Text("resultado"),
        content=ft.Text(f"el resultado es:{resul}"),
        actions=[
            ft.TextButton("Da click para salir", on_click=lambda e: close_dialog(page))]
    )

def multiplicar(text_field, text_field2, page):
    primer =int(text_field.value)
    segundo =int(text_field2.value)
    resul=primer*segundo
    dialog= ft.AlertDialog(
        title=ft.Text("resultado"),
        content=ft.Text(f"el resultado es:{resul}"),
        actions=[
            ft.TextButton("Da click para salir", on_click=lambda e: close_dialog(page))]
    )
    
def dividir(text_field, text_field2, page):
    primer =int(text_field.value)
    segundo =int(text_field2.value)
    resul=primer/segundo
    dialog= ft.AlertDialog(
        title=ft.Text("resultado"),
        content=ft.Text(f"el resultado es:{resul}"),
        actions=[
            ft.TextButton("Da click para salir", on_click=lambda e: close_dialog(page))]
    )

def limpiar(text_field, text_field2, page):
    text_field = ft.TextField(label="")
    text_field2 = ft.TextField(label="")

    page.dialog =dialog
    page.dialog.open = True
    page.update()

def close_dialog(page):
    page.dialog.open = False
    page.update()

def main(page: ft.Page):
    page.title="calculadora chafa"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor="red"

    num1=ft.Text("primer numero",
                 style=ft.TextStyle(size=20,weight="bold"))

    num2=ft.Text("segundo numero",
                 style=ft.TextStyle(size=20,weight="bold"))
    
    lblresult=ft.text("resultado: ",color="blue")

    btnsumar=ft.ElevatedButton("+",
                            color="black",
                            width=100,
                            height=50,
                            on_click=lambda e: sumar(text_field,text_field2, page))
    
    btnrestar=ft.ElevatedButton("-",
                            color="black",
                            width=100,
                            height=50,
                            on_click=lambda e: restar(text_field,text_field2, page))

    btnmultiplicar=ft.ElevatedButton("*",
                            color="black",
                            width=100,
                            height=50,
                            on_click=lambda e: multiplicar(text_field,text_field2, page))
    
    btndividir=ft.ElevatedButton("/",
                            color="black",
                            width=100,
                            height=50,
                            on_click=lambda e: dividir(text_field,text_field2, page))

    btnlimpiar=ft.ElevatedButton("limpiar",
                            color="black",
                            width=100,
                            height=50,
                            on_click=lambda e: limpiar(text_field,text_field2, page))
    

    text_field = ft.TextField(label="")

    text_field2 = ft.TextField(label="")

    def limpiar(e):
        page.update()

    page.add(
        ft.Row
        ft([ft.Column([num1,text_field,num2,text_field2,lblresult,ft.Row([btnsumar,btnrestar,btnmultiplicar,btndividir,btnlimpiar])]),],
               alignment=ft.MainAxisAlignment.CENTER,)
    )

ft.app(target=main)

ft.app(main)
