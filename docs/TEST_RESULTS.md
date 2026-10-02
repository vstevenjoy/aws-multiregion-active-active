# Test Results

## Region A

**Endpoint:** `GET /incident/INC001`  
**Region:** `eu-north-1`  
**Result:** HTTP 200 / Incident found

## Region B

**Endpoint:** `GET /incident/INC001`  
**Region:** `eu-central-1`  
**Result:** HTTP 200 / Incident found

## Common data returned

- Incident ID: `INC001`
- Title: `Road service interruption`
- Status: `OPEN`
- Created at: `2026-09-28T18:00:00Z`

## Monitoring

CloudWatch dashboard contains invocation and error metrics for both Lambda functions.
