from flask import Flask
from simulador_aws import crear_instancia_ec2_simulada, listar_buckets_s3_simulado

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Bienvenido a la Simulación de AWS</h2>
        <p><a href="/simular">Simular tareas de AWS</a></p>
    '''

@app.route('/simular')
def simular():
    # Llamamos a las funciones de simulación de AWS
    mensaje_ec2 = crear_instancia_ec2_simulada()
    lista_buckets = listar_buckets_s3_simulado()

    # Mostramos los resultados en la página
    return f'''
        <h3>Simulación completada</h3>
        <p>{mensaje_ec2}</p>
        <p>Buckets S3 encontrados:</p>
        <ul>
            {"".join([f"<li>{bucket}</li>" for bucket in lista_buckets])}
        </ul>
        <a href="/">Volver</a>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
