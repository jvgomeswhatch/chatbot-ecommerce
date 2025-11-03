# actions/actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

# Simulação de um banco de dados de produtos e pedidos
mock_products = {
    "camisetas": ["Camiseta Estampada", "Camiseta Básica", "Regata"],
    "calças": ["Calça Jeans", "Calça de Moletom", "Calça Social"],
    "sapatos": ["Tênis de Corrida", "Sapato Social", "Sandália"]
}

mock_orders = {
    "12345": "Seu pedido está a caminho!",
    "ABC-123": "Seu pedido foi entregue.",
    "54321": "Pagamento confirmado. Preparando para envio."
}

class ActionRecommendProduct(Action):
    def name(self) -> Text:
        return "action_recommend_product"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        category = next(tracker.get_latest_entity_values("product_category"), None)

        if category and category.lower() in mock_products:
            product = random.choice(mock_products[category.lower()])
            dispatcher.utter_message(text=f"Que tal esta opção: {product}?")
        else:
            dispatcher.utter_message(text="Não encontrei produtos para essa categoria. Temos camisetas, calças e sapatos.")

        return []

class ActionGetOrderStatus(Action):
    def name(self) -> Text:
        return "action_get_order_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        order_id = next(tracker.get_latest_entity_values("order_id"), None)

        if order_id and order_id in mock_orders:
            status = mock_orders[order_id]
            dispatcher.utter_message(text=f"O status do pedido {order_id} é: {status}")
        else:
            dispatcher.utter_message(action="utter_order_status_not_found")

        return []