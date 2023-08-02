import pymongo

# env variables
mongo_conn_str = (
	"mongodb+srv://kennethr:jldWyszwZi8bRtsN@data-main.ubaxa5i.mongodb.net/data_main"
)

# initialize mongo client
mongo_client = pymongo.MongoClient(mongo_conn_str).get_database("mqtt").RawSignals
mongo_cursor = mongo_client.find()
signals = list(mongo_cursor)