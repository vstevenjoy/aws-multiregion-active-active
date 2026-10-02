# 5-Minute Hackathon Demo Script

## 1. Problem
"We want an application that can continue serving requests from more than one AWS Region instead of depending on a single regional application stack."

## 2. Architecture
"We deployed API Gateway and Lambda in Stockholm and Frankfurt. Both Lambda functions read the incident data from our DynamoDB table in Stockholm."

## 3. Region A live test
Open the Stockholm endpoint and request `INC001`.

Say: "This request was processed by the Stockholm Lambda, shown by `eu-north-1` in the response."

## 4. Region B live test
Open the Frankfurt endpoint and request `INC001`.

Say: "Now the same API operation is processed by the Frankfurt Lambda, shown by `eu-central-1`. It returns the same incident record."

## 5. Monitoring
Open the CloudWatch dashboard.

Say: "CloudWatch lets us monitor invocations and errors for both regional Lambda functions."

## 6. Limitation
If asked whether the database is fully multi-region:

"Our current Free Plan implementation keeps one DynamoDB table in Stockholm. The API and compute layers are multi-region. A production extension would add multi-region data replication and global traffic routing."
