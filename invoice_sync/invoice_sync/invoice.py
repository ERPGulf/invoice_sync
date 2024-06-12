import requests
import json
import frappe
import json
import urllib.parse;
import base64
from werkzeug.wrappers import Response


@frappe.whitelist(allow_guest=True)
def generate_token_secure( api_key, api_secret, app_key):
                
               
                try:
                    try:
                        app_key = base64.b64decode(app_key).decode("utf-8")
                    except Exception as e:
                        return Response(json.dumps({"message": "Security Parameters are not valid" , "user_count": 0}), status=401, mimetype='application/json')
                    clientID, clientSecret, clientUser = frappe.db.get_value('OAuth Client', {'app_name': app_key}, ['client_id', 'client_secret','user'])
                    
                    if clientID is None:
                        # return app_key
                        return Response(json.dumps({"message": "Security Parameters are not valid" , "user_count": 0}), status=401, mimetype='application/json')
                    
                    client_id = clientID  # Replace with your OAuth client ID
                    client_secret = clientSecret  # Replace with your OAuth client secret
                    url =  frappe.local.conf.host_name  + "/api/method/frappe.integrations.oauth2.get_token"
                    payload = {
                        "username": api_key,
                        "password": api_secret,
                        "grant_type": "password",
                        "client_id": client_id,
                        "client_secret": client_secret,
                        
                    }
                    files = []
                    headers = {"Content-Type": "application/json"}
                    response = requests.request("POST", url, data=payload, files=files)
                    if response.status_code == 200:
                        result_data = json.loads(response.text)
                        return Response(json.dumps({"data":result_data}), status=200, mimetype='application/json')
                    
                        
                    else:
                        
                        frappe.local.response.http_status_code = 401
                        return json.loads(response.text)
                        
                    
                except Exception as e:
                        
                        
                        return Response(json.dumps({"message": e , "user_count": 0}), status=500, mimetype='application/json')
    
    
    
    
    
                    
@frappe.whitelist(allow_guest=True)      
def create_refresh_token(refresh_token):
                    url =  frappe.local.conf.host_name  + "/api/method/frappe.integrations.oauth2.get_token"
                    payload = f'grant_type=refresh_token&refresh_token={refresh_token}'
                    headers = {
                        'Content-Type': 'application/x-www-form-urlencoded'
                    }
                    files = []
                    
                    response = requests.post(url, headers=headers, data=payload, files=files)

                    
                    if response.status_code == 200:
                        try:
                            
                            message_json = json.loads(response.text)
                            
                          
                            new_message = {
                                "access_token": message_json["access_token"],
                                "expires_in": message_json["expires_in"],
                                "token_type": message_json["token_type"],
                                "scope": message_json["scope"],
                                "refresh_token": message_json["refresh_token"]
                            }

                           
                            return  Response(json.dumps({"data": new_message}), status=200, mimetype='application/json')
                        except json.JSONDecodeError as e:
                            return  Response(json.dumps({"data": f"Error decoding JSON: {e}"}), status=401, mimetype='application/json')
                    else:
                        
                        return  Response(json.dumps({"data": response.text}), status=401, mimetype='application/json')





@frappe.whitelist()
def customer(customer, customer_type, phone, email,is_supplier=False):
                    response_content =frappe.session.user
                    is_supplier = is_supplier.lower() in ['true', '1', 'yes'] if isinstance(is_supplier, str) else bool(is_supplier)
                    
                    if not is_supplier:
                
                        email_result = []

                        
                        if email is not None:
                            email_result = frappe.get_all("Customer", fields=["name as id", "customer_name", "customer_type", "mobile_no", "custom_email as email"],
                                                        filters={'custom_email': ['like', email]})

                        if not email_result:
                            customer_doc = frappe.get_doc({
                                "doctype": "Customer",
                                "customer_name": customer,
                                "customer_type": customer_type,
                                "mobile_no": phone,
                                "custom_email": email,
                                
                            })

                            customer_doc.insert(ignore_permissions=True)
                            customer_doc.save()

                            details = frappe.get_all("Customer", fields=["name as id", "customer_name", "customer_type", "mobile_no", "custom_email as email",],
                                                    filters={'name': ['like', customer_doc.name]})

                            data = {
                                "message": "Customer created successfully.",
                                "Details": details,
                            }

                        
                            return  Response(json.dumps({"data":data}), status=200, mimetype='application/json')


                        else:
                            data = {
                                "message": "Customer already exists",
                                "Details": email_result
                            }
                        
                        
                            return  Response(json.dumps({"data":data}), status=409, mimetype='application/json')

                    else:
                        suplr_already_exist=frappe.get_all("Supplier", fields=["name as id", "supplier_name", "custom_email as email", "custom_mobileno as phone"],
                                                            filters={'name': ['like',customer]})
                        details={
                            "message":"Already exists",
                            "Details":suplr_already_exist
                        }
                        if suplr_already_exist:
                            return  Response(json.dumps({"data":details }), status=409, mimetype='application/json')
                        supplier_doc = frappe.get_doc({
                                "doctype": "Supplier",
                                "supplier_name": customer,
                                "custom_mobileno": phone,
                                "custom_email": email,
                            })
                        supplier_doc.insert(ignore_permissions=True)

                        supplier_details = frappe.get_all("Supplier", fields=["name as id", "supplier_name", "custom_email as email", "custom_mobileno as phone"],
                                                            filters={'name': ['like', supplier_doc.name]})
                        suplr={
                            "Details":supplier_details
                        }
                        return  Response(json.dumps({"data":suplr}), status=200, mimetype='application/json')

                    

@frappe.whitelist()
def customer1(customer, phone, email, is_supplier=False, user_id=None):
            try:
                return "hello"

            except frappe.exceptions.PermissionError as e:
                return Response(json.dumps({"message": "Permission error"}), status=401, mimetype='application/json')
            except Exception as e:
               
                return Response(json.dumps({"message": str(e)}), status=500, mimetype='application/json')



@frappe.whitelist()
def create_invoice(customer_id, supplier_id, payment_method, items, taxes, Customer_Purchase_Order,discount_amount=None):
        if not taxes:
            return Response(json.dumps({"data": "taxes information not provided"}), status=404, mimetype='application/json')

        customer_details = frappe.get_all("Customer", fields=["name"], filters={'name': ['like', customer_id]})
        if not customer_details:
            return Response(json.dumps({"data": "customer id not found"}), status=404, mimetype='application/json')

        supplier_details = frappe.get_all("Supplier", fields=["name"], filters={'name': ['like', supplier_id]})
        if not supplier_details:
            return Response(json.dumps({"data": "supplier id not found"}), status=404, mimetype='application/json')
        try:
            invoice_items = []
            company = frappe.defaults.get_defaults().company
            doc = frappe.get_doc("Company", company)

            income_account = doc.default_income_account

            for item in items:
                item_code = item["item_name"]
                item_exists = frappe.get_value("Item", {"name": item_code}, "name")

                if not item_exists:
                    invoice_item = {
                        "item_name": item_code,
                        "qty": item.get("quantity", 0),
                        "rate": item.get("rate", 0),
                        "uom": item.get("uom", "Nos"),
                        "income_account": item.get("income_account", income_account)
                    }
                else:
                    invoice_item = {
                        "item_code": item_code,
                        "qty": item.get("quantity", 0),
                        "rate": item.get("rate", 0),
                    }

                invoice_items.append(invoice_item)

            taxes_list = []
            for tax in taxes:
                charge_type = tax.get("charge_type")
                account_head = tax.get("account_head")
                amount = tax.get("amount")
                description=tax.get("description")

                if charge_type and account_head and amount is not None:
                    taxes_list.append({
                        "charge_type": charge_type,
                        "account_head": account_head,
                        "tax_amount": amount,
                        "description": description
                    })

            new_invoice = frappe.get_doc({
                "doctype": "Sales Invoice",
                "customer": customer_id,
                "custom_supplier_id": supplier_id,
                "custom_payment_method": payment_method,
                "discount_amount":discount_amount,
                "items": invoice_items,
                "taxes": taxes_list,
                "po_no": Customer_Purchase_Order
            })

            new_invoice.insert(ignore_permissions=True)
            new_invoice.save()
            iitem = frappe.get_doc("Sales Invoice", new_invoice.name)

            attribute_dict = []
            for attribute in iitem.items:
                attribute_data = {
                    "item_name": attribute.item_name,
                    "item_code": attribute.item_code,
                    "quantity": attribute.qty,
                    "rate": attribute.rate,
                    "uom": attribute.uom,
                    "income_account": attribute.income_account
                }
                attribute_dict.append(attribute_data)
            sales_dict=[]
            for sales in iitem.taxes:
                sales_data={
                    "charge_type": sales.charge_type,
                    "account_head": sales.account_head,
                    "tax_amount": sales.tax_amount,
                    "total":sales.total,
                    "description": sales.description
                    
                }
                sales_dict.append(sales_data)
            customer_info = {
                "id": new_invoice.name,
                "customer_id": new_invoice.customer,
                "customer_name": new_invoice.customer_name,
                "supplier_id": new_invoice.custom_supplier_id,
                "payment_method": new_invoice.custom_payment_method,
                "total_quantity": new_invoice.total_qty,
                "total": new_invoice.total,
                "grand_total": new_invoice.grand_total,
                "Customer's Purchase Order": int(new_invoice.po_no),
                "discount_amount":new_invoice.discount_amount,
                "items": attribute_dict,
                "taxes":sales_dict
            }

            return Response(json.dumps({"data": customer_info}), status=200, mimetype='application/json')

        except Exception as e:
                return Response(json.dumps({"message": str(e)}), status=404, mimetype='application/json')


