import tornado.web
from datetime import datetime

VERSION = "0.0.1"


# Manipulador Base para todas as rotas na aplicação, auxiliando no envio de respostas em formato JSON
class BaseHandler(tornado.web.RequestHandler):
    def send_response(self, message=None, data=None, status=200):
        response = {"status": status, "message": message, "data": data}
        self.set_header("Content-Type", "application/json")
        self.set_status(status)
        self.write(response)
    
    def prepare(self):
        # Configura CORS (pode ser ajustado conforme necessidade)
        self.set_header("Access-Control-Allow-Origin", "*")
        # Configura métodos permitidos
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.set_header("Access-Control-Allow-Credentials", "true")
        # Adiciona cabeçalhos de segurança
        self.set_header("X-Content-Type-Options", "nosniff")
        self.set_header("X-Frame-Options", "DENY")
        # Estas configuração mais permissiva deve ser usada apenas para desenvolvimento, não para produção
        self.set_header("Content-Security-Policy", "default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com")

    def validate_token(self, token):
        # Exemplo simples de validação de token, em desenvolvimento
        return token == "Bearer eIrxFA8QCXsfdhHpMemzbWaTaMEqmMDTLa8Kp7jw8BJtmY0bZQbKT1lakIkz0g12"


# Tratamento de erros 404 Não Encontrado ou 405 Método Não Permitido
class NotFoundHandler(BaseHandler):
    ALLOWED_METHODS = {"GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"}

    def prepare(self):
        requested_path = self.request.path
        if self.request.method not in self.ALLOWED_METHODS:
            self.send_response(
                message="Method Not Allowed",
                data={
                    "path": requested_path,
                    "method": self.request.method,
                    "allowed_methods": list(self.ALLOWED_METHODS),
                },
                status=405,
            )
        else:
            self.send_response(
                message="Not Found",
                data={"path": requested_path, "method": self.request.method},
                status=404,
            )

    def _unimplemented_method(self):
        pass

    get = post = put = delete = patch = options = _unimplemented_method

# Pagina Index so para teste do render
class MainHandler(BaseHandler):
    def get(self):
        year = datetime.now().year
        self.render("index.html", year=year)

# Rota da API com auth básica
class ApiHandler(BaseHandler):
    def prepare(self):
        super().prepare()
        # Checa autenticação mínima
        auth_header = self.request.headers.get("Authorization")
        if not auth_header or not self.validate_token(auth_header):
            self.set_status(401)
            self.finish("Unauthorized")
            return

    def get(self):
        year = datetime.now().year
        self.send_response(
            message=f"Tornato Project {year}",
            data={"version": VERSION, "method": self.request.method},
        )

    def post(self):
        year = datetime.now().year
        self.send_response(
            message=f"Tornato Project {year}",
            data={"version": VERSION, "method": self.request.method},
        )

# Definição das rotas
routes = [
    (r"/", MainHandler),
    (r"/api/v1", ApiHandler),  # Rota da API
    (r".*", NotFoundHandler),  # Captura todas as rotas não tratadas
]
