import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0981", "title": "Orders scenario 981", "data": {"sku": "SKU981", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user981@example.com", "threshold": 810}},
    {"id": "ORDERS-0982", "title": "Orders scenario 982", "data": {"sku": "SKU982", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user982@example.com", "threshold": 820}},
    {"id": "ORDERS-0983", "title": "Orders scenario 983", "data": {"sku": "SKU983", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user983@example.com", "threshold": 830}},
    {"id": "ORDERS-0984", "title": "Orders scenario 984", "data": {"sku": "SKU984", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user984@example.com", "threshold": 840}},
    {"id": "ORDERS-0985", "title": "Orders scenario 985", "data": {"sku": "SKU985", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user985@example.com", "threshold": 850}},
    {"id": "ORDERS-0986", "title": "Orders scenario 986", "data": {"sku": "SKU986", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user986@example.com", "threshold": 860}},
    {"id": "ORDERS-0987", "title": "Orders scenario 987", "data": {"sku": "SKU987", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user987@example.com", "threshold": 870}},
    {"id": "ORDERS-0988", "title": "Orders scenario 988", "data": {"sku": "SKU988", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user988@example.com", "threshold": 880}},
    {"id": "ORDERS-0989", "title": "Orders scenario 989", "data": {"sku": "SKU989", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user989@example.com", "threshold": 890}},
    {"id": "ORDERS-0990", "title": "Orders scenario 990", "data": {"sku": "SKU990", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user990@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
