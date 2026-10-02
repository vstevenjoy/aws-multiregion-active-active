import json
import boto3

# DynamoDB table is hosted in Stockholm (eu-north-1)
dynamodb = boto3.resource("dynamodb", region_name="eu-north-1")
table = dynamodb.Table("service-incidents")


def lambda_handler(event, context):
    path_params = event.get("pathParameters") or {}
    incident_id = (
        path_params.get("incidentId")
        or event.get("incidentId")
        or "INC001"
    )

    response = table.get_item(Key={"incidentId": incident_id})
    item = response.get("Item")

    if item:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Incident found",
                "region": "eu-north-1",
                "incident": item
            })
        }

    return {
        "statusCode": 404,
        "body": json.dumps({
            "message": "Incident not found",
            "incidentId": incident_id,
            "region": "eu-north-1"
        })
    }
