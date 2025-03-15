# Documentação do Servidor Tornado

## Visão Geral

Este é um servidor web robusto desenvolvido com o framework Tornado em Python, oferecendo uma solução versátil para aplicações web modernas. O projeto demonstra a implementação de uma aplicação web com suporte completo a templates e gestão eficiente de rotas, sendo ideal tanto para renderização de templates quanto para desenvolvimento de APIs.

### Características Principais

- **Servidor Assíncrono**: Utiliza o poder do Tornado para processamento assíncrono eficiente
- **Suporte a Templates**: Sistema integrado de templates para renderização dinâmica
- **API Ready**: Estrutura preparada para implementação de APIs RESTful
- **Debug Mode**: Configuração de desenvolvimento com auto-reload
- **Compressão de Resposta**: Otimização automática do tráfego de rede

## Requisitos

- Python 3.x
- Tornado 6.4.2

## Instalação

### Windows

1. Criar ambiente virtual:
```bash
python -m venv venv
# ou
py -3.12 -m venv venv
```

2. Ativar ambiente virtual:
```bash
venv\Scripts\activate
```

### Linux/macOS

1. Criar ambiente virtual:
```bash
python3 -m venv venv
```

2. Ativar ambiente virtual:
```bash
source venv/bin/activate
```

### Instalar Dependências

Depois de ativar o ambiente virtual, instale as dependências necessárias:
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Para desativar o ambiente virtual em qualquer sistema operativo:
```bash
deactivate
```

## Estrutura do Projeto

```
/
├── app.py           # Arquivo principal do servidor
├── middlewares/     # Middlewares da aplicação
│   └── __init__.py
├── routes/          # Módulo de rotas
│   ├── __init__.py
│   └── route.py     # Implementação das rotas
├── static/          # Arquivos estáticos
│   ├── css/         # Estilos CSS
│   │   └── main.css
│   ├── js/          # Scripts JavaScript
│   │   └── darkMode.js
│   └── img/         # Imagens
│       └── favicon.png
├── templates/       # Diretório de templates
│   └── index.html   # Template principal
├── utils/           # Utilitários
│   └── __init__.py
└── requirements.txt # Dependências do projeto
```

## Arquitetura do Servidor

### Configuração Principal (app.py)

O servidor é configurado no ficheiro `app.py`, que implementa:

- **Configuração Base**:
  - Framework Tornado para processamento assíncrono
  - Sistema de rotas modular
  - Suporte a templates
  - Compressão automática de respostas

- **Características Avançadas**:
  - Debug mode para desenvolvimento
  - Auto-reload para atualizações em tempo real
  - Gestão de erros com traceback detalhado
  - Encerramento gracioso do servidor

### Sistema de Rotas (routes.py)

- Implementação modular de rotas
- Suporte a múltiplos métodos HTTP (GET, POST)
- Integração com sistema de templates
- Processamento assíncrono de requisições

## Uso

### Iniciar o Servidor

1. Ative o ambiente virtual conforme instruções acima
2. Execute o servidor:
```bash
python app.py
```
3. Acesse `http://localhost:8888` no navegador

### Desenvolvimento de Templates

Os templates são armazenados no diretório `templates/` e utilizam a sintaxe do Tornado:

```html
<!-- Exemplo de template -->
<html>
  <body>
    {{ message }}
  </body>
</html>
```

### Desenvolvimento de API

Exemplo de implementação de endpoint API:

```python
class ApiHandler(tornado.web.RequestHandler):
    def get(self):
        self.send_response(
            message=f"Tornato Project {year}",
            data={"version": VERSION, "method": self.request.method},
        )
```

## Gestão do Servidor

### Encerramento Seguro

O servidor pode ser encerrado de forma segura através de:
- Ctrl+C (SIGINT)
- Comando de terminação do sistema (SIGTERM)

O sistema implementa encerramento gracioso para garantir que todas as requisições em andamento sejam concluídas adequadamente.

## Dicas de Desenvolvimento

- Utilize o modo debug durante o desenvolvimento
- Implemente tratamento de erros adequado
- Siga as práticas assíncronas do Tornado
- Mantenha a estrutura modular do projeto

## Resolução de Problemas

### Problemas Comuns

1. **Porta em Uso**:
   - Verifique se a porta 8888 está disponível
   - Altere a porta no arquivo `app.py` se necessário
   - 
   ```sh
    netstat -ano | findstr :8888
   ```
   - 
   ```sh	
   taskkill /PID <PID> /F
   ```

2. **Erro de Dependências**:
   - Confirme que o ambiente virtual está ativo
   - Verifique se todas as dependências foram instaladas

### Verifique ficheiro TODO.md