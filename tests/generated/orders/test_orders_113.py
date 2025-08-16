import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6741", "title": "Orders scenario 6741", "data": {"sku": "SKU6741", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6741@example.com", "threshold": 410}},
    {"id": "ORDERS-6742", "title": "Orders scenario 6742", "data": {"sku": "SKU6742", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6742@example.com", "threshold": 420}},
    {"id": "ORDERS-6743", "title": "Orders scenario 6743", "data": {"sku": "SKU6743", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6743@example.com", "threshold": 430}},
    {"id": "ORDERS-6744", "title": "Orders scenario 6744", "data": {"sku": "SKU6744", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6744@example.com", "threshold": 440}},
    {"id": "ORDERS-6745", "title": "Orders scenario 6745", "data": {"sku": "SKU6745", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6745@example.com", "threshold": 450}},
    {"id": "ORDERS-6746", "title": "Orders scenario 6746", "data": {"sku": "SKU6746", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6746@example.com", "threshold": 460}},
    {"id": "ORDERS-6747", "title": "Orders scenario 6747", "data": {"sku": "SKU6747", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6747@example.com", "threshold": 470}},
    {"id": "ORDERS-6748", "title": "Orders scenario 6748", "data": {"sku": "SKU6748", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6748@example.com", "threshold": 480}},
    {"id": "ORDERS-6749", "title": "Orders scenario 6749", "data": {"sku": "SKU6749", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6749@example.com", "threshold": 490}},
    {"id": "ORDERS-6750", "title": "Orders scenario 6750", "data": {"sku": "SKU6750", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6750@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
