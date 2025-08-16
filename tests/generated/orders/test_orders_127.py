import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-7581", "title": "Orders scenario 7581", "data": {"sku": "SKU7581", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7581@example.com", "threshold": 810}},
    {"id": "ORDERS-7582", "title": "Orders scenario 7582", "data": {"sku": "SKU7582", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7582@example.com", "threshold": 820}},
    {"id": "ORDERS-7583", "title": "Orders scenario 7583", "data": {"sku": "SKU7583", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7583@example.com", "threshold": 830}},
    {"id": "ORDERS-7584", "title": "Orders scenario 7584", "data": {"sku": "SKU7584", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7584@example.com", "threshold": 840}},
    {"id": "ORDERS-7585", "title": "Orders scenario 7585", "data": {"sku": "SKU7585", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7585@example.com", "threshold": 850}},
    {"id": "ORDERS-7586", "title": "Orders scenario 7586", "data": {"sku": "SKU7586", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7586@example.com", "threshold": 860}},
    {"id": "ORDERS-7587", "title": "Orders scenario 7587", "data": {"sku": "SKU7587", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7587@example.com", "threshold": 870}},
    {"id": "ORDERS-7588", "title": "Orders scenario 7588", "data": {"sku": "SKU7588", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7588@example.com", "threshold": 880}},
    {"id": "ORDERS-7589", "title": "Orders scenario 7589", "data": {"sku": "SKU7589", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7589@example.com", "threshold": 890}},
    {"id": "ORDERS-7590", "title": "Orders scenario 7590", "data": {"sku": "SKU7590", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7590@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
