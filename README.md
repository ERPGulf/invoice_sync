get-app https://github.com/ERPGulf/invoice_sync.git \
bench --site yoursite.erpgulf.com invoice_sync \
bench --site yoursite.erpgulf.com migrate \
Goto Help->About and make sure you have invoice_sync app installaed.



## Generate token and refresh_key (GET)
The generate token secure API is designed to facilitate secure authentication and token generation for accessing resources within the system.It generate token and refresh key.Here the request parameters are api key, api secret and app key. user-related parameters are included in the request headers as cookies.
### Request

```
curl --location '/api/method/invoice_sync.invoice_sync.invoice.generate_token_secure' \
--header 'Cookie: full_name=Guest; sid=Guest; system_user=no; user_id=Guest; user_image=; full_name=Guest; sid=Guest; system_user=no; user_id=Guest; user_image=; sid=Guest; full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image=; full_name=Guest; system_user=no; user_id=Guest; user_image=' \
--header 'Content-Type: application/json' \
--data-raw '{
    "api_key":"your key",
"api_secret":"api secret",
"app_key":"key==",
"client_secret":" your client secret"
}'

```
### Response
```
{
    "data": {
        "access_token": "token",
        "expires_in": 3600,
        "token_type": "Bearer",
        "scope": "all openid",
        "refresh_token": "token"
    }
}

```

## create_refresh_token
The create_refresh_token API is designed to facilitate secure authentication and token generation for accessing resources within the system.It generate token and refresh key.Here the request parameters are refresh token that already generated with the help of Generate token and refresh_key api. user-related parameters are included in the request headers as cookies.
### Request

```
curl --location --request GET '/api/method/invoice_sync.invoice_sync.invoice.create_refresh_token' \
--header 'Cookie: full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image=; full_name=Guest; system_user=no; user_id=Guest; user_image=' \
--form 'refresh_token="token"'
```
### Response
```
{
    "data": {
        "access_token": "token",
        "expires_in": 3600,
        "token_type": "Bearer",
        "scope": "all openid",
        "refresh_token": "token"
    }
}
```

##  create customer or supplier
this api is used to create customer when we pass parameters like customer,customer_type,phone,email and is_supplier field need to be false, then only customer list create.if is_supplier field is true then supplier list will create with the help of this parameters,if already customer exist the it shows the details of that customer same way if the supplier exist then it shows the details of that supplier,Here authentication  is required.user-related parameters are included in the request headers as cookies needed.
### Request

```
curl --location 'https://pi/method/invoice_sync.invoice_sync.invoice.customer' \
--header 'Authorization: Bearer ' \
--header 'Cookie: full_name=Guest; sid=Guest; system_user=no; user_id=Guest; user_image=' \
--form 'customer="testing31"' \
--form 'customer_type="Company"' \
--form 'phone=""' \
--form 'email="testing31@gmail.com"' \
--form 'is_supplier="true"'

```
### Response
```
{
    "data": {
        "Details": [
            {
                "id": "testing35",
                "supplier_name": "testing35",
                "email": "testing35@gmail.com",
                "phone": "987654321"
            }
        ]
    }
}
```

## create sales invoice
This api is used to create sales invoice using customer id,supplier id and payment method and we can add multiple items .



### Request

```
curl --location 'https://api/method/invoice_sync.invoice_sync.invoice.create_invoice' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer k' \
--header 'Cookie: full_name=Guest; sid=Guest; system_user=no; user_id=Guest; user_image=' \
--data '
{
  "customer_id":"C-00008",
  "supplier_id":"testing17",
  "payment_method":"cash",
  "items": [
    {"item_name": "pencil", "quantity": 5, "rate": 10.0},
    {"item_name": "pencil1", "quantity": 3, "rate": 15.0}
   
  ]
}
'
```
### Response
```
{
    "data": {
        "id": "ACC-SINV-2024-00080",
        "customer_id": "C-00008",
        "customer_name": "testing26",
        "supplier_id": "testing17",
        "payment_method": "cash",
        "total_quantity": 8.0,
        "total": 95.0,
        "grand_total": 95.0,
        "items": [
            {
                "item_name": "pencil",
                "item_code": "pencil",
                "quantity": 5.0,
                "rate": 10.0,
                "uom": "Unit",
                "income_account": "Sales - erp"
            },
            {
                "item_name": "pencil1",
                "item_code": null,
                "quantity": 3.0,
                "rate": 15.0,
                "uom": "Nos",
                "income_account": "Sales - erp"
            }
        ]
    }
}
```

