get_order_schema = ''''openapi: 3.1.0
info:
  title: Shopmonkey API
  version: "2.0"
  description: API para obter informações de pedidos do Shopmonkey
servers:
  - url: https://api.shopmonkey.io/v2
paths:
  /orders:
    get:
      operationId: getOrders
      summary: Obter lista de pedidos
      description: Retorna uma lista de pedidos com base nos parâmetros fornecidos.
      parameters:
        - name: customerId
          in: query
          description: ID do cliente
          required: false
          schema:
            type: string
        - name: limit
          in: query
          description: Limite de resultados retornados (1 a 100)
          required: false
          schema:
            type: integer
            minimum: 1
            maximum: 100
        - name: number
          in: query
          description: Número do pedido
          required: false
          schema:
            type: integer
        - name: offset
          in: query
          description: Deslocamento dos resultados retornados
          required: false
          schema:
            type: integer
        - name: sort
          in: query
          description: Campo para ordenar os resultados
          required: false
          schema:
            type: string
        - name: vehicleId
          in: query
          description: ID do veículo
          required: false
          schema:
            type: string
        - name: workflow
          in: query
          description: Fluxo de trabalho
          required: false
          schema:
            type: string
        - name: updateDateStart
          in: query
          description: Data/hora inicial da atualização
          required: false
          schema:
            type: string
            format: date-time
        - name: updateDateEnd
          in: query
          description: Data/hora final da atualização
          required: false
          schema:
            type: string
            format: date-time
        - name: creationDateStart
          in: query
          description: Data/hora inicial da criação
          required: false
          schema:
            type: string
            format: date-time
        - name: creationDateEnd
          in: query
          description: Data/hora final da criação
          required: false
          schema:
            type: string
            format: date-time
        - name: customerShopmonkeyId
          in: query
          description: ID do cliente no Shopmonkey
          required: false
          schema:
            type: string
        - name: isArchived
          in: query
          description: Se o pedido está arquivado
          required: false
          schema:
            type: boolean
        - name: isAuthorized
          in: query
          description: Se o pedido está autorizado
          required: false
          schema:
            type: boolean
        - name: isInvoice
          in: query
          description: Se o pedido é uma fatura
          required: false
          schema:
            type: boolean
        - name: isPaid
          in: query
          description: Se o pedido está pago
          required: false
          schema:
            type: boolean
        - name: vehicleShopmonkeyId
          in: query
          description: ID do veículo no Shopmonkey
          required: false
          schema:
            type: string
      responses:
        "200":
          description: Lista de pedidos retornada com sucesso
          content:
            application/json:
              schema:
                type: object
                properties:
                  orders:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        customerId:
                          type: string
                        vehicleId:
                          type: string
                        number:
                          type: integer
                        workflow:
                          type: string
                        updateDate:
                          type: string
                          format: date-time
                        creationDate:
                          type: string
                          format: date-time
                        isArchived:
                          type: boolean
                        isAuthorized:
                          type: boolean
                        isInvoice:
                          type: boolean
                        isPaid:
                          type: boolean
        "400":
          description: Solicitação inválida
        "401":
          description: Não autorizado
        "500":
          description: Erro interno do servidor
'''