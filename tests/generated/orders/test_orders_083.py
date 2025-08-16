import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4941", "title": "Orders scenario 4941", "data": {"sku": "SKU4941", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4941@example.com", "threshold": 410}},
    {"id": "ORDERS-4942", "title": "Orders scenario 4942", "data": {"sku": "SKU4942", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4942@example.com", "threshold": 420}},
    {"id": "ORDERS-4943", "title": "Orders scenario 4943", "data": {"sku": "SKU4943", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4943@example.com", "threshold": 430}},
    {"id": "ORDERS-4944", "title": "Orders scenario 4944", "data": {"sku": "SKU4944", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4944@example.com", "threshold": 440}},
    {"id": "ORDERS-4945", "title": "Orders scenario 4945", "data": {"sku": "SKU4945", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4945@example.com", "threshold": 450}},
    {"id": "ORDERS-4946", "title": "Orders scenario 4946", "data": {"sku": "SKU4946", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4946@example.com", "threshold": 460}},
    {"id": "ORDERS-4947", "title": "Orders scenario 4947", "data": {"sku": "SKU4947", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4947@example.com", "threshold": 470}},
    {"id": "ORDERS-4948", "title": "Orders scenario 4948", "data": {"sku": "SKU4948", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4948@example.com", "threshold": 480}},
    {"id": "ORDERS-4949", "title": "Orders scenario 4949", "data": {"sku": "SKU4949", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4949@example.com", "threshold": 490}},
    {"id": "ORDERS-4950", "title": "Orders scenario 4950", "data": {"sku": "SKU4950", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4950@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
