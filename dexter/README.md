# Dextor

Dextor is an ai that helps developer with their development related task. It uses OpenAI with multiple prompts to achieve the flow.
Use the API for creating a dexter instance
# Setup

```shell
make setup
```

# Run

```shell
make run
```

# API's

## 1. Create

Use the API for creating a dexter instance 

`POST`: `https://api.dexgpt.app/create/dex/`

##### Headers

```json
{ "Content-type": "application/json"}
```

##### Request

Open AI is free to use, Get your open ai key for [here](https://platform.openai.com/account/api-keys) 

```
{
    "key": "REPLACE_WITH_YOUR_OPEN_AI_KEY"
}
```

##### Response

Store instance id, it will be required for further transactions.

```
{
    "status": true,
    "payload": {
        "instance_id": "7740dd0b-8de5-4f2e-aac8-3d2bbf795102"
    },
    "message": "Dexter is ready to help"
}
```

## 2. Query

`POST`: `https://api.dexgpt.app/query/`

##### Headers

```json
{ "Content-type": "application/json"}
```

##### Request

Use instance id from previously stored id in [Create API](#create-api)

```
{
    "instance_id": "42b37e84-c36d-4af3-b69e-c00fb7a0d9e9",
    "query": "my name is saurabh pandey"
}
```

##### Response

```
{
  "status": true,
  "payload": "मेरा नाम सौरभ पांडेय है",
  "message": "Dexter is talking"
}
```

## 3. Get a list of available prompts

`GET`: `https://api.dexgpt.app/prompts/`

##### Headers

```json
{ "Content-type": "application/json"}
```

##### Response

```
{
  "status": true,
  "payload": [{
    "id": 1,
    "prompt_name": "Hindi Translation Prompt",
    "prompt_text": "Dexter translates the input to Hindi",
    "created_on": "2023-07-07T14:48:23.284412Z",
    "updated_on": "2023-07-07T14:48:23.284423Z",
    "created_by": 1
  }],
  "message": "Prompt added successfully"
}
```

## 4. Change Prompt

`POST`: `https://api.dexgpt.app/change/prompt/`

##### Headers

```json
{ "Content-type": "application/json"}
```

##### Request

Use instance id from previously stored id in [Create API](#create-api)
Prompt ID can be obtained from list of avalible prompts [Get a list of available prompts]()

```
{
    "prompt_id": 1,
    "instance_id": "42b37e84-c36d-4af3-b69e-c00fb7a0d9e9"
}
```

##### Response

```
{
    "status": true,
    "payload": {
        "instance_id": "42b37e84-c36d-4af3-b69e-c00fb7a0d9e9"
    },
    "message": "Dexter is ready to help"
}
```

