import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0321", "title": "Orders scenario 321", "data": {"sku": "SKU321", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user321@example.com", "threshold": 210}},
    {"id": "ORDERS-0322", "title": "Orders scenario 322", "data": {"sku": "SKU322", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user322@example.com", "threshold": 220}},
    {"id": "ORDERS-0323", "title": "Orders scenario 323", "data": {"sku": "SKU323", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user323@example.com", "threshold": 230}},
    {"id": "ORDERS-0324", "title": "Orders scenario 324", "data": {"sku": "SKU324", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user324@example.com", "threshold": 240}},
    {"id": "ORDERS-0325", "title": "Orders scenario 325", "data": {"sku": "SKU325", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user325@example.com", "threshold": 250}},
    {"id": "ORDERS-0326", "title": "Orders scenario 326", "data": {"sku": "SKU326", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user326@example.com", "threshold": 260}},
    {"id": "ORDERS-0327", "title": "Orders scenario 327", "data": {"sku": "SKU327", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user327@example.com", "threshold": 270}},
    {"id": "ORDERS-0328", "title": "Orders scenario 328", "data": {"sku": "SKU328", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user328@example.com", "threshold": 280}},
    {"id": "ORDERS-0329", "title": "Orders scenario 329", "data": {"sku": "SKU329", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user329@example.com", "threshold": 290}},
    {"id": "ORDERS-0330", "title": "Orders scenario 330", "data": {"sku": "SKU330", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user330@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
