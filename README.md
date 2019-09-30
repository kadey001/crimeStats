# Hate Crime Stats API

## Usage

All responses will have the format

```json
[
	{
		"agencyName": "Name",
		"agencyType": "Type",
		"disability": #,
		"gender": #,
		"genderIdentity": #,
		"population": #,
		"race": #,
		"religion": #,
		"sexOrientation": #,
		"state": "State"
	},
]
```

Search by type

### Cities

**Definition**

`GET /cities`

**Specify City Name**

`GET /cities/<cityName>`

**Response**

- `200 OK` on success

### State

**Definition**

`GET /state/<stateName>`

**Response**

- `200 OK` on success