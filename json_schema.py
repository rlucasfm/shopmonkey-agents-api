get_order_json_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "description": "Schema for a car service orders api",
    "type": "object",
    "properties": {
        "orders": {
            "description": "List of car service records",
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "authorizedDate": {
                        "description": "Date when the service was authorized",
                        "type": "string",
                        "format": "date-time"
                    },
                    "complaint": {
                        "description": "Complaint reported by the customer",
                        "type": ["string", "null"]
                    },
                    "completedDate": {
                        "description": "Date when the service was completed",
                        "type": ["string", "null"],
                        "format": "date-time"
                    },
                    "creationDate": {
                        "description": "Date when the record was created",
                        "type": "string",
                        "format": "date-time"
                    },
                    "dueDate": {
                        "description": "Date when the service is due",
                        "type": ["string", "null"],
                        "format": "date-time"
                    },
                    "invoicedDate": {
                        "description": "Date when the invoice was issued",
                        "type": "string",
                        "format": "date-time"
                    },
                    "isArchived": {
                        "description": "Indicates if the record is archived",
                        "type": "boolean"
                    },
                    "isAuthorized": {
                        "description": "Indicates if the service is authorized",
                        "type": "boolean"
                    },
                    "isInvoice": {
                        "description": "Indicates if the record is an invoice",
                        "type": "boolean"
                    },
                    "isLaborShopSupplies": {
                        "description": "Indicates if labor shop supplies are included",
                        "type": "boolean"
                    },
                    "isLaborTaxable": {
                        "description": "Indicates if labor is taxable",
                        "type": "boolean"
                    },
                    "isPaid": {
                        "description": "Indicates if the service is paid",
                        "type": "boolean"
                    },
                    "isPartShopSupplies": {
                        "description": "Indicates if part shop supplies are included",
                        "type": "boolean"
                    },
                    "jobCardPosition": {
                        "description": "Position of the job card",
                        "type": "integer"
                    },
                    "number": {
                        "description": "Service record number",
                        "type": "integer"
                    },
                    "paidAmount": {
                        "description": "Amount paid for the service",
                        "type": "number"
                    },
                    "poNumber": {
                        "description": "Purchase order number",
                        "type": "string"
                    },
                    "publicId": {
                        "description": "Public identifier for the service record",
                        "type": "string"
                    },
                    "sendCollectPayment": {
                        "description": "Indicates if payment collection is sent",
                        "type": "boolean"
                    },
                    "sendCustomerAuthorize": {
                        "description": "Indicates if customer authorization is sent",
                        "type": "boolean"
                    },
                    "sendDisplayActivity": {
                        "description": "Indicates if display activity is sent",
                        "type": "boolean"
                    },
                    "sendDisplayAuthorizations": {
                        "description": "Indicates if display authorizations are sent",
                        "type": "boolean"
                    },
                    "sendDisplayMessages": {
                        "description": "Indicates if display messages are sent",
                        "type": "boolean"
                    },
                    "sendRequestedAmount": {
                        "description": "Requested amount to be sent",
                        "type": "number"
                    },
                    "shopmonkeyId": {
                        "description": "Shopmonkey identifier",
                        "type": "string"
                    },
                    "techRecommendation": {
                        "description": "Technical recommendation",
                        "type": ["string", "null"]
                    },
                    "totalAmount": {
                        "description": "Total amount for the service",
                        "type": "number"
                    },
                    "updateDate": {
                        "description": "Date when the record was last updated",
                        "type": "string",
                        "format": "date-time"
                    },
                    "name": {
                        "description": "Name of the service",
                        "type": "string"
                    },
                    "workflow": {
                        "description": "Workflow status",
                        "type": "string"
                    },
                    "workflowId": {
                        "description": "Workflow identifier",
                        "type": "string"
                    },
                    "tags": {
                        "description": "List of tags associated with the service",
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "description": "Tag name",
                                    "type": "string"
                                },
                                "color": {
                                    "description": "Tag color",
                                    "type": "string"
                                },
                                "shopmonkeyId": {
                                    "description": "Shopmonkey identifier for the tag",
                                    "type": "string"
                                }
                            },
                            "required": ["name"]
                        }
                    },
                    "customer": {
                        "description": "Customer details",
                        "type": "object",
                        "properties": {
                            "shopmonkeyId": {
                                "description": "Shopmonkey identifier for the customer",
                                "type": "string"
                            },
                            "firstName": {
                                "description": "First name of the customer",
                                "type": "string"
                            },
                            "lastName": {
                                "description": "Last name of the customer",
                                "type": "string"
                            },
                            "email": {
                                "description": "Email of the customer",
                                "type": ["string", "null"],
                                "format": "email"
                            },
                            "phone": {
                                "description": "Phone number of the customer",
                                "type": ["string", "null"],
                                "pattern": "^\\+?[1-9]\\d{1,14}$"
                            }
                        },
                        "required": ["shopmonkeyId", "firstName", "lastName"]
                    },
                    "vehicle": {
                        "description": "Vehicle details",
                        "type": "object",
                        "properties": {
                            "shopmonkeyId": {
                                "description": "Shopmonkey identifier for the vehicle",
                                "type": "string"
                            },
                            "make": {
                                "description": "Make of the vehicle",
                                "type": "string"
                            },
                            "model": {
                                "description": "Model of the vehicle",
                                "type": "string"
                            },
                            "year": {
                                "description": "Year of the vehicle",
                                "type": "integer"
                            },
                            "type": {
                                "description": "Type of the vehicle",
                                "type": "string"
                            },
                            "vin": {
                                "description": "VIN of the vehicle",
                                "type": "string"
                            },
                            "licensePlate": {
                                "description": "License plate of the vehicle",
                                "type": ["string", "null"]
                            },
                            "submodel": {
                                "description": "Submodel of the vehicle",
                                "type": ["string", "null"]
                            }
                        },
                        "required": ["shopmonkeyId", "make", "model", "year", "type", "vin"]
                    },
                    "serviceWriter": {
                        "description": "Service writer details",
                        "type": "object",
                        "properties": {
                            "shopmonkeyId": {
                                "description": "Shopmonkey identifier for the service writer",
                                "type": "string"
                            },
                            "firstName": {
                                "description": "First name of the service writer",
                                "type": "string"
                            },
                            "lastName": {
                                "description": "Last name of the service writer",
                                "type": "string"
                            }
                        },
                        "required": ["shopmonkeyId", "firstName", "lastName"]
                    },
                    "paymentTerm": {
                        "description": "Payment terms",
                        "type": "object",
                        "properties": {
                            "shopmonkeyId": {
                                "description": "Shopmonkey identifier for the payment term",
                                "type": "string"
                            },
                            "name": {
                                "description": "Name of the payment term",
                                "type": "string"
                            }
                        },
                        "required": ["shopmonkeyId", "name"]
                    }
                },
                "required": ["authorizedDate", "creationDate", "invoicedDate", "isArchived", "isAuthorized", "isInvoice", "isLaborShopSupplies", "isLaborTaxable", "isPaid", "isPartShopSupplies", "jobCardPosition", "number", "paidAmount", "publicId", "sendCollectPayment", "sendCustomerAuthorize", "sendDisplayActivity", "sendDisplayAuthorizations", "sendDisplayMessages", "shopmonkeyId", "totalAmount", "updateDate", "name", "workflow", "workflowId", "customer", "vehicle", "serviceWriter", "paymentTerm"]
            }
        }
    },
    "required": ["orders"]
}
