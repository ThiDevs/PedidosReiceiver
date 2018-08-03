import base64
import socket

while True:
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 7071
        serversocket.bind((host, port))
        serversocket.listen(5)
        clientsocket, addr = serversocket.accept()
        item = str(clientsocket.recv(8024), encoding='utf-8')
        Info = item.split("SEPARAPAL")[0]

        nome = Info.split(";")[0]
        setor = Info.split(";")[1]
        comprou = Info.split(";")[2]
        valor = Info.split(";")[3]

        import mysql.connector

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="produtos"
        )

        mycursor = mydb.cursor()
        sql = "insert into pedidos values (default,%s,%s,%s,%s,%s,%s)"


        item = item.split("SEPARAPAL")[1]


        linha = str(clientsocket.recv(8024), encoding='utf-8')
        item += linha
        while linha != "":
            linha = str(clientsocket.recv(8024), encoding='utf-8')
            item += linha
        fh = open(nome+"_"+setor+".png", "wb")
        fh.write(base64.decodebytes(str.encode(item)))
        fh.close()

        val = (nome, setor, comprou, valor, '2018-05-05', fh.name)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

        clientsocket.close()
    except Exception:
        pass