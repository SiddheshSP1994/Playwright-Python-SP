import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9321", "title": "Orders scenario 9321", "data": {"sku": "SKU9321", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9321@example.com", "threshold": 210}},
    {"id": "ORDERS-9322", "title": "Orders scenario 9322", "data": {"sku": "SKU9322", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9322@example.com", "threshold": 220}},
    {"id": "ORDERS-9323", "title": "Orders scenario 9323", "data": {"sku": "SKU9323", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9323@example.com", "threshold": 230}},
    {"id": "ORDERS-9324", "title": "Orders scenario 9324", "data": {"sku": "SKU9324", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9324@example.com", "threshold": 240}},
    {"id": "ORDERS-9325", "title": "Orders scenario 9325", "data": {"sku": "SKU9325", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9325@example.com", "threshold": 250}},
    {"id": "ORDERS-9326", "title": "Orders scenario 9326", "data": {"sku": "SKU9326", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9326@example.com", "threshold": 260}},
    {"id": "ORDERS-9327", "title": "Orders scenario 9327", "data": {"sku": "SKU9327", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9327@example.com", "threshold": 270}},
    {"id": "ORDERS-9328", "title": "Orders scenario 9328", "data": {"sku": "SKU9328", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9328@example.com", "threshold": 280}},
    {"id": "ORDERS-9329", "title": "Orders scenario 9329", "data": {"sku": "SKU9329", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9329@example.com", "threshold": 290}},
    {"id": "ORDERS-9330", "title": "Orders scenario 9330", "data": {"sku": "SKU9330", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9330@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
