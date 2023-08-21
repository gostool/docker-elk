from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['http://0.0.0.0:9200'],  # scheme, host, and port
    basic_auth=('elastic', 'changeme'),
    verify_certs=False
)




def main():
    if not es.ping():
        raise ValueError("Elasticsearch is not running")
    print(es.info())

if __name__ == '__main__':
    main()