import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6321", "title": "Orders scenario 6321", "data": {"sku": "SKU6321", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6321@example.com", "threshold": 210}},
    {"id": "ORDERS-6322", "title": "Orders scenario 6322", "data": {"sku": "SKU6322", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6322@example.com", "threshold": 220}},
    {"id": "ORDERS-6323", "title": "Orders scenario 6323", "data": {"sku": "SKU6323", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6323@example.com", "threshold": 230}},
    {"id": "ORDERS-6324", "title": "Orders scenario 6324", "data": {"sku": "SKU6324", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6324@example.com", "threshold": 240}},
    {"id": "ORDERS-6325", "title": "Orders scenario 6325", "data": {"sku": "SKU6325", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6325@example.com", "threshold": 250}},
    {"id": "ORDERS-6326", "title": "Orders scenario 6326", "data": {"sku": "SKU6326", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6326@example.com", "threshold": 260}},
    {"id": "ORDERS-6327", "title": "Orders scenario 6327", "data": {"sku": "SKU6327", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6327@example.com", "threshold": 270}},
    {"id": "ORDERS-6328", "title": "Orders scenario 6328", "data": {"sku": "SKU6328", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6328@example.com", "threshold": 280}},
    {"id": "ORDERS-6329", "title": "Orders scenario 6329", "data": {"sku": "SKU6329", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6329@example.com", "threshold": 290}},
    {"id": "ORDERS-6330", "title": "Orders scenario 6330", "data": {"sku": "SKU6330", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6330@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
