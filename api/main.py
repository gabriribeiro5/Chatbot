from uvicorn import run

'''
    Inicializa a execução da api atraves do servidor uvicorn
'''

if __name__ == "__main__":
    run("bot:app", host="0.0.0.0", port=8080, log_level="info", reload=True)