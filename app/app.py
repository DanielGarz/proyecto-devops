from flask import Flask
from simulador_aws import crear_instancia_ec2_simulada, listar_buckets_s3_simulado

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Bienvenido a DevOps Simulacion</h2>
        <p><a href="/main">Simular tareas AWS</a></p>
    '''

@app.route('/simular')
def simular():
    crear_instancia_ec2_simulada()
    listar_buckets_s3_simulado()
    return '''
        <h3>✅ Simulación completada</h3>
        <p>Instancias EC2 y Buckets S3 simulados.</p>
        <a href="/">Volver</a>
    '''
