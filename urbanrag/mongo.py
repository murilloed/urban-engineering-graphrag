"""Optional persistence adapter, requires pymongo; no remote DB configured."""
def persist(uri,docs,graph):
    from pymongo import MongoClient
    with MongoClient(uri,serverSelectionTimeoutMS=5000) as client:
        db=client.urban_portfolio; db.documents.create_index('id',unique=True)
        for d in docs: db.documents.update_one({'id':d['id']},{'$set':d},upsert=True)
        for source,targets in graph.items():
            db.relations.update_one({'_id':source},{'$set':{'targets':targets}},upsert=True)
