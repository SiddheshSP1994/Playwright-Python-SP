import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-9741", "title": "Orders scenario 9741", "data": {"sku": "SKU9741", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9741@example.com", "threshold": 410}},
    {"id": "ORDERS-9742", "title": "Orders scenario 9742", "data": {"sku": "SKU9742", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9742@example.com", "threshold": 420}},
    {"id": "ORDERS-9743", "title": "Orders scenario 9743", "data": {"sku": "SKU9743", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9743@example.com", "threshold": 430}},
    {"id": "ORDERS-9744", "title": "Orders scenario 9744", "data": {"sku": "SKU9744", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9744@example.com", "threshold": 440}},
    {"id": "ORDERS-9745", "title": "Orders scenario 9745", "data": {"sku": "SKU9745", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9745@example.com", "threshold": 450}},
    {"id": "ORDERS-9746", "title": "Orders scenario 9746", "data": {"sku": "SKU9746", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9746@example.com", "threshold": 460}},
    {"id": "ORDERS-9747", "title": "Orders scenario 9747", "data": {"sku": "SKU9747", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9747@example.com", "threshold": 470}},
    {"id": "ORDERS-9748", "title": "Orders scenario 9748", "data": {"sku": "SKU9748", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9748@example.com", "threshold": 480}},
    {"id": "ORDERS-9749", "title": "Orders scenario 9749", "data": {"sku": "SKU9749", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9749@example.com", "threshold": 490}},
    {"id": "ORDERS-9750", "title": "Orders scenario 9750", "data": {"sku": "SKU9750", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9750@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
