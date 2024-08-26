from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

# Define uma classe que herda de SimpleHTTPRequestHandler para personalizar o comportamento do servidor
class MeuManipulador(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Verifica se o caminho da solicitação é '/'
        if self.path == '/':
            self.path = '/index.html'
        elif self.path == '/favicon.ico':
            self.send_response(404)
            self.end_headers()
            return
        # Chama o método do_GET da classe pai para lidar com a solicitação
        return SimpleHTTPRequestHandler.do_GET(self)

# Define uma função para obter o endereço IP da máquina
def obter_endereco_ip():
    try:
        # Cria um socket UDP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Conecta-se a um servidor externo
        endereco_ip = s.getsockname()[0]  # Obtém o endereço IP do socket
        s.close()
        return endereco_ip
    except:
        return "localhost"  # Retorna localhost se não for possível obter o endereço IP

# Define uma função para executar o servidor
def executar(servidor_classe=HTTPServer, manipulador_classe=MeuManipulador, endereco="localhost", porta=8000):
    # Configura o endereço e a porta do servidor
    endereco_servidor = (endereco, porta)
    servidor_http = servidor_classe(endereco_servidor, manipulador_classe)
    print(f"Servidor rodando em http://{endereco}:{porta}/")
    servidor_http.serve_forever()

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Obtém o endereço IP da máquina
    endereco_ip = obter_endereco_ip()
    # Chama a função executar para iniciar o servidor com o endereço IP obtido
    executar(endereco=endereco_ip)
