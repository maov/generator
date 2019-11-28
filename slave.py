from multiprocessing import Process,Pipe

def serialize(child_conn, data):
    child_conn.send('Done seen {} chars'.format(len(data)))
    child_conn.close()
