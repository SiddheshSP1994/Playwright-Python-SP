import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1261", "title": "Checkout scenario 1261", "data": {"sku": "SKU1261", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1261@example.com", "threshold": 610}},
    {"id": "CHECKOUT-1262", "title": "Checkout scenario 1262", "data": {"sku": "SKU1262", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1262@example.com", "threshold": 620}},
    {"id": "CHECKOUT-1263", "title": "Checkout scenario 1263", "data": {"sku": "SKU1263", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1263@example.com", "threshold": 630}},
    {"id": "CHECKOUT-1264", "title": "Checkout scenario 1264", "data": {"sku": "SKU1264", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1264@example.com", "threshold": 640}},
    {"id": "CHECKOUT-1265", "title": "Checkout scenario 1265", "data": {"sku": "SKU1265", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1265@example.com", "threshold": 650}},
    {"id": "CHECKOUT-1266", "title": "Checkout scenario 1266", "data": {"sku": "SKU1266", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1266@example.com", "threshold": 660}},
    {"id": "CHECKOUT-1267", "title": "Checkout scenario 1267", "data": {"sku": "SKU1267", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1267@example.com", "threshold": 670}},
    {"id": "CHECKOUT-1268", "title": "Checkout scenario 1268", "data": {"sku": "SKU1268", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1268@example.com", "threshold": 680}},
    {"id": "CHECKOUT-1269", "title": "Checkout scenario 1269", "data": {"sku": "SKU1269", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1269@example.com", "threshold": 690}},
    {"id": "CHECKOUT-1270", "title": "Checkout scenario 1270", "data": {"sku": "SKU1270", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1270@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
