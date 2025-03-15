import tornado.web
import asyncio
from routes.route import routes


async def main():
    application = tornado.web.Application(
        routes,
        template_path="templates",  # caminho dos templates
        debug=True,                 # modo de depuração
        autoreload=True,            # recarregar quando o código mudar
        compress_response=True,     # comprimir resposta
        serve_traceback=True,       # mostrar rastreamento
        static_path="static",        # caminho estático
        static_url_prefix="/static/"  # prefixo do URL estático
    )
    server = application.listen(8888)
    # Criar um evento asyncio para encerramento
    shutdown_event = asyncio.Event()

    async def shutdown():
        print("\nA encerrar o servidor...")
        server.stop()
        await server.close_all_connections()
        shutdown_event.set()
        print("Servidor foi encerrado com sucesso")

    try:
        print("Servidor em execução em http://localhost:8888")
        print("Pressione Ctrl+C para parar o servidor")
        await shutdown_event.wait()
    except KeyboardInterrupt:
        await shutdown()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Servidor foi encerrado com sucesso")
        pass
