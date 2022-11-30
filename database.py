from deta import Deta
# from dotenv import load_dotenv
# import os


# # load the environment variables
# load_dotenv(.env)
# DETA_KEY = os.getenv("DETA_KEY")
# deta = Deta(DETA_KEY)

deta = Deta("b0pvpc5o_X9jPX8XBrrDnvjNQtEAPqY65fwNiAHiM")


#Create and Connect to the database

db = deta.Base("predicted_database")

def insert_data(text, predict, confidence):
    return db.put({"key":predict, "text":text, "confidence_score":confidence})

# def insert_data(text, predict, confidence, all_probability):
#     return db.put({"key":predict, "text":text,
#                       "confidence":confidence, "all_probability":all_probability})

def fetch_all_data():
    res = db.fetch()
    return res.items


def get_period(predict):
    return db.get(predict)