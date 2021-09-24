from google.cloud import bigquery
from flask import Flask, request
import json


app = Flask(__name__)


def querysomething(json_object):
    # https://googleapis.dev/python/bigquery/latest/generated/google.cloud.bigquery.client.Client.html#google.cloud.bigquery.client.Client.from_service_account_info
    client = bigquery.Client.from_service_account_info(json_object)
    # example below stolen from:
    # https://cloud.google.com/bigquery/docs/reference/libraries#using_the_client_library
    query = """
        SELECT name, SUM(number) as total_people
        FROM `bigquery-public-data.usa_names.usa_1910_2013`
        WHERE state = 'TX'
        GROUP BY name, state
        ORDER BY total_people DESC
        LIMIT 20
    """
    query_job = client.query(query)  # Make an API request.
    print("The query data:")
    for row in query_job:
        # Row values can be accessed by field name or index.
        print("name={}, count={}".format(row[0], row["total_people"]))


@app.route("/api/query", methods=["POST"])
def api_query():
    print(request.is_json)
    json_object = json.loads(request.get_json())
    print(json_object)
    querysomething(json_object)
    return "ok"


if __name__ == "__main__":
    app.run(debug=True)
